import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB_FILE = Path(__file__).resolve().parent / "guardrive.db"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def get_connection():
    conn = sqlite3.connect(
        str(DB_FILE),
        timeout=30,
        check_same_thread=False,
    )
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")
    return conn


def init_db():
    with get_connection() as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS drivers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL UNIQUE,
                active INTEGER NOT NULL DEFAULT 1,
                created_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS locations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                driver_id INTEGER NOT NULL,
                latitude REAL NOT NULL,
                longitude REAL NOT NULL,
                speed REAL NOT NULL DEFAULT 0,
                battery REAL,
                recorded_at TEXT NOT NULL,
                FOREIGN KEY (driver_id) REFERENCES drivers(id) ON DELETE CASCADE
            );

            CREATE INDEX IF NOT EXISTS idx_locations_driver_id
                ON locations(driver_id);

            CREATE INDEX IF NOT EXISTS idx_locations_driver_time
                ON locations(driver_id, id DESC);

            CREATE TABLE IF NOT EXISTS access_requests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                driver_id INTEGER NOT NULL,
                requester_name TEXT NOT NULL,
                requester_phone TEXT NOT NULL,
                duration TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'PENDING',
                created_at TEXT NOT NULL,
                expires_at TEXT,
                FOREIGN KEY (driver_id) REFERENCES drivers(id) ON DELETE CASCADE
            );

            CREATE INDEX IF NOT EXISTS idx_access_driver
                ON access_requests(driver_id);

            CREATE INDEX IF NOT EXISTS idx_access_lookup
                ON access_requests(driver_id, requester_phone, status);
            """
        )


def create_driver(name: str, phone: str):
    name = name.strip()
    phone = phone.strip()

    with get_connection() as conn:
        try:
            cur = conn.execute(
                """
                INSERT INTO drivers (name, phone, active, created_at)
                VALUES (?, ?, 1, ?)
                """,
                (name, phone, utc_now_iso()),
            )
            return cur.lastrowid
        except sqlite3.IntegrityError:
            return None


def get_driver_by_phone(phone: str):
    with get_connection() as conn:
        return conn.execute(
            """
            SELECT *
            FROM drivers
            WHERE phone = ?
              AND active = 1
            LIMIT 1
            """,
            (phone.strip(),),
        ).fetchone()


def get_driver_by_id(driver_id: int):
    with get_connection() as conn:
        return conn.execute(
            """
            SELECT *
            FROM drivers
            WHERE id = ?
            LIMIT 1
            """,
            (int(driver_id),),
        ).fetchone()


def save_location(
    driver_id: int,
    latitude: float,
    longitude: float,
    speed: float = 0,
    battery=None,
):
    with get_connection() as conn:
        conn.execute(
            """
            INSERT INTO locations
                (driver_id, latitude, longitude, speed, battery, recorded_at)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                int(driver_id),
                float(latitude),
                float(longitude),
                float(speed or 0),
                battery,
                utc_now_iso(),
            ),
        )


def get_latest_location(driver_id: int):
    with get_connection() as conn:
        return conn.execute(
            """
            SELECT *
            FROM locations
            WHERE driver_id = ?
            ORDER BY id DESC
            LIMIT 1
            """,
            (int(driver_id),),
        ).fetchone()


def get_location_history(driver_id: int, limit: int = 100):
    limit = max(1, min(int(limit), 1000))

    with get_connection() as conn:
        return conn.execute(
            """
            SELECT *
            FROM locations
            WHERE driver_id = ?
            ORDER BY id DESC
            LIMIT ?
            """,
            (int(driver_id), limit),
        ).fetchall()


def create_access_request(
    driver_id: int,
    requester_name: str,
    requester_phone: str,
    duration: str,
):
    with get_connection() as conn:
        cur = conn.execute(
            """
            INSERT INTO access_requests
                (
                    driver_id,
                    requester_name,
                    requester_phone,
                    duration,
                    status,
                    created_at
                )
            VALUES (?, ?, ?, ?, 'PENDING', ?)
            """,
            (
                int(driver_id),
                requester_name.strip(),
                requester_phone.strip(),
                duration,
                utc_now_iso(),
            ),
        )
        return cur.lastrowid


def get_driver_requests(driver_id: int):
    with get_connection() as conn:
        return conn.execute(
            """
            SELECT *
            FROM access_requests
            WHERE driver_id = ?
            ORDER BY id DESC
            """,
            (int(driver_id),),
        ).fetchall()


def get_access_request(request_id: int):
    with get_connection() as conn:
        return conn.execute(
            """
            SELECT *
            FROM access_requests
            WHERE id = ?
            LIMIT 1
            """,
            (int(request_id),),
        ).fetchone()


def update_access_request(request_id: int, status: str, expires_at=None):
    with get_connection() as conn:
        conn.execute(
            """
            UPDATE access_requests
            SET status = ?, expires_at = ?
            WHERE id = ?
            """,
            (status, expires_at, int(request_id)),
        )


def check_location_access(driver_id: int, requester_phone: str):
    expire_old_access()

    with get_connection() as conn:
        access = conn.execute(
            """
            SELECT *
            FROM access_requests
            WHERE driver_id = ?
              AND requester_phone = ?
              AND status = 'ACTIVE'
            ORDER BY id DESC
            LIMIT 1
            """,
            (int(driver_id), requester_phone.strip()),
        ).fetchone()

    if not access:
        return False, None

    if access["duration"] == "UNTIL_REVOKED":
        return True, access

    expires_at = access["expires_at"]
    if not expires_at:
        return False, None

    try:
        expiry = datetime.fromisoformat(expires_at)
        if expiry.tzinfo is None:
            expiry = expiry.replace(tzinfo=timezone.utc)

        if datetime.now(timezone.utc) < expiry:
            return True, access
    except (TypeError, ValueError):
        pass

    return False, None


def expire_old_access():
    now = utc_now_iso()

    with get_connection() as conn:
        conn.execute(
            """
            UPDATE access_requests
            SET status = 'EXPIRED'
            WHERE status = 'ACTIVE'
              AND expires_at IS NOT NULL
              AND expires_at <= ?
            """,
            (now,),
        )


def revoke_access(request_id: int):
    update_access_request(
        request_id=request_id,
        status="REVOKED",
        expires_at=None,
    )


def deny_access(request_id: int):
    update_access_request(
        request_id=request_id,
        status="DENIED",
        expires_at=None,
    )


init_db()

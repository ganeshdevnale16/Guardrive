# import streamlit as st

# from datetime import datetime, timezone

# from streamlit_autorefresh import st_autorefresh

# import database


# st.set_page_config(
#     page_title="Guardrive | Family Access",
#     page_icon="👥",
#     layout="wide",
#     initial_sidebar_state="collapsed",
# )


# if not st.session_state.get("authenticated", False):
#     st.switch_page("app.py")


# if "family_driver_id" not in st.session_state:
#     st.session_state.family_driver_id = None


# st.markdown(
#     """
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

#     html, body, [class*="css"] {
#         font-family: "Inter", sans-serif;
#     }

#     #MainMenu, header, footer {
#         visibility: hidden;
#     }

#     .block-container {
#         max-width: 1000px;
#         padding: 28px 24px 50px;
#     }

#     .topbar {
#         display: flex;
#         justify-content: space-between;
#         align-items: center;
#         margin-bottom: 30px;
#     }

#     .brand {
#         display: flex;
#         align-items: center;
#         gap: 12px;
#     }

#     .brand-icon {
#         width: 44px;
#         height: 44px;
#         flex: 0 0 44px;
#         border-radius: 13px;
#         background: #111827;
#         color: white;
#         display: flex;
#         align-items: center;
#         justify-content: center;
#         font-size: 21px;
#         font-weight: 800;
#     }

#     .brand-title {
#         font-size: 20px;
#         font-weight: 800;
#         color: #111827;
#     }

#     .brand-subtitle {
#         font-size: 10px;
#         letter-spacing: 1.2px;
#         color: #9ca3af;
#         margin-top: 2px;
#     }

#     .hero {
#         background: #111827;
#         border-radius: 24px;
#         padding: 38px;
#         margin-bottom: 32px;
#     }

#     .hero-label {
#         color: #9ca3af;
#         font-size: 11px;
#         letter-spacing: 1.5px;
#         font-weight: 700;
#     }

#     .hero-title {
#         color: white;
#         font-size: 36px;
#         font-weight: 800;
#         margin-top: 10px;
#     }

#     .hero-text {
#         color: #d1d5db;
#         max-width: 650px;
#         line-height: 1.7;
#         font-size: 14px;
#         margin-top: 12px;
#     }

#     .card {
#         width: 100%;
#         min-width: 0;
#         box-sizing: border-box;
#         overflow-wrap: anywhere;
#         padding: 25px;
#         border-radius: 20px;
#         border: 1px solid #e5e7eb;
#         background: white;
#         margin-bottom: 20px;
#     }

#     .driver-name {
#         font-size: 23px;
#         font-weight: 800;
#         color: #111827;
#     }

#     .driver-phone {
#         color: #6b7280;
#         font-size: 13px;
#         margin-top: 4px;
#     }

#     .location-number {
#         font-size: 22px;
#         font-weight: 800;
#         color: #111827;
#         overflow-wrap: anywhere;
#     }

#     .location-label {
#         font-size: 10px;
#         color: #9ca3af;
#         letter-spacing: 1px;
#         font-weight: 700;
#         margin-bottom: 6px;
#     }

#     .footer {
#         margin-top: 45px;
#         padding-top: 20px;
#         border-top: 1px solid #e5e7eb;
#         color: #9ca3af;
#         font-size: 12px;
#         display: flex;
#         justify-content: space-between;
#         gap: 20px;
#     }

#     @media (max-width: 700px) {
#         .block-container {
#             padding-left: 16px;
#             padding-right: 16px;
#         }

#         .topbar, .footer {
#             align-items: flex-start;
#             flex-direction: column;
#         }

#         .hero {
#             padding: 30px;
#         }

#         .hero-title {
#             font-size: 31px;
#         }
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )


# st.markdown(
#     """
#     <div class="topbar">
#         <div class="brand">
#             <div class="brand-icon">G</div>
#             <div>
#                 <div class="brand-title">Guardrive</div>
#                 <div class="brand-subtitle">FAMILY ACCESS</div>
#             </div>
#         </div>
#     </div>

#     <div class="hero">
#         <div class="hero-label">FAMILY ACCESS</div>
#         <div class="hero-title">
#             Stay connected with your family.
#         </div>
#         <div class="hero-text">
#             Enter the driver's registered phone number.
#             Location is only available after the driver
#             explicitly approves access.
#         </div>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )


# st.markdown(
#     """
#     <div class="card">
#         <div style="
#             font-size:18px;
#             font-weight:800;
#             color:#111827;
#             margin-bottom:16px;
#         ">
#             Family member details
#         </div>
#     """,
#     unsafe_allow_html=True,
# )

# family_col1, family_col2 = st.columns(2)

# with family_col1:
#     requester_name = st.text_input(
#         "Your name",
#         placeholder="Enter your name",
#         key="requester_name",
#     )

# with family_col2:
#     requester_phone = st.text_input(
#         "Your phone number",
#         placeholder="Enter your phone number",
#         key="requester_phone",
#     )

# driver_phone = st.text_input(
#     "Driver phone number",
#     placeholder="Enter driver's registered phone number",
#     key="driver_phone_search",
# )

# st.markdown("</div>", unsafe_allow_html=True)


# search_col1, search_col2 = st.columns(2)

# with search_col1:
#     search_driver = st.button(
#         "Find Driver",
#         use_container_width=True,
#         type="primary",
#     )

# with search_col2:
#     if st.button(
#         "← Back to Guardrive",
#         use_container_width=True,
#     ):
#         st.switch_page("app.py")


# if search_driver:
#     clean_driver_phone = driver_phone.strip()

#     if not clean_driver_phone:
#         st.error("Please enter the driver's phone number.")
#     else:
#         driver = database.get_driver_by_phone(clean_driver_phone)

#         if driver:
#             st.session_state.family_driver_id = driver["id"]
#         else:
#             st.session_state.family_driver_id = None
#             st.error(
#                 "No active Guardrive driver found with this phone number."
#             )


# driver_id = st.session_state.family_driver_id

# if driver_id:
#     driver = database.get_driver_by_id(driver_id)

#     if not driver:
#         st.session_state.family_driver_id = None
#         st.error("Driver profile no longer exists.")
#         st.rerun()

#     database.expire_old_access()

#     st.markdown(
#         f"""
#         <div class="card">
#             <div class="driver-name">{driver["name"]}</div>
#             <div class="driver-phone">
#                 Driver phone · {driver["phone"]}
#             </div>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )

#     clean_requester_phone = requester_phone.strip()

#     access_ok, access = database.check_location_access(
#         driver_id=driver_id,
#         requester_phone=clean_requester_phone,
#     )

#     if access_ok and access:
#         st.success("Location access is active.")

#         latest = database.get_latest_location(driver_id)

#         if latest:
#             col1, col2, col3 = st.columns(3)

#             with col1:
#                 st.markdown(
#                     f"""
#                     <div class="card">
#                         <div class="location-label">LATITUDE</div>
#                         <div class="location-number">
#                             {latest["latitude"]:.6f}
#                         </div>
#                     </div>
#                     """,
#                     unsafe_allow_html=True,
#                 )

#             with col2:
#                 st.markdown(
#                     f"""
#                     <div class="card">
#                         <div class="location-label">LONGITUDE</div>
#                         <div class="location-number">
#                             {latest["longitude"]:.6f}
#                         </div>
#                     </div>
#                     """,
#                     unsafe_allow_html=True,
#                 )

#             with col3:
#                 speed = float(latest["speed"] or 0)
#                 status = "MOVING" if speed > 2 else "STATIONARY"

#                 st.markdown(
#                     f"""
#                     <div class="card">
#                         <div class="location-label">DRIVER STATUS</div>
#                         <div class="location-number">{status}</div>
#                     </div>
#                     """,
#                     unsafe_allow_html=True,
#                 )

#             recorded_at = latest["recorded_at"]

#             try:
#                 recorded_dt = datetime.fromisoformat(recorded_at)
#                 if recorded_dt.tzinfo is None:
#                     recorded_dt = recorded_dt.replace(
#                         tzinfo=timezone.utc
#                     )

#                 display_time = recorded_dt.astimezone().strftime(
#                     "%d %b %Y, %I:%M:%S %p"
#                 )
#             except (TypeError, ValueError):
#                 display_time = recorded_at

#             st.markdown(
#                 f"""
#                 <div class="card">
#                     <div style="
#                         font-size:17px;
#                         font-weight:800;
#                         color:#111827;
#                     ">
#                         Latest recorded location
#                     </div>

#                     <div style="
#                         color:#6b7280;
#                         font-size:13px;
#                         margin-top:7px;
#                     ">
#                         Last GPS record:
#                         <strong>{display_time}</strong>
#                     </div>
#                 </div>
#                 """,
#                 unsafe_allow_html=True,
#             )

#             maps_url = (
#                 "https://www.google.com/maps/search/?api=1"
#                 f"&query={latest['latitude']},{latest['longitude']}"
#             )

#             st.link_button(
#                 "Open Current Recorded Location",
#                 maps_url,
#                 use_container_width=True,
#             )

#             st_autorefresh(
#                 interval=5000,
#                 key="family_location_refresh",
#             )
#         else:
#             st.warning(
#                 "Access is active, but the driver has not recorded "
#                 "a GPS location yet."
#             )

#     else:
#         st.warning("You do not currently have location access.")

#         st.markdown(
#             """
#             <div class="card">
#                 <div style="
#                     font-size:17px;
#                     font-weight:800;
#                     color:#111827;
#                 ">
#                     Request Location Access
#                 </div>

#                 <div style="
#                     color:#6b7280;
#                     font-size:13px;
#                     line-height:1.6;
#                     margin-top:7px;
#                 ">
#                     The driver must approve your request before
#                     you can view their location.
#                 </div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

#         duration = st.selectbox(
#             "Access duration",
#             options=[
#                 "One time",
#                 "24 hours",
#                 "7 days",
#                 "Until I revoke",
#             ],
#             key="access_duration",
#         )

#         duration_map = {
#             "One time": "ONE_TIME",
#             "24 hours": "24_HOURS",
#             "7 days": "7_DAYS",
#             "Until I revoke": "UNTIL_REVOKED",
#         }

#         requester_name_clean = requester_name.strip()
#         requester_phone_clean = requester_phone.strip()

#         existing_requests = database.get_driver_requests(driver_id)

#         matching_request = None

#         for request in existing_requests:
#             if request["requester_phone"] == requester_phone_clean:
#                 matching_request = request
#                 break

#         if matching_request:
#             status = matching_request["status"]

#             if status == "PENDING":
#                 st.info(
#                     "Your access request is waiting for driver approval."
#                 )

#             elif status in {"DENIED", "REVOKED", "EXPIRED"}:
#                 if st.button(
#                     "Request Access Again",
#                     use_container_width=True,
#                     type="primary",
#                 ):
#                     if not requester_name_clean:
#                         st.error("Please enter your name.")
#                     elif not requester_phone_clean:
#                         st.error("Please enter your phone number.")
#                     else:
#                         database.create_access_request(
#                             driver_id=driver_id,
#                             requester_name=requester_name_clean,
#                             requester_phone=requester_phone_clean,
#                             duration=duration_map[duration],
#                         )
#                         st.success(
#                             "New access request sent to the driver."
#                         )
#                         st.rerun()

#             elif status == "ACTIVE":
#                 st.info(
#                     "An active request already exists for this phone number."
#                 )

#         else:
#             if st.button(
#                 "Request Location Access",
#                 use_container_width=True,
#                 type="primary",
#             ):
#                 if not requester_name_clean:
#                     st.error("Please enter your name.")
#                 elif not requester_phone_clean:
#                     st.error("Please enter your phone number.")
#                 else:
#                     database.create_access_request(
#                         driver_id=driver_id,
#                         requester_name=requester_name_clean,
#                         requester_phone=requester_phone_clean,
#                         duration=duration_map[duration],
#                     )
#                     st.success(
#                         "Access request sent to the driver."
#                     )
#                     st.rerun()


# st.markdown(
#     """
#     <div class="footer">
#         <div>Guardrive © 2026</div>
#         <div>Location is shown only after driver approval</div>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )






import streamlit as st
from datetime import datetime, timezone

from streamlit_autorefresh import st_autorefresh

import database


st.set_page_config(
    page_title="Guardrive | Family Access",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# AUTHENTICATION
# ============================================================

if not st.session_state.get("authenticated", False):
    st.switch_page("app.py")


# ============================================================
# SESSION STATE
# ============================================================

if "family_driver_id" not in st.session_state:
    st.session_state.family_driver_id = None


# ============================================================
# FAMILY AUTO REFRESH
# ============================================================

# Refresh family page every 2 seconds.
# This reads the latest GPS record from the database.
st_autorefresh(
    interval=2000,
    key="family_location_refresh",
)


# ============================================================
# GLOBAL CSS
# ============================================================

st.html(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html,
    body,
    [class*="css"] {
        font-family: "Inter", sans-serif;
    }

    #MainMenu,
    header,
    footer {
        visibility: hidden;
    }

    .block-container {
        max-width: 1000px;
        padding: 28px 24px 50px;
    }

    .topbar {
        display: flex;
        align-items: center;
        margin-bottom: 30px;
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .brand-icon {
        width: 44px;
        height: 44px;
        border-radius: 13px;
        background: #111827;
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 21px;
        font-weight: 800;
    }

    .brand-title {
        font-size: 20px;
        font-weight: 800;
        color: #111827;
    }

    .brand-subtitle {
        font-size: 10px;
        letter-spacing: 1.2px;
        color: #9ca3af;
        margin-top: 2px;
    }

    .hero {
        background: #111827;
        border-radius: 24px;
        padding: 38px;
        margin-bottom: 32px;
    }

    .hero-label {
        color: #9ca3af;
        font-size: 11px;
        letter-spacing: 1.5px;
        font-weight: 700;
    }

    .hero-title {
        color: white;
        font-size: 36px;
        font-weight: 800;
        margin-top: 10px;
    }

    .hero-text {
        color: #d1d5db;
        max-width: 650px;
        line-height: 1.7;
        font-size: 14px;
        margin-top: 12px;
    }

    .card {
        width: 100%;
        box-sizing: border-box;
        overflow-wrap: anywhere;
        padding: 25px;
        border-radius: 20px;
        border: 1px solid #e5e7eb;
        background: white;
        margin-bottom: 20px;
    }

    .section-title {
        font-size: 18px;
        font-weight: 800;
        color: #111827;
    }

    .driver-name {
        font-size: 23px;
        font-weight: 800;
        color: #111827;
    }

    .driver-phone {
        color: #6b7280;
        font-size: 13px;
        margin-top: 4px;
    }

    .location-number {
        font-size: 22px;
        font-weight: 800;
        color: #111827;
        overflow-wrap: anywhere;
    }

    .location-label {
        font-size: 10px;
        color: #9ca3af;
        letter-spacing: 1px;
        font-weight: 700;
        margin-bottom: 6px;
    }

    .live-status {
        display: inline-block;
        padding: 6px 10px;
        border-radius: 20px;
        background: #ecfdf5;
        color: #047857;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 0.5px;
    }

    .recent-status {
        display: inline-block;
        padding: 6px 10px;
        border-radius: 20px;
        background: #fffbeb;
        color: #b45309;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 0.5px;
    }

    .offline-status {
        display: inline-block;
        padding: 6px 10px;
        border-radius: 20px;
        background: #fef2f2;
        color: #b91c1c;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 0.5px;
    }

    .footer {
        margin-top: 45px;
        padding-top: 20px;
        border-top: 1px solid #e5e7eb;
        color: #9ca3af;
        font-size: 12px;
        display: flex;
        justify-content: space-between;
        gap: 20px;
    }

    @media (max-width: 700px) {

        .block-container {
            padding-left: 16px;
            padding-right: 16px;
        }

        .footer {
            align-items: flex-start;
            flex-direction: column;
        }

        .hero {
            padding: 30px;
        }

        .hero-title {
            font-size: 31px;
        }

    }

    </style>
    """
)


# ============================================================
# HEADER
# ============================================================

st.html(
    """
    <div class="topbar">

        <div class="brand">

            <div class="brand-icon">
                G
            </div>

            <div>

                <div class="brand-title">
                    Guardrive
                </div>

                <div class="brand-subtitle">
                    FAMILY ACCESS
                </div>

            </div>

        </div>

    </div>

    <div class="hero">

        <div class="hero-label">
            FAMILY ACCESS
        </div>

        <div class="hero-title">
            Stay connected with your family.
        </div>

        <div class="hero-text">
            Enter the driver's registered phone number.
            Location is only available after the driver
            explicitly approves access.
        </div>

    </div>
    """
)


# ============================================================
# FAMILY DETAILS
# ============================================================

st.html(
    """
    <div class="card">

        <div class="section-title">
            Family member details
        </div>

    </div>
    """
)


family_col1, family_col2 = st.columns(2)


with family_col1:

    requester_name = st.text_input(
        "Your name",
        placeholder="Enter your name",
        key="requester_name",
    )


with family_col2:

    requester_phone = st.text_input(
        "Your phone number",
        placeholder="Enter your phone number",
        key="requester_phone",
    )


driver_phone = st.text_input(
    "Driver phone number",
    placeholder="Enter driver's registered phone number",
    key="driver_phone_search",
)


# ============================================================
# BUTTONS
# ============================================================

search_col1, search_col2 = st.columns(2)


with search_col1:

    search_driver = st.button(
        "Find Driver",
        use_container_width=True,
        type="primary",
    )


with search_col2:

    if st.button(
        "← Back to Guardrive",
        use_container_width=True,
    ):

        st.switch_page("app.py")


# ============================================================
# FIND DRIVER
# ============================================================

if search_driver:

    clean_driver_phone = driver_phone.strip()

    if not clean_driver_phone:

        st.error(
            "Please enter the driver's phone number."
        )

    else:

        driver = database.get_driver_by_phone(
            clean_driver_phone
        )

        if driver:

            st.session_state.family_driver_id = driver["id"]

        else:

            st.session_state.family_driver_id = None

            st.error(
                "No active Guardrive driver found with this phone number."
            )


# ============================================================
# DRIVER
# ============================================================

driver_id = st.session_state.family_driver_id


if driver_id:

    driver = database.get_driver_by_id(
        driver_id
    )

    if not driver:

        st.session_state.family_driver_id = None

        st.error(
            "Driver profile no longer exists."
        )

        st.stop()


    # ========================================================
    # EXPIRE OLD ACCESS
    # ========================================================

    database.expire_old_access()


    # ========================================================
    # DRIVER CARD
    # ========================================================

    st.html(
        f"""
        <div class="card">

            <div class="driver-name">
                {driver["name"]}
            </div>

            <div class="driver-phone">
                Driver phone · {driver["phone"]}
            </div>

        </div>
        """
    )


    # ========================================================
    # ACCESS CHECK
    # ========================================================

    clean_requester_phone = requester_phone.strip()

    access_ok, access = database.check_location_access(
        driver_id=driver_id,
        requester_phone=clean_requester_phone,
    )


    # ========================================================
    # LOCATION ACCESS ACTIVE
    # ========================================================

    if access_ok and access:

        st.success(
            "Location access is active."
        )


        latest = database.get_latest_location(
            driver_id
        )


        if latest:

            # =================================================
            # GPS AGE
            # =================================================

            recorded_at = latest["recorded_at"]

            try:

                recorded_dt = datetime.fromisoformat(
                    recorded_at
                )

                if recorded_dt.tzinfo is None:

                    recorded_dt = recorded_dt.replace(
                        tzinfo=timezone.utc
                    )

                now_utc = datetime.now(timezone.utc)

                age_seconds = (
                    now_utc - recorded_dt
                ).total_seconds()

                if age_seconds < 0:
                    age_seconds = 0

                display_time = recorded_dt.astimezone().strftime(
                    "%d %b %Y, %I:%M:%S %p"
                )

            except (TypeError, ValueError):

                age_seconds = 999999

                display_time = recorded_at


            # =================================================
            # LOCATION STATUS
            # =================================================

            if age_seconds <= 10:

                location_status = (
                    '<span class="live-status">● LIVE</span>'
                )

            elif age_seconds <= 30:

                location_status = (
                    '<span class="recent-status">● RECENT</span>'
                )

            else:

                location_status = (
                    '<span class="offline-status">'
                    '● LAST RECORDED'
                    '</span>'
                )


            # =================================================
            # LOCATION HEADER
            # =================================================

            st.html(
                f"""
                <div class="card">

                    <div style="
                        display:flex;
                        justify-content:space-between;
                        align-items:center;
                        gap:15px;
                        flex-wrap:wrap;
                    ">

                        <div>

                            <div style="
                                font-size:17px;
                                font-weight:800;
                                color:#111827;
                            ">
                                Driver Location
                            </div>

                            <div style="
                                color:#6b7280;
                                font-size:13px;
                                margin-top:6px;
                            ">
                                GPS record received
                                {int(age_seconds)}
                                seconds ago
                            </div>

                        </div>

                        <div>
                            {location_status}
                        </div>

                    </div>

                </div>
                """
            )


            # =================================================
            # LOCATION VALUES
            # =================================================

            col1, col2, col3 = st.columns(3)


            with col1:

                st.html(
                    f"""
                    <div class="card">

                        <div class="location-label">
                            LATITUDE
                        </div>

                        <div class="location-number">
                            {latest["latitude"]:.6f}
                        </div>

                    </div>
                    """
                )


            with col2:

                st.html(
                    f"""
                    <div class="card">

                        <div class="location-label">
                            LONGITUDE
                        </div>

                        <div class="location-number">
                            {latest["longitude"]:.6f}
                        </div>

                    </div>
                    """
                )


            with col3:

                speed = float(
                    latest["speed"] or 0
                )

                status = (
                    "MOVING"
                    if speed > 2
                    else "STATIONARY"
                )


                st.html(
                    f"""
                    <div class="card">

                        <div class="location-label">
                            DRIVER STATUS
                        </div>

                        <div class="location-number">
                            {status}
                        </div>

                    </div>
                    """
                )


            # =================================================
            # LAST GPS TIME
            # =================================================

            st.html(
                f"""
                <div class="card">

                    <div style="
                        font-size:17px;
                        font-weight:800;
                        color:#111827;
                    ">
                        Latest recorded location
                    </div>

                    <div style="
                        color:#6b7280;
                        font-size:13px;
                        margin-top:7px;
                    ">
                        Last GPS record:
                        <strong>{display_time}</strong>
                    </div>

                </div>
                """
            )


            # =================================================
            # GOOGLE MAPS
            # =================================================

            maps_url = (
                "https://www.google.com/maps/search/?api=1"
                f"&query={latest['latitude']},{latest['longitude']}"
            )


            st.link_button(
                "Open Recorded Location",
                maps_url,
                use_container_width=True,
            )


        else:

            st.warning(
                "Access is active, but the driver has not recorded "
                "a GPS location yet."
            )


    # ========================================================
    # NO LOCATION ACCESS
    # ========================================================

    else:

        st.warning(
            "You do not currently have location access."
        )


        st.html(
            """
            <div class="card">

                <div class="section-title">
                    Request Location Access
                </div>

                <div style="
                    color:#6b7280;
                    font-size:13px;
                    line-height:1.6;
                    margin-top:7px;
                ">
                    The driver must approve your request before
                    you can view their location.
                </div>

            </div>
            """
        )


        duration = st.selectbox(
            "Access duration",
            options=[
                "One time",
                "24 hours",
                "7 days",
                "Until I revoke",
            ],
            key="access_duration",
        )


        duration_map = {
            "One time": "ONE_TIME",
            "24 hours": "24_HOURS",
            "7 days": "7_DAYS",
            "Until I revoke": "UNTIL_REVOKED",
        }


        requester_name_clean = requester_name.strip()

        requester_phone_clean = requester_phone.strip()


        existing_requests = database.get_driver_requests(
            driver_id
        )


        matching_request = None


        for request in existing_requests:

            if (
                request["requester_phone"]
                == requester_phone_clean
            ):

                matching_request = request

                break


        # ====================================================
        # EXISTING REQUEST
        # ====================================================

        if matching_request:

            status = matching_request["status"]


            if status == "PENDING":

                st.info(
                    "Your access request is waiting for driver approval."
                )


            elif status in {
                "DENIED",
                "REVOKED",
                "EXPIRED",
            }:

                if st.button(
                    "Request Access Again",
                    use_container_width=True,
                    type="primary",
                ):

                    if not requester_name_clean:

                        st.error(
                            "Please enter your name."
                        )

                    elif not requester_phone_clean:

                        st.error(
                            "Please enter your phone number."
                        )

                    else:

                        database.create_access_request(
                            driver_id=driver_id,
                            requester_name=requester_name_clean,
                            requester_phone=requester_phone_clean,
                            duration=duration_map[duration],
                        )

                        st.success(
                            "New access request sent to the driver."
                        )

                        st.rerun()


            elif status == "ACTIVE":

                st.info(
                    "An active request already exists for this phone number."
                )


        # ====================================================
        # NEW REQUEST
        # ====================================================

        else:

            if st.button(
                "Request Location Access",
                use_container_width=True,
                type="primary",
            ):

                if not requester_name_clean:

                    st.error(
                        "Please enter your name."
                    )

                elif not requester_phone_clean:

                    st.error(
                        "Please enter your phone number."
                    )

                else:

                    database.create_access_request(
                        driver_id=driver_id,
                        requester_name=requester_name_clean,
                        requester_phone=requester_phone_clean,
                        duration=duration_map[duration],
                    )

                    st.success(
                        "Access request sent to the driver."
                    )

                    st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <div class="footer">

        <div>
            Guardrive © 2026
        </div>

        <div>
            Location is shown only after driver approval
        </div>

    </div>
    """
)

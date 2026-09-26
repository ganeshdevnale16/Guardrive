# # # import json
# # # import os
# # # from datetime import datetime, timezone, timedelta

# # # import streamlit as st
# # # import streamlit.components.v1 as components
# # # # from streamlit_autorefresh import st_autorefresh

# # # import database


# # # st.set_page_config(
# # #     page_title="Guardrive | Driver",
# # #     page_icon="🚗",
# # #     layout="wide",
# # #     initial_sidebar_state="collapsed",
# # # )


# # # if not st.session_state.get("authenticated", False):
# # #     st.switch_page("app.py")


# # # if "driver_id" not in st.session_state:
# # #     st.session_state.driver_id = None

# # # if "tracking" not in st.session_state:
# # #     st.session_state.tracking = False


# # # GPS_API_URL = os.getenv("GPS_API_URL", "http://127.0.0.1:8000").rstrip("/")


# # # st.markdown(
# # #     """
# # #     <style>
# # #     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

# # #     html, body, [class*="css"] {
# # #         font-family: "Inter", sans-serif;
# # #     }

# # #     #MainMenu, header, footer {
# # #         visibility: hidden;
# # #     }

# # #     .block-container {
# # #         max-width: 1200px;
# # #         padding: 28px 24px 50px;
# # #     }

# # #     .topbar {
# # #         display: flex;
# # #         justify-content: space-between;
# # #         align-items: center;
# # #         gap: 20px;
# # #         margin-bottom: 30px;
# # #     }

# # #     .brand {
# # #         display: flex;
# # #         align-items: center;
# # #         gap: 12px;
# # #     }

# # #     .brand-icon {
# # #         width: 44px;
# # #         height: 44px;
# # #         flex: 0 0 44px;
# # #         border-radius: 13px;
# # #         background: #111827;
# # #         color: #fff;
# # #         display: flex;
# # #         align-items: center;
# # #         justify-content: center;
# # #         font-size: 21px;
# # #         font-weight: 800;
# # #     }

# # #     .brand-title {
# # #         font-size: 20px;
# # #         font-weight: 800;
# # #         color: #111827;
# # #     }

# # #     .brand-subtitle {
# # #         font-size: 10px;
# # #         letter-spacing: 1.2px;
# # #         color: #9ca3af;
# # #         margin-top: 2px;
# # #     }

# # #     .secure-pill {
# # #         color: #15803d;
# # #         font-size: 12px;
# # #         font-weight: 700;
# # #         white-space: nowrap;
# # #     }

# # #     .hero {
# # #         background: #111827;
# # #         border-radius: 24px;
# # #         padding: 38px;
# # #         margin-bottom: 32px;
# # #     }

# # #     .hero-label {
# # #         color: #9ca3af;
# # #         font-size: 11px;
# # #         letter-spacing: 1.5px;
# # #         font-weight: 700;
# # #     }

# # #     .hero-title {
# # #         color: #fff;
# # #         font-size: 38px;
# # #         font-weight: 800;
# # #         margin-top: 10px;
# # #     }

# # #     .hero-text {
# # #         color: #d1d5db;
# # #         max-width: 680px;
# # #         line-height: 1.7;
# # #         font-size: 14px;
# # #         margin-top: 12px;
# # #     }

# # #     .info-card, .location-card {
# # #         width: 100%;
# # #         min-width: 0;
# # #         box-sizing: border-box;
# # #         overflow-wrap: anywhere;
# # #         border: 1px solid #e5e7eb;
# # #         border-radius: 18px;
# # #         background: #fff;
# # #     }

# # #     .info-card {
# # #         padding: 20px;
# # #         min-height: 105px;
# # #     }

# # #     .metric-label, .location-label {
# # #         color: #9ca3af;
# # #         font-size: 10px;
# # #         font-weight: 700;
# # #         letter-spacing: 1.3px;
# # #     }

# # #     .metric-value {
# # #         color: #111827;
# # #         font-size: 20px;
# # #         font-weight: 800;
# # #         margin-top: 6px;
# # #         overflow-wrap: anywhere;
# # #     }

# # #     .metric-small {
# # #         color: #6b7280;
# # #         font-size: 12px;
# # #         margin-top: 3px;
# # #         overflow-wrap: anywhere;
# # #     }

# # #     .section-title {
# # #         font-size: 22px;
# # #         font-weight: 800;
# # #         color: #111827;
# # #         margin-top: 35px;
# # #         margin-bottom: 5px;
# # #     }

# # #     .section-subtitle {
# # #         color: #6b7280;
# # #         font-size: 13px;
# # #         margin-bottom: 18px;
# # #     }

# # #     .location-card {
# # #         padding: 25px;
# # #     }

# # #     .location-value {
# # #         font-size: 25px;
# # #         font-weight: 800;
# # #         color: #111827;
# # #         overflow-wrap: anywhere;
# # #     }

# # #     .status-active {
# # #         color: #15803d;
# # #         font-weight: 800;
# # #     }

# # #     .status-stopped {
# # #         color: #6b7280;
# # #         font-weight: 800;
# # #     }

# # #     .gps-box {
# # #         margin-top: 18px;
# # #         padding: 15px 18px;
# # #         border-radius: 14px;
# # #         background: #f0fdf4;
# # #         border: 1px solid #bbf7d0;
# # #         color: #166534;
# # #         font-size: 13px;
# # #         font-weight: 600;
# # #     }

# # #     .footer {
# # #         margin-top: 45px;
# # #         padding-top: 20px;
# # #         border-top: 1px solid #e5e7eb;
# # #         color: #9ca3af;
# # #         font-size: 12px;
# # #         display: flex;
# # #         justify-content: space-between;
# # #         gap: 20px;
# # #     }

# # #     @media (max-width: 700px) {
# # #         .block-container {
# # #             padding-left: 16px;
# # #             padding-right: 16px;
# # #         }

# # #         .topbar, .footer {
# # #             align-items: flex-start;
# # #             flex-direction: column;
# # #         }

# # #         .hero {
# # #             padding: 30px;
# # #         }

# # #         .hero-title {
# # #             font-size: 32px;
# # #         }
# # #     }
# # #     </style>
# # #     """,
# # #     unsafe_allow_html=True,
# # # )


# # # st.markdown(
# # #     """
# # #     <div class="topbar">
# # #         <div class="brand">
# # #             <div class="brand-icon">G</div>
# # #             <div>
# # #                 <div class="brand-title">Guardrive</div>
# # #                 <div class="brand-subtitle">
# # #                     DRIVER LOCATION PROTECTION
# # #                 </div>
# # #             </div>
# # #         </div>

# # #         <div class="secure-pill">● Secure Session</div>
# # #     </div>

# # #     <div class="hero">
# # #         <div class="hero-label">DRIVER PORTAL</div>
# # #         <div class="hero-title">Your location. Your control.</div>
# # #         <div class="hero-text">
# # #             Guardrive records your GPS location while protection
# # #             is active. Family members can only access your
# # #             location after you approve their request.
# # #         </div>
# # #     </div>
# # #     """,
# # #     unsafe_allow_html=True,
# # # )


# # # # if st.session_state.driver_id is None:
# # # #     st.markdown(
# # # #         '<div class="section-title">Driver Registration</div>',
# # # #         unsafe_allow_html=True,
# # # #     )
# # # #     st.markdown(
# # # #         '<div class="section-subtitle">'
# # # #         'Create or access your Guardrive driver profile.'
# # # #         '</div>',
# # # #         unsafe_allow_html=True,
# # # #     )

# # # #     col1, col2 = st.columns(2)

# # # #     with col1:
# # # #         driver_name = st.text_input(
# # # #             "Driver name",
# # # #             placeholder="Enter driver name",
# # # #             key="driver_registration_name",
# # # #         )

# # # #     with col2:
# # # #         driver_phone = st.text_input(
# # # #             "Driver phone number",
# # # #             placeholder="Enter phone number",
# # # #             key="driver_registration_phone",
# # # #         )

# # # #     if st.button(
# # # #         "Continue to Driver Portal",
# # # #         use_container_width=True,
# # # #         type="primary",
# # # #     ):
# # # #         driver_name = driver_name.strip()
# # # #         driver_phone = driver_phone.strip()

# # # #         if not driver_name:
# # # #             st.error("Please enter driver name.")
# # # #         elif not driver_phone:
# # # #             st.error("Please enter driver phone number.")
# # # #         else:
# # # #             existing_driver = database.get_driver_by_phone(driver_phone)

# # # #             if existing_driver:
# # # #                 st.session_state.driver_id = existing_driver["id"]
# # # #                 st.session_state.driver_name = existing_driver["name"]
# # # #                 st.session_state.driver_phone = existing_driver["phone"]
# # # #             else:
# # # #                 driver_id = database.create_driver(
# # # #                     name=driver_name,
# # # #                     phone=driver_phone,
# # # #                 )

# # # #                 if driver_id is None:
# # # #                     st.error(
# # # #                         "A driver with this phone number already exists. "
# # # #                         "Try the same number with the registered name."
# # # #                     )
# # # #                     st.stop()

# # # #                 st.session_state.driver_id = driver_id
# # # #                 st.session_state.driver_name = driver_name
# # # #                 st.session_state.driver_phone = driver_phone

# # # #             st.rerun()

# # # #     if st.button("← Back to Guardrive", use_container_width=True):
# # # #         st.switch_page("app.py")

# # # #     st.stop()
# # # if st.session_state.tracking:
# # #     st.markdown(
# # #         """
# # #         <div class="gps-box">
# # #             ● GPS protection is active. Keep this browser page open
# # #             and allow location permission.
# # #         </div>
# # #         """,
# # #         unsafe_allow_html=True,
# # #     )

# # #     gps_api_json = json.dumps(GPS_API_URL)
# # #     driver_id = int(st.session_state.driver_id)

# # #     gps_html = f"""
# # #     <!doctype html>
# # #     <html>
# # #     <head>
# # #         <meta name="viewport" content="width=device-width, initial-scale=1">
# # #         <style>
# # #             html, body {{
# # #                 margin: 0;
# # #                 padding: 0;
# # #                 background: transparent;
# # #                 font-family: Arial, sans-serif;
# # #             }}

# # #             #status {{
# # #                 padding: 14px;
# # #                 border-radius: 12px;
# # #                 background: #f8fafc;
# # #                 border: 1px solid #e5e7eb;
# # #                 color: #475569;
# # #                 font-size: 13px;
# # #                 line-height: 1.45;
# # #             }}
# # #         </style>
# # #     </head>

# # #     <body>

# # #         <div id="status">
# # #             Starting continuous GPS tracking...
# # #         </div>

# # #         <script>
# # #             const DRIVER_ID = {driver_id};
# # #             const GPS_API = {gps_api_json};

# # #             const statusBox = document.getElementById("status");

# # #             let gpsTimer = null;
# # #             let sending = false;

# # #             function setStatus(message) {{
# # #                 statusBox.textContent = message;
# # #             }}

# # #             async function getBatteryLevel() {{
# # #                 try {{
# # #                     if (!navigator.getBattery) {{
# # #                         return null;
# # #                     }}

# # #                     const battery = await navigator.getBattery();

# # #                     return Math.round(
# # #                         battery.level * 100
# # #                     );

# # #                 }} catch (error) {{
# # #                     return null;
# # #                 }}
# # #             }}

# # #             async function sendCurrentLocation(position) {{

# # #                 if (sending) {{
# # #                     return;
# # #                 }}

# # #                 sending = true;

# # #                 const coords = position.coords;

# # #                 const battery = await getBatteryLevel();

# # #                 const payload = {{
# # #                     driver_id: DRIVER_ID,

# # #                     latitude: coords.latitude,

# # #                     longitude: coords.longitude,

# # #                     accuracy: coords.accuracy,

# # #                     speed: coords.speed,

# # #                     heading: coords.heading,

# # #                     battery: battery,

# # #                     browser_timestamp: position.timestamp
# # #                 }};

# # #                 setStatus(
# # #                     "● GPS detected · Sending location..."
# # #                 );

# # #                 try {{

# # #                     const response = await fetch(
# # #                         GPS_API + "/gps/update",
# # #                         {{
# # #                             method: "POST",

# # #                             headers: {{
# # #                                 "Content-Type": "application/json"
# # #                             }},

# # #                             body: JSON.stringify(payload)
# # #                         }}
# # #                     );

# # #                     if (!response.ok) {{

# # #                         const detail =
# # #                             await response.text();

# # #                         throw new Error(
# # #                             detail || "GPS API error"
# # #                         );
# # #                     }}

# # #                     const result =
# # #                         await response.json();

# # #                     const now =
# # #                         new Date().toLocaleTimeString();

# # #                     setStatus(
# # #                         "● GPS ACTIVE · Last sent at " + now
# # #                     );

# # #                     console.log(
# # #                         "Guardrive GPS sent:",
# # #                         result
# # #                     );

# # #                 }} catch (error) {{

# # #                     console.error(
# # #                         "GPS API error:",
# # #                         error
# # #                     );

# # #                     setStatus(
# # #                         "⚠ GPS detected, but location "
# # #                         + "could not be sent to Guardrive."
# # #                     );

# # #                 }} finally {{

# # #                     sending = false;

# # #                 }}
# # #             }}

# # #             function gpsError(error) {{

# # #                 if (error.code === 1) {{

# # #                     setStatus(
# # #                         "⚠ Location permission denied. "
# # #                         + "Allow location access for this site."
# # #                     );

# # #                 }} else if (error.code === 2) {{

# # #                     setStatus(
# # #                         "⚠ Location unavailable. "
# # #                         + "Check GPS/location services."
# # #                     );

# # #                 }} else if (error.code === 3) {{

# # #                     setStatus(
# # #                         "⚠ GPS request timed out. "
# # #                         + "Retrying..."
# # #                     );

# # #                 }} else {{

# # #                     setStatus(
# # #                         "⚠ Unable to read GPS location."
# # #                     );
# # #                 }}
# # #             }}

# # #             function requestGPS() {{

# # #                 if (!navigator.geolocation) {{

# # #                     setStatus(
# # #                         "This browser does not support GPS."
# # #                     );

# # #                     return;
# # #                 }}

# # #                 navigator.geolocation.getCurrentPosition(
# # #                     sendCurrentLocation,
# # #                     gpsError,
# # #                     {{
# # #                         enableHighAccuracy: true,

# # #                         maximumAge: 0,

# # #                         timeout: 15000
# # #                     }}
# # #                 );
# # #             }}

# # #             function startTracking() {{

# # #                 if (!window.isSecureContext) {{

# # #                     setStatus(
# # #                         "GPS requires HTTPS when deployed. "
# # #                         + "localhost is allowed for local development."
# # #                     );

# # #                     return;
# # #                 }}

# # #                 setStatus(
# # #                     "Requesting GPS permission..."
# # #                 );

# # #                 // Send immediately
# # #                 requestGPS();

# # #                 // Then send every 3 seconds
# # #                 gpsTimer = setInterval(
# # #                     requestGPS,
# # #                     3000
# # #                 );
# # #             }}

# # #             startTracking();

# # #         </script>

# # #     </body>
# # #     </html>
# # #     """

# # #     components.html(
# # #         gps_html,
# # #         height=95,
# # #         scrolling=False,
# # #     )

# # # driver = database.get_driver_by_id(st.session_state.driver_id)

# # # if not driver:
# # #     st.session_state.driver_id = None
# # #     st.session_state.tracking = False
# # #     st.error("Driver profile could not be found.")
# # #     st.rerun()


# # # database.expire_old_access()

# # # col1, col2, col3 = st.columns(3)

# # # with col1:
# # #     st.markdown(
# # #         f"""
# # #         <div class="info-card">
# # #             <div class="metric-label">DRIVER</div>
# # #             <div class="metric-value">{driver["name"]}</div>
# # #             <div class="metric-small">{driver["phone"]}</div>
# # #         </div>
# # #         """,
# # #         unsafe_allow_html=True,
# # #     )

# # # with col2:
# # #     status = "ACTIVE" if st.session_state.tracking else "STOPPED"
# # #     status_class = (
# # #         "status-active"
# # #         if st.session_state.tracking
# # #         else "status-stopped"
# # #     )

# # #     st.markdown(
# # #         f"""
# # #         <div class="info-card">
# # #             <div class="metric-label">LOCATION PROTECTION</div>
# # #             <div class="metric-value {status_class}">{status}</div>
# # #             <div class="metric-small">GPS recording status</div>
# # #         </div>
# # #         """,
# # #         unsafe_allow_html=True,
# # #     )

# # # with col3:
# # #     latest = database.get_latest_location(st.session_state.driver_id)
# # #     latest_text = "Location available" if latest else "No location recorded"

# # #     st.markdown(
# # #         f"""
# # #         <div class="info-card">
# # #             <div class="metric-label">LAST GPS RECORD</div>
# # #             <div class="metric-value">{latest_text}</div>
# # #             <div class="metric-small">Verified database record</div>
# # #         </div>
# # #         """,
# # #         unsafe_allow_html=True,
# # #     )


# # # st.markdown(
# # #     '<div class="section-title">Location Protection</div>',
# # #     unsafe_allow_html=True,
# # # )
# # # st.markdown(
# # #     '<div class="section-subtitle">'
# # #     'Start or stop GPS location recording from this device.'
# # #     '</div>',
# # #     unsafe_allow_html=True,
# # # )

# # # button_col1, button_col2 = st.columns(2)

# # # with button_col1:
# # #     if not st.session_state.tracking:
# # #         if st.button(
# # #             "▶ Start Location Protection",
# # #             use_container_width=True,
# # #             type="primary",
# # #         ):
# # #             st.session_state.tracking = True
# # #             st.rerun()
# # #     else:
# # #         if st.button(
# # #             "■ Stop Location Protection",
# # #             use_container_width=True,
# # #         ):
# # #             st.session_state.tracking = False
# # #             st.rerun()

# # # with button_col2:
# # #     if st.button(
# # #         "← Back to Guardrive",
# # #         use_container_width=True,
# # #     ):
# # #         st.switch_page("app.py")


# # # if st.session_state.tracking:
# # #     st.markdown(
# # #         """
# # #         <div class="gps-box">
# # #             ● GPS protection is active. Keep this browser page open
# # #             and allow location permission.
# # #         </div>
# # #         """,
# # #         unsafe_allow_html=True,
# # #     )

# # #     gps_api_json = json.dumps(GPS_API_URL)
# # #     driver_id = int(st.session_state.driver_id)

# # #     gps_html = f"""
# # #     <!doctype html>
# # #     <html>
# # #     <head>
# # #         <meta name="viewport" content="width=device-width, initial-scale=1">
# # #         <style>
# # #             html, body {{
# # #                 margin: 0;
# # #                 padding: 0;
# # #                 background: transparent;
# # #                 font-family: Arial, sans-serif;
# # #             }}
# # #             #status {{
# # #                 padding: 14px;
# # #                 border-radius: 12px;
# # #                 background: #f8fafc;
# # #                 border: 1px solid #e5e7eb;
# # #                 color: #475569;
# # #                 font-size: 13px;
# # #                 line-height: 1.45;
# # #             }}
# # #         </style>
# # #     </head>
# # #     <body>
# # #         <div id="status">Starting GPS watcher...</div>

# # #         <script>
# # #             const DRIVER_ID = {driver_id};
# # #             const GPS_API = {gps_api_json};
# # #             const statusBox = document.getElementById("status");

# # #             function setStatus(message) {{
# # #                 statusBox.textContent = message;
# # #             }}

# # #             async function getBatteryLevel() {{
# # #                 try {{
# # #                     if (!navigator.getBattery) return null;
# # #                     const battery = await navigator.getBattery();
# # #                     return Math.round(battery.level * 100);
# # #                 }} catch (e) {{
# # #                     return null;
# # #                 }}
# # #             }}

# # #             async function sendLocation(position) {{
# # #                 const coords = position.coords;
# # #                 const battery = await getBatteryLevel();

# # #                 const payload = {{
# # #                     driver_id: DRIVER_ID,
# # #                     latitude: coords.latitude,
# # #                     longitude: coords.longitude,
# # #                     accuracy: coords.accuracy,
# # #                     speed: coords.speed,
# # #                     heading: coords.heading,
# # #                     battery: battery,
# # #                     browser_timestamp: position.timestamp
# # #                 }};

# # #                 try {{
# # #                     const response = await fetch(
# # #                         GPS_API + "/gps/update",
# # #                         {{
# # #                             method: "POST",
# # #                             headers: {{
# # #                                 "Content-Type": "application/json"
# # #                             }},
# # #                             body: JSON.stringify(payload)
# # #                         }}
# # #                     );

# # #                     if (!response.ok) {{
# # #                         const detail = await response.text();
# # #                         throw new Error(detail || "GPS server error");
# # #                     }}

# # #                     setStatus(
# # #                         "● GPS active · Last coordinate sent successfully"
# # #                     );
# # #                 }} catch (error) {{
# # #                     setStatus(
# # #                         "⚠ GPS detected, but the GPS API is not reachable. "
# # #                         + "Check GPS_API_URL and the FastAPI server."
# # #                     );
# # #                 }}
# # #             }}

# # #             function gpsError(error) {{
# # #                 if (error.code === 1) {{
# # #                     setStatus("Location permission denied. Allow location access for this site.");
# # #                 }} else if (error.code === 2) {{
# # #                     setStatus("Location unavailable. Check device GPS/location services.");
# # #                 }} else if (error.code === 3) {{
# # #                     setStatus("GPS request timed out. Retrying...");
# # #                 }} else {{
# # #                     setStatus("Unable to read GPS location.");
# # #                 }}
# # #             }}

# # #             if (!window.isSecureContext) {{
# # #                 setStatus(
# # #                     "GPS requires HTTPS when deployed. localhost is allowed for local development."
# # #                 );
# # #             }} else if (!navigator.geolocation) {{
# # #                 setStatus("This browser does not support GPS.");
# # #             }} else {{
# # #                 setStatus("Requesting GPS permission...");

# # #                 navigator.geolocation.watchPosition(
# # #                     sendLocation,
# # #                     gpsError,
# # #                     {{
# # #                         enableHighAccuracy: true,
# # #                         maximumAge: 3000,
# # #                         timeout: 15000
# # #                     }}
# # #                 );
# # #             }}
# # #         </script>
# # #     </body>
# # #     </html>
# # #     """

# # #     components.html(
# # #         gps_html,
# # #         height=95,
# # #         scrolling=False,
# # #     )

# # #     # st_autorefresh(
# # #     #     interval=5000,
# # #     #     key="driver_gps_refresh",
# # #     # )


# # # st.markdown(
# # #     '<div class="section-title">Latest Recorded Location</div>',
# # #     unsafe_allow_html=True,
# # # )
# # # st.markdown(
# # #     '<div class="section-subtitle">'
# # #     'This is the latest location actually stored by Guardrive.'
# # #     '</div>',
# # #     unsafe_allow_html=True,
# # # )

# # # latest = database.get_latest_location(st.session_state.driver_id)

# # # if latest:
# # #     location_col1, location_col2, location_col3 = st.columns(3)

# # #     with location_col1:
# # #         st.markdown(
# # #             f"""
# # #             <div class="location-card">
# # #                 <div class="location-label">LATITUDE</div>
# # #                 <div class="location-value">{latest["latitude"]:.6f}</div>
# # #             </div>
# # #             """,
# # #             unsafe_allow_html=True,
# # #         )

# # #     with location_col2:
# # #         st.markdown(
# # #             f"""
# # #             <div class="location-card">
# # #                 <div class="location-label">LONGITUDE</div>
# # #                 <div class="location-value">{latest["longitude"]:.6f}</div>
# # #             </div>
# # #             """,
# # #             unsafe_allow_html=True,
# # #         )

# # #     with location_col3:
# # #         speed_value = float(latest["speed"] or 0)
# # #         st.markdown(
# # #             f"""
# # #             <div class="location-card">
# # #                 <div class="location-label">SPEED</div>
# # #                 <div class="location-value">{speed_value:.1f} km/h</div>
# # #             </div>
# # #             """,
# # #             unsafe_allow_html=True,
# # #         )

# # #     recorded_at = latest["recorded_at"]

# # #     try:
# # #         recorded_dt = datetime.fromisoformat(recorded_at)
# # #         if recorded_dt.tzinfo is None:
# # #             recorded_dt = recorded_dt.replace(tzinfo=timezone.utc)

# # #         recorded_display = recorded_dt.astimezone().strftime(
# # #             "%d %b %Y, %I:%M:%S %p"
# # #         )
# # #     except (TypeError, ValueError):
# # #         recorded_display = recorded_at

# # #     st.markdown(
# # #         f"""
# # #         <div style="
# # #             margin-top:15px;
# # #             color:#6b7280;
# # #             font-size:13px;
# # #         ">
# # #             Last recorded at <strong>{recorded_display}</strong>
# # #         </div>
# # #         """,
# # #         unsafe_allow_html=True,
# # #     )

# # #     maps_url = (
# # #         "https://www.google.com/maps/search/?api=1"
# # #         f"&query={latest['latitude']},{latest['longitude']}"
# # #     )

# # #     st.link_button(
# # #         "Open Latest Location in Google Maps",
# # #         maps_url,
# # #         use_container_width=True,
# # #     )
# # # else:
# # #     st.info(
# # #         "No GPS location has been recorded yet. "
# # #         "Start Location Protection."
# # #     )


# # # st.markdown(
# # #     '<div class="section-title">Access Requests</div>',
# # #     unsafe_allow_html=True,
# # # )
# # # st.markdown(
# # #     '<div class="section-subtitle">'
# # #     'Approve, deny or revoke family location access.'
# # #     '</div>',
# # #     unsafe_allow_html=True,
# # # )

# # # requests = database.get_driver_requests(st.session_state.driver_id)
# # # pending_requests = [
# # #     request for request in requests
# # #     if request["status"] == "PENDING"
# # # ]

# # # if not pending_requests:
# # #     st.info("No pending access requests.")
# # # else:
# # #     for request in pending_requests:
# # #         st.markdown(
# # #             f"""
# # #             <div class="location-card" style="margin-bottom:12px;">
# # #                 <div style="
# # #                     font-size:17px;
# # #                     font-weight:800;
# # #                     color:#111827;
# # #                 ">
# # #                     {request["requester_name"]}
# # #                 </div>

# # #                 <div style="
# # #                     margin-top:5px;
# # #                     color:#6b7280;
# # #                     font-size:13px;
# # #                 ">
# # #                     {request["requester_phone"]}
# # #                 </div>

# # #                 <div style="
# # #                     margin-top:8px;
# # #                     color:#6b7280;
# # #                     font-size:13px;
# # #                 ">
# # #                     Requested access: {request["duration"]}
# # #                 </div>
# # #             </div>
# # #             """,
# # #             unsafe_allow_html=True,
# # #         )

# # #         approve_col, deny_col = st.columns(2)

# # #         with approve_col:
# # #             if st.button(
# # #                 "Approve",
# # #                 key=f"approve_{request['id']}",
# # #                 use_container_width=True,
# # #                 type="primary",
# # #             ):
# # #                 duration = request["duration"]
# # #                 expires_at = None
# # #                 now = datetime.now(timezone.utc)

# # #                 if duration == "ONE_TIME":
# # #                     expires_at = (
# # #                         now + timedelta(minutes=10)
# # #                     ).isoformat()
# # #                 elif duration == "24_HOURS":
# # #                     expires_at = (
# # #                         now + timedelta(hours=24)
# # #                     ).isoformat()
# # #                 elif duration == "7_DAYS":
# # #                     expires_at = (
# # #                         now + timedelta(days=7)
# # #                     ).isoformat()

# # #                 database.update_access_request(
# # #                     request["id"],
# # #                     "ACTIVE",
# # #                     expires_at,
# # #                 )

# # #                 st.success("Access approved.")
# # #                 st.rerun()

# # #         with deny_col:
# # #             if st.button(
# # #                 "Deny",
# # #                 key=f"deny_{request['id']}",
# # #                 use_container_width=True,
# # #             ):
# # #                 database.deny_access(request["id"])
# # #                 st.warning("Access request denied.")
# # #                 st.rerun()


# # # st.markdown(
# # #     '<div class="section-title">Access History</div>',
# # #     unsafe_allow_html=True,
# # # )

# # # for request in requests:
# # #     status = request["status"]

# # #     if status == "PENDING":
# # #         continue

# # #     if status == "ACTIVE":
# # #         st.markdown(
# # #             f"""
# # #             <div class="location-card">
# # #                 <strong>{request["requester_name"]}</strong>
# # #                 <span style="color:#15803d;"> · ACTIVE</span>

# # #                 <div style="
# # #                     margin-top:5px;
# # #                     color:#6b7280;
# # #                     font-size:13px;
# # #                 ">
# # #                     {request["requester_phone"]} · {request["duration"]}
# # #                 </div>
# # #             </div>
# # #             """,
# # #             unsafe_allow_html=True,
# # #         )

# # #         if st.button(
# # #             "Revoke Access",
# # #             key=f"revoke_{request['id']}",
# # #             use_container_width=True,
# # #         ):
# # #             database.revoke_access(request["id"])
# # #             st.rerun()

# # #     elif status == "DENIED":
# # #         st.warning(f'{request["requester_name"]} · DENIED')

# # #     elif status == "REVOKED":
# # #         st.info(f'{request["requester_name"]} · REVOKED')

# # #     elif status == "EXPIRED":
# # #         st.info(f'{request["requester_name"]} · EXPIRED')


# # # st.markdown(
# # #     """
# # #     <div class="footer">
# # #         <div>Guardrive © 2026</div>
# # #         <div>Private location sharing · Prototype</div>
# # #     </div>
# # #     """,
# # #     unsafe_allow_html=True,
# # # )





# # import json
# # import os
# # from datetime import datetime, timezone, timedelta
# # from html import escape

# # import streamlit as st
# # import streamlit.components.v1 as components

# # import database


# # # ============================================================
# # # PAGE CONFIG
# # # ============================================================

# # st.set_page_config(
# #     page_title="Guardrive | Driver",
# #     page_icon="🚗",
# #     layout="wide",
# #     initial_sidebar_state="collapsed",
# # )


# # # ============================================================
# # # AUTHENTICATION
# # # ============================================================

# # if not st.session_state.get("authenticated", False):
# #     st.switch_page("app.py")


# # # ============================================================
# # # SESSION STATE
# # # ============================================================

# # if "driver_id" not in st.session_state:
# #     st.session_state.driver_id = None

# # if "tracking" not in st.session_state:
# #     st.session_state.tracking = False


# # # ============================================================
# # # CONFIG
# # # ============================================================

# # GPS_API_URL = os.getenv(
# #     "GPS_API_URL",
# #     "http://127.0.0.1:8000"
# # ).rstrip("/")

# # MVP_DRIVER_NAME = "Ganesh"
# # MVP_DRIVER_PHONE = "1111111111"


# # # ============================================================
# # # LOAD / CREATE DRIVER
# # # ============================================================

# # driver_id = st.session_state.get("driver_id")


# # # If session does not have driver ID, find driver by phone
# # if driver_id is None:

# #     driver = database.get_driver_by_phone(MVP_DRIVER_PHONE)

# #     # If driver doesn't exist, create it
# #     if not driver:

# #         new_driver_id = database.create_driver(
# #             name=MVP_DRIVER_NAME,
# #             phone=MVP_DRIVER_PHONE,
# #         )

# #         if new_driver_id:
# #             driver = database.get_driver_by_id(new_driver_id)

# #         else:
# #             # Try loading again in case it already exists
# #             driver = database.get_driver_by_phone(
# #                 MVP_DRIVER_PHONE
# #             )

# #     if not driver:
# #         st.error(
# #             f"Unable to create or load driver profile "
# #             f"for {MVP_DRIVER_PHONE}."
# #         )
# #         st.stop()

# #     driver_id = int(driver["id"])

# #     st.session_state.driver_id = driver_id
# #     st.session_state.driver_name = driver["name"]
# #     st.session_state.driver_phone = driver["phone"]


# # # ============================================================
# # # SAFELY VALIDATE DRIVER ID
# # # ============================================================

# # driver_id = st.session_state.get("driver_id")

# # if driver_id is None:

# #     st.session_state.tracking = False

# #     st.error(
# #         "Driver ID is missing. Please reload the Driver Portal."
# #     )

# #     st.stop()


# # try:
# #     driver_id = int(driver_id)

# # except (TypeError, ValueError):

# #     st.session_state.driver_id = None
# #     st.session_state.tracking = False

# #     st.error(
# #         "Invalid driver ID. Please reload the Driver Portal."
# #     )

# #     st.stop()


# # # ============================================================
# # # LOAD DRIVER
# # # ============================================================

# # driver = database.get_driver_by_id(driver_id)

# # if not driver:

# #     st.session_state.driver_id = None
# #     st.session_state.tracking = False

# #     st.error(
# #         "Driver profile could not be found."
# #     )

# #     st.stop()


# # # ============================================================
# # # CSS
# # # ============================================================

# # st.markdown(
# #     """
# #     <style>

# #     @import url(
# #         'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
# #     );

# #     html, body, [class*="css"] {
# #         font-family: "Inter", sans-serif;
# #     }

# #     #MainMenu, header, footer {
# #         visibility: hidden;
# #     }

# #     .block-container {
# #         max-width: 1200px;
# #         padding: 28px 24px 50px;
# #     }

# #     .topbar {
# #         display: flex;
# #         justify-content: space-between;
# #         align-items: center;
# #         gap: 20px;
# #         margin-bottom: 30px;
# #     }

# #     .brand {
# #         display: flex;
# #         align-items: center;
# #         gap: 12px;
# #     }

# #     .brand-icon {
# #         width: 44px;
# #         height: 44px;
# #         flex: 0 0 44px;
# #         border-radius: 13px;
# #         background: #111827;
# #         color: #fff;
# #         display: flex;
# #         align-items: center;
# #         justify-content: center;
# #         font-size: 21px;
# #         font-weight: 800;
# #     }

# #     .brand-title {
# #         font-size: 20px;
# #         font-weight: 800;
# #         color: #111827;
# #     }

# #     .brand-subtitle {
# #         font-size: 10px;
# #         letter-spacing: 1.2px;
# #         color: #9ca3af;
# #         margin-top: 2px;
# #     }

# #     .secure-pill {
# #         color: #15803d;
# #         font-size: 12px;
# #         font-weight: 700;
# #         white-space: nowrap;
# #     }

# #     .hero {
# #         background: #111827;
# #         border-radius: 24px;
# #         padding: 38px;
# #         margin-bottom: 32px;
# #     }

# #     .hero-label {
# #         color: #9ca3af;
# #         font-size: 11px;
# #         letter-spacing: 1.5px;
# #         font-weight: 700;
# #     }

# #     .hero-title {
# #         color: #fff;
# #         font-size: 38px;
# #         font-weight: 800;
# #         margin-top: 10px;
# #     }

# #     .hero-text {
# #         color: #d1d5db;
# #         max-width: 680px;
# #         line-height: 1.7;
# #         font-size: 14px;
# #         margin-top: 12px;
# #     }

# #     .info-card,
# #     .location-card {
# #         width: 100%;
# #         min-width: 0;
# #         box-sizing: border-box;
# #         overflow-wrap: anywhere;
# #         border: 1px solid #e5e7eb;
# #         border-radius: 18px;
# #         background: #fff;
# #     }

# #     .info-card {
# #         padding: 20px;
# #         min-height: 105px;
# #     }

# #     .metric-label,
# #     .location-label {
# #         color: #9ca3af;
# #         font-size: 10px;
# #         font-weight: 700;
# #         letter-spacing: 1.3px;
# #     }

# #     .metric-value {
# #         color: #111827;
# #         font-size: 20px;
# #         font-weight: 800;
# #         margin-top: 6px;
# #         overflow-wrap: anywhere;
# #     }

# #     .metric-small {
# #         color: #6b7280;
# #         font-size: 12px;
# #         margin-top: 3px;
# #         overflow-wrap: anywhere;
# #     }

# #     .section-title {
# #         font-size: 22px;
# #         font-weight: 800;
# #         color: #111827;
# #         margin-top: 35px;
# #         margin-bottom: 5px;
# #     }

# #     .section-subtitle {
# #         color: #6b7280;
# #         font-size: 13px;
# #         margin-bottom: 18px;
# #     }

# #     .location-card {
# #         padding: 25px;
# #     }

# #     .location-value {
# #         font-size: 25px;
# #         font-weight: 800;
# #         color: #111827;
# #         overflow-wrap: anywhere;
# #     }

# #     .status-active {
# #         color: #15803d;
# #         font-weight: 800;
# #     }

# #     .status-stopped {
# #         color: #6b7280;
# #         font-weight: 800;
# #     }

# #     .gps-box {
# #         margin-top: 18px;
# #         padding: 15px 18px;
# #         border-radius: 14px;
# #         background: #f0fdf4;
# #         border: 1px solid #bbf7d0;
# #         color: #166534;
# #         font-size: 13px;
# #         font-weight: 600;
# #     }

# #     .footer {
# #         margin-top: 45px;
# #         padding-top: 20px;
# #         border-top: 1px solid #e5e7eb;
# #         color: #9ca3af;
# #         font-size: 12px;
# #         display: flex;
# #         justify-content: space-between;
# #         gap: 20px;
# #     }

# #     @media (max-width: 700px) {

# #         .block-container {
# #             padding-left: 16px;
# #             padding-right: 16px;
# #         }

# #         .topbar,
# #         .footer {
# #             align-items: flex-start;
# #             flex-direction: column;
# #         }

# #         .hero {
# #             padding: 30px;
# #         }

# #         .hero-title {
# #             font-size: 32px;
# #         }

# #     }

# #     </style>
# #     """,
# #     unsafe_allow_html=True,
# # )


# # # ============================================================
# # # HEADER
# # # ============================================================

# # st.markdown(
# #     """
# #     <div class="topbar">

# #         <div class="brand">

# #             <div class="brand-icon">
# #                 G
# #             </div>

# #             <div>

# #                 <div class="brand-title">
# #                     Guardrive
# #                 </div>

# #                 <div class="brand-subtitle">
# #                     DRIVER LOCATION PROTECTION
# #                 </div>

# #             </div>

# #         </div>

# #         <div class="secure-pill">
# #             ● Secure Session
# #         </div>

# #     </div>


# #     <div class="hero">

# #         <div class="hero-label">
# #             DRIVER PORTAL
# #         </div>

# #         <div class="hero-title">
# #             Your location. Your control.
# #         </div>

# #         <div class="hero-text">

# #             Guardrive records your GPS location while
# #             protection is active. Family members can only
# #             access your location after you approve their request.

# #         </div>

# #     </div>
# #     """,
# #     unsafe_allow_html=True,
# # )


# # # ============================================================
# # # DRIVER INFORMATION
# # # ============================================================

# # database.expire_old_access()


# # col1, col2, col3 = st.columns(3)


# # with col1:

# #     st.markdown(
# #         f"""
# #         <div class="info-card">

# #             <div class="metric-label">
# #                 DRIVER
# #             </div>

# #             <div class="metric-value">
# #                 {escape(str(driver["name"]))}
# #             </div>

# #             <div class="metric-small">
# #                 {escape(str(driver["phone"]))}
# #             </div>

# #         </div>
# #         """,
# #         unsafe_allow_html=True,
# #     )


# # with col2:

# #     status = (
# #         "ACTIVE"
# #         if st.session_state.tracking
# #         else "STOPPED"
# #     )

# #     status_class = (
# #         "status-active"
# #         if st.session_state.tracking
# #         else "status-stopped"
# #     )

# #     st.markdown(
# #         f"""
# #         <div class="info-card">

# #             <div class="metric-label">
# #                 LOCATION PROTECTION
# #             </div>

# #             <div class="metric-value {status_class}">
# #                 {status}
# #             </div>

# #             <div class="metric-small">
# #                 GPS recording status
# #             </div>

# #         </div>
# #         """,
# #         unsafe_allow_html=True,
# #     )


# # with col3:

# #     latest = database.get_latest_location(driver_id)

# #     latest_text = (
# #         "Location available"
# #         if latest
# #         else "No location recorded"
# #     )

# #     st.markdown(
# #         f"""
# #         <div class="info-card">

# #             <div class="metric-label">
# #                 LAST GPS RECORD
# #             </div>

# #             <div class="metric-value">
# #                 {latest_text}
# #             </div>

# #             <div class="metric-small">
# #                 Verified database record
# #             </div>

# #         </div>
# #         """,
# #         unsafe_allow_html=True,
# #     )


# # # ============================================================
# # # LOCATION PROTECTION
# # # ============================================================

# # st.markdown(
# #     '<div class="section-title">Location Protection</div>',
# #     unsafe_allow_html=True,
# # )

# # st.markdown(
# #     """
# #     <div class="section-subtitle">
# #         Start or stop GPS location recording from this device.
# #     </div>
# #     """,
# #     unsafe_allow_html=True,
# # )


# # button_col1, button_col2 = st.columns(2)


# # with button_col1:

# #     if not st.session_state.tracking:

# #         if st.button(
# #             "▶ Start Location Protection",
# #             use_container_width=True,
# #             type="primary",
# #         ):

# #             st.session_state.tracking = True

# #             st.rerun()

# #     else:

# #         if st.button(
# #             "■ Stop Location Protection",
# #             use_container_width=True,
# #         ):

# #             st.session_state.tracking = False

# #             st.rerun()


# # with button_col2:

# #     if st.button(
# #         "← Back to Guardrive",
# #         use_container_width=True,
# #     ):

# #         st.switch_page("app.py")


# # # ============================================================
# # # CONTINUOUS GPS TRACKING
# # # ============================================================

# # if st.session_state.tracking:

# #     st.markdown(
# #         """
# #         <div class="gps-box">

# #             ● GPS protection is active.
# #             Keep this browser page open and allow
# #             location permission.

# #         </div>
# #         """,
# #         unsafe_allow_html=True,
# #     )

# #     gps_api_json = json.dumps(GPS_API_URL)

# #     gps_html = f"""
# #     <!doctype html>

# #     <html>

# #     <head>

# #         <meta
# #             name="viewport"
# #             content="width=device-width, initial-scale=1"
# #         >

# #         <style>

# #             html, body {{
# #                 margin: 0;
# #                 padding: 0;
# #                 background: transparent;
# #                 font-family: Arial, sans-serif;
# #             }}

# #             #status {{
# #                 padding: 14px;
# #                 border-radius: 12px;
# #                 background: #f8fafc;
# #                 border: 1px solid #e5e7eb;
# #                 color: #475569;
# #                 font-size: 13px;
# #                 line-height: 1.45;
# #             }}

# #         </style>

# #     </head>

# #     <body>

# #         <div id="status">
# #             Starting continuous GPS tracking...
# #         </div>


# #         <script>

# #             const DRIVER_ID = {driver_id};

# #             const GPS_API = {gps_api_json};

# #             const statusBox =
# #                 document.getElementById("status");

# #             let sending = false;


# #             function setStatus(message) {{

# #                 statusBox.textContent = message;

# #             }}


# #             async function getBatteryLevel() {{

# #                 try {{

# #                     if (!navigator.getBattery) {{

# #                         return null;

# #                     }}

# #                     const battery =
# #                         await navigator.getBattery();

# #                     return Math.round(
# #                         battery.level * 100
# #                     );

# #                 }} catch (error) {{

# #                     return null;

# #                 }}

# #             }}


# #             async function sendCurrentLocation(position) {{

# #                 if (sending) {{

# #                     return;

# #                 }}

# #                 sending = true;


# #                 const coords = position.coords;


# #                 const battery =
# #                     await getBatteryLevel();


# #                 const payload = {{

# #                     driver_id: DRIVER_ID,

# #                     latitude: coords.latitude,

# #                     longitude: coords.longitude,

# #                     accuracy: coords.accuracy,

# #                     speed: coords.speed,

# #                     heading: coords.heading,

# #                     battery: battery,

# #                     browser_timestamp: position.timestamp

# #                 }};


# #                 setStatus(
# #                     "● GPS detected · Sending location..."
# #                 );


# #                 try {{

# #                     const response =
# #                         await fetch(
# #                             GPS_API + "/gps/update",
# #                             {{
# #                                 method: "POST",

# #                                 headers: {{
# #                                     "Content-Type":
# #                                         "application/json"
# #                                 }},

# #                                 body:
# #                                     JSON.stringify(payload)
# #                             }}
# #                         );


# #                     if (!response.ok) {{

# #                         const detail =
# #                             await response.text();

# #                         throw new Error(
# #                             detail || "GPS API error"
# #                         );

# #                     }}


# #                     await response.json();


# #                     const now =
# #                         new Date().toLocaleTimeString();


# #                     setStatus(
# #                         "● GPS ACTIVE · Last sent at "
# #                         + now
# #                     );


# #                 }} catch (error) {{

# #                     console.error(
# #                         "Guardrive GPS error:",
# #                         error
# #                     );


# #                     setStatus(
# #                         "⚠ GPS detected, but location "
# #                         + "could not be sent to Guardrive."
# #                     );

# #                 }} finally {{

# #                     sending = false;

# #                 }}

# #             }}


# #             function gpsError(error) {{

# #                 if (error.code === 1) {{

# #                     setStatus(
# #                         "⚠ Location permission denied. "
# #                         + "Allow location access for this site."
# #                     );

# #                 }}

# #                 else if (error.code === 2) {{

# #                     setStatus(
# #                         "⚠ Location unavailable. "
# #                         + "Check GPS/location services."
# #                     );

# #                 }}

# #                 else if (error.code === 3) {{

# #                     setStatus(
# #                         "⚠ GPS request timed out. "
# #                         + "Retrying..."
# #                     );

# #                 }}

# #                 else {{

# #                     setStatus(
# #                         "⚠ Unable to read GPS location."
# #                     );

# #                 }}

# #             }}


# #             function requestGPS() {{

# #                 if (!navigator.geolocation) {{

# #                     setStatus(
# #                         "This browser does not support GPS."
# #                     );

# #                     return;

# #                 }}


# #                 navigator.geolocation.getCurrentPosition(
# #                     sendCurrentLocation,
# #                     gpsError,
# #                     {{
# #                         enableHighAccuracy: true,

# #                         maximumAge: 0,

# #                         timeout: 15000
# #                     }}
# #                 );

# #             }}


# #             function startTracking() {{

# #                 if (!window.isSecureContext) {{

# #                     setStatus(
# #                         "GPS requires HTTPS when deployed. "
# #                         + "localhost is allowed for local development."
# #                     );

# #                     return;

# #                 }}


# #                 setStatus(
# #                     "Requesting GPS permission..."
# #                 );


# #                 // First GPS request immediately
# #                 requestGPS();


# #                 // Then every 3 seconds
# #                 setInterval(
# #                     requestGPS,
# #                     3000
# #                 );

# #             }}


# #             startTracking();

# #         </script>

# #     </body>

# #     </html>
# #     """


# #     components.html(
# #         gps_html,
# #         height=95,
# #         scrolling=False,
# #     )


# # # ============================================================
# # # LATEST RECORDED LOCATION
# # # ============================================================

# # st.markdown(
# #     '<div class="section-title">Latest Recorded Location</div>',
# #     unsafe_allow_html=True,
# # )

# # st.markdown(
# #     """
# #     <div class="section-subtitle">
# #         This is the latest location actually stored by Guardrive.
# #     </div>
# #     """,
# #     unsafe_allow_html=True,
# # )


# # latest = database.get_latest_location(driver_id)


# # if latest:

# #     location_col1, location_col2, location_col3 = st.columns(3)


# #     with location_col1:

# #         st.markdown(
# #             f"""
# #             <div class="location-card">

# #                 <div class="location-label">
# #                     LATITUDE
# #                 </div>

# #                 <div class="location-value">
# #                     {float(latest["latitude"]):.6f}
# #                 </div>

# #             </div>
# #             """,
# #             unsafe_allow_html=True,
# #         )


# #     with location_col2:

# #         st.markdown(
# #             f"""
# #             <div class="location-card">

# #                 <div class="location-label">
# #                     LONGITUDE
# #                 </div>

# #                 <div class="location-value">
# #                     {float(latest["longitude"]):.6f}
# #                 </div>

# #             </div>
# #             """,
# #             unsafe_allow_html=True,
# #         )


# #     with location_col3:

# #         speed_value = float(
# #             latest["speed"] or 0
# #         )

# #         st.markdown(
# #             f"""
# #             <div class="location-card">

# #                 <div class="location-label">
# #                     SPEED
# #                 </div>

# #                 <div class="location-value">
# #                     {speed_value:.1f} km/h
# #                 </div>

# #             </div>
# #             """,
# #             unsafe_allow_html=True,
# #         )


# #     recorded_at = latest["recorded_at"]


# #     try:

# #         recorded_dt = datetime.fromisoformat(
# #             recorded_at
# #         )

# #         if recorded_dt.tzinfo is None:

# #             recorded_dt = recorded_dt.replace(
# #                 tzinfo=timezone.utc
# #             )


# #         recorded_display = (
# #             recorded_dt
# #             .astimezone()
# #             .strftime(
# #                 "%d %b %Y, %I:%M:%S %p"
# #             )
# #         )

# #     except (TypeError, ValueError):

# #         recorded_display = recorded_at


# #     st.markdown(
# #         f"""
# #         <div style="
# #             margin-top:15px;
# #             color:#6b7280;
# #             font-size:13px;
# #         ">

# #             Last recorded at
# #             <strong>{escape(str(recorded_display))}</strong>

# #         </div>
# #         """,
# #         unsafe_allow_html=True,
# #     )


# #     maps_url = (
# #         "https://www.google.com/maps/search/?api=1"
# #         f"&query={latest['latitude']},{latest['longitude']}"
# #     )


# #     st.link_button(
# #         "Open Latest Location in Google Maps",
# #         maps_url,
# #         use_container_width=True,
# #     )


# # else:

# #     st.info(
# #         "No GPS location has been recorded yet. "
# #         "Start Location Protection."
# #     )


# # # ============================================================
# # # ACCESS REQUESTS
# # # ============================================================

# # st.markdown(
# #     '<div class="section-title">Access Requests</div>',
# #     unsafe_allow_html=True,
# # )

# # st.markdown(
# #     """
# #     <div class="section-subtitle">
# #         Approve, deny or revoke family location access.
# #     </div>
# #     """,
# #     unsafe_allow_html=True,
# # )


# # requests = database.get_driver_requests(
# #     driver_id
# # )


# # pending_requests = [
# #     request
# #     for request in requests
# #     if request["status"] == "PENDING"
# # ]


# # if not pending_requests:

# #     st.info(
# #         "No pending access requests."
# #     )


# # else:

# #     for request in pending_requests:

# #         requester_name = escape(
# #             str(request["requester_name"])
# #         )

# #         requester_phone = escape(
# #             str(request["requester_phone"])
# #         )

# #         duration = escape(
# #             str(request["duration"])
# #         )


# #         st.markdown(
# #             f"""
# #             <div
# #                 class="location-card"
# #                 style="margin-bottom:12px;"
# #             >

# #                 <div style="
# #                     font-size:17px;
# #                     font-weight:800;
# #                     color:#111827;
# #                 ">

# #                     {requester_name}

# #                 </div>


# #                 <div style="
# #                     margin-top:5px;
# #                     color:#6b7280;
# #                     font-size:13px;
# #                 ">

# #                     {requester_phone}

# #                 </div>


# #                 <div style="
# #                     margin-top:8px;
# #                     color:#6b7280;
# #                     font-size:13px;
# #                 ">

# #                     Requested access:
# #                     {duration}

# #                 </div>

# #             </div>
# #             """,
# #             unsafe_allow_html=True,
# #         )


# #         approve_col, deny_col = st.columns(2)


# #         with approve_col:

# #             if st.button(
# #                 "Approve",
# #                 key=f"approve_{request['id']}",
# #                 use_container_width=True,
# #                 type="primary",
# #             ):

# #                 duration_value = request["duration"]

# #                 expires_at = None

# #                 now = datetime.now(
# #                     timezone.utc
# #                 )


# #                 if duration_value == "ONE_TIME":

# #                     expires_at = (
# #                         now
# #                         + timedelta(minutes=10)
# #                     ).isoformat()


# #                 elif duration_value == "24_HOURS":

# #                     expires_at = (
# #                         now
# #                         + timedelta(hours=24)
# #                     ).isoformat()


# #                 elif duration_value == "7_DAYS":

# #                     expires_at = (
# #                         now
# #                         + timedelta(days=7)
# #                     ).isoformat()


# #                 elif duration_value == "UNTIL_REVOKED":

# #                     expires_at = None


# #                 database.update_access_request(
# #                     request["id"],
# #                     "ACTIVE",
# #                     expires_at,
# #                 )


# #                 st.success(
# #                     "Access approved."
# #                 )

# #                 st.rerun()


# #         with deny_col:

# #             if st.button(
# #                 "Deny",
# #                 key=f"deny_{request['id']}",
# #                 use_container_width=True,
# #             ):

# #                 database.deny_access(
# #                     request["id"]
# #                 )

# #                 st.warning(
# #                     "Access request denied."
# #                 )

# #                 st.rerun()


# # # ============================================================
# # # ACCESS HISTORY
# # # ============================================================

# # st.markdown(
# #     '<div class="section-title">Access History</div>',
# #     unsafe_allow_html=True,
# # )


# # for request in requests:

# #     status = request["status"]


# #     if status == "PENDING":

# #         continue


# #     requester_name = escape(
# #         str(request["requester_name"])
# #     )

# #     requester_phone = escape(
# #         str(request["requester_phone"])
# #     )

# #     duration = escape(
# #         str(request["duration"])
# #     )


# #     if status == "ACTIVE":

# #         st.markdown(
# #             f"""
# #             <div class="location-card">

# #                 <strong>
# #                     {requester_name}
# #                 </strong>

# #                 <span style="color:#15803d;">
# #                     · ACTIVE
# #                 </span>


# #                 <div style="
# #                     margin-top:5px;
# #                     color:#6b7280;
# #                     font-size:13px;
# #                 ">

# #                     {requester_phone}
# #                     ·
# #                     {duration}

# #                 </div>

# #             </div>
# #             """,
# #             unsafe_allow_html=True,
# #         )


# #         if st.button(
# #             "Revoke Access",
# #             key=f"revoke_{request['id']}",
# #             use_container_width=True,
# #         ):

# #             database.revoke_access(
# #                 request["id"]
# #             )

# #             st.rerun()


# #     elif status == "DENIED":

# #         st.warning(
# #             f"{requester_name} · DENIED"
# #         )


# #     elif status == "REVOKED":

# #         st.info(
# #             f"{requester_name} · REVOKED"
# #         )


# #     elif status == "EXPIRED":

# #         st.info(
# #             f"{requester_name} · EXPIRED"
# #         )


# # # ============================================================
# # # FOOTER
# # # ============================================================

# # st.markdown(
# #     """
# #     <div class="footer">

# #         <div>
# #             Guardrive © 2026
# #         </div>

# #         <div>
# #             Private location sharing · Prototype
# #         </div>

# #     </div>
# #     """,
# #     unsafe_allow_html=True,
# # )



























# import json
# import os
# from datetime import datetime, timezone, timedelta

# import streamlit as st
# import streamlit.components.v1 as components

# import database


# # ============================================================
# # PAGE CONFIG
# # ============================================================

# st.set_page_config(
#     page_title="Guardrive | Driver",
#     page_icon="🚗",
#     layout="wide",
#     initial_sidebar_state="collapsed",
# )


# # ============================================================
# # AUTH
# # ============================================================

# if not st.session_state.get("authenticated", False):
#     st.switch_page("app.py")


# # ============================================================
# # SESSION STATE
# # ============================================================

# if "driver_id" not in st.session_state:
#     st.session_state.driver_id = None

# if "tracking" not in st.session_state:
#     st.session_state.tracking = False


# # ============================================================
# # CONFIG
# # ============================================================

# GPS_API_URL = os.getenv(
#     "GPS_API_URL",
#     "http://127.0.0.1:8000"
# ).rstrip("/")

# MVP_DRIVER_NAME = "Ganesh"
# MVP_DRIVER_PHONE = "1111111111"


# # ============================================================
# # DRIVER LOAD / CREATE
# # ============================================================

# driver_id = st.session_state.get("driver_id")


# if driver_id is None:

#     driver = database.get_driver_by_phone(
#         MVP_DRIVER_PHONE
#     )

#     if not driver:

#         new_driver_id = database.create_driver(
#             name=MVP_DRIVER_NAME,
#             phone=MVP_DRIVER_PHONE,
#         )

#         if new_driver_id:
#             driver = database.get_driver_by_id(
#                 new_driver_id
#             )
#         else:
#             driver = database.get_driver_by_phone(
#                 MVP_DRIVER_PHONE
#             )

#     if not driver:
#         st.error(
#             f"Unable to load driver profile "
#             f"for {MVP_DRIVER_PHONE}."
#         )
#         st.stop()

#     driver_id = int(driver["id"])

#     st.session_state.driver_id = driver_id
#     st.session_state.driver_name = driver["name"]
#     st.session_state.driver_phone = driver["phone"]


# # ============================================================
# # VALIDATE DRIVER ID
# # ============================================================

# driver_id = st.session_state.get("driver_id")

# if driver_id is None:

#     st.session_state.tracking = False

#     st.error("Driver ID is missing.")
#     st.stop()


# try:

#     driver_id = int(driver_id)

# except (TypeError, ValueError):

#     st.session_state.driver_id = None
#     st.session_state.tracking = False

#     st.error("Invalid driver ID.")
#     st.stop()


# # ============================================================
# # LOAD DRIVER
# # ============================================================

# driver = database.get_driver_by_id(driver_id)

# if not driver:

#     st.session_state.driver_id = None
#     st.session_state.tracking = False

#     st.error("Driver profile could not be found.")
#     st.stop()


# # ============================================================
# # CSS ONLY
# # ============================================================

# st.markdown(
#     """
#     <style>

#     #MainMenu {
#         visibility: hidden;
#     }

#     header {
#         visibility: hidden;
#     }

#     footer {
#         visibility: hidden;
#     }

#     .block-container {
#         max-width: 1200px;
#         padding-top: 30px;
#         padding-bottom: 50px;
#     }

#     </style>
#     """,
#     unsafe_allow_html=True,
# )


# # ============================================================
# # HEADER
# # ============================================================

# header_col1, header_col2 = st.columns(
#     [5, 1],
#     vertical_alignment="center"
# )

# with header_col1:

#     st.markdown(
#         "# 🚗 Guardrive"
#     )

#     st.caption(
#         "DRIVER LOCATION PROTECTION"
#     )

# with header_col2:

#     st.success(
#         "● Secure Session"
#     )


# st.divider()


# # ============================================================
# # HERO
# # ============================================================

# st.markdown(
#     "### DRIVER PORTAL"
# )

# st.title(
#     "Your location. Your control."
# )

# st.write(
#     "Guardrive records your GPS location while "
#     "protection is active. Family members can only "
#     "access your location after you approve their request."
# )


# st.divider()


# # ============================================================
# # DRIVER INFORMATION
# # ============================================================

# col1, col2, col3 = st.columns(3)


# with col1:

#     st.caption("DRIVER")

#     st.subheader(
#         str(driver["name"])
#     )

#     st.caption(
#         str(driver["phone"])
#     )


# with col2:

#     st.caption(
#         "LOCATION PROTECTION"
#     )

#     if st.session_state.tracking:

#         st.success("ACTIVE")

#     else:

#         st.info("STOPPED")

#     st.caption(
#         "GPS recording status"
#     )


# with col3:

#     st.caption(
#         "LAST GPS RECORD"
#     )

#     latest = database.get_latest_location(
#         driver_id
#     )

#     if latest:

#         st.success(
#             "Location available"
#         )

#     else:

#         st.info(
#             "No location recorded"
#         )

#     st.caption(
#         "Verified database record"
#     )


# # ============================================================
# # LOCATION PROTECTION
# # ============================================================

# st.markdown("## Location Protection")

# st.caption(
#     "Start or stop GPS location recording "
#     "from this device."
# )


# button_col1, button_col2 = st.columns(2)


# with button_col1:

#     if not st.session_state.tracking:

#         if st.button(
#             "▶ Start Location Protection",
#             use_container_width=True,
#             type="primary",
#         ):

#             st.session_state.tracking = True

#             st.rerun()

#     else:

#         if st.button(
#             "■ Stop Location Protection",
#             use_container_width=True,
#         ):

#             st.session_state.tracking = False

#             st.rerun()


# with button_col2:

#     if st.button(
#         "← Back to Guardrive",
#         use_container_width=True,
#     ):

#         st.switch_page("app.py")


# # ============================================================
# # GPS TRACKING
# # ============================================================

# # if st.session_state.tracking:

# #     st.success(
# #         "● GPS protection is active. "
# #         "Keep this browser page open and allow location permission."
# #     )

# #     gps_api_json = json.dumps(
# #         GPS_API_URL
# #     )

# #     gps_html = f"""
# #     <!doctype html>

# #     <html>

# #     <head>

# #         <meta
# #             name="viewport"
# #             content="width=device-width, initial-scale=1"
# #         >

# #         <style>

# #             html, body {{
# #                 margin: 0;
# #                 padding: 0;
# #                 background: transparent;
# #                 font-family: Arial, sans-serif;
# #             }}

# #             #status {{
# #                 padding: 14px;
# #                 border-radius: 12px;
# #                 background: #f8fafc;
# #                 border: 1px solid #e5e7eb;
# #                 color: #475569;
# #                 font-size: 13px;
# #                 line-height: 1.45;
# #             }}

# #         </style>

# #     </head>

# #     <body>

# #         <div id="status">
# #             Starting continuous GPS tracking...
# #         </div>


# #         <script>

# #             const DRIVER_ID = {driver_id};

# #             const GPS_API = {gps_api_json};

# #             const statusBox =
# #                 document.getElementById("status");

# #             let sending = false;


# #             function setStatus(message) {{

# #                 statusBox.textContent = message;

# #             }}


# #             async function getBatteryLevel() {{

# #                 try {{

# #                     if (!navigator.getBattery) {{
# #                         return null;
# #                     }}

# #                     const battery =
# #                         await navigator.getBattery();

# #                     return Math.round(
# #                         battery.level * 100
# #                     );

# #                 }} catch (error) {{

# #                     return null;

# #                 }}

# #             }}


# #             async function sendCurrentLocation(position) {{

# #                 if (sending) {{
# #                     return;
# #                 }}

# #                 sending = true;


# #                 const coords =
# #                     position.coords;


# #                 const battery =
# #                     await getBatteryLevel();


# #                 const payload = {{

# #                     driver_id: DRIVER_ID,

# #                     latitude:
# #                         coords.latitude,

# #                     longitude:
# #                         coords.longitude,

# #                     accuracy:
# #                         coords.accuracy,

# #                     speed:
# #                         coords.speed,

# #                     heading:
# #                         coords.heading,

# #                     battery:
# #                         battery,

# #                     browser_timestamp:
# #                         position.timestamp

# #                 }};


# #                 setStatus(
# #                     "● GPS detected · Sending location..."
# #                 );


# #                 try {{

# #                     const response =
# #                         await fetch(
# #                             GPS_API + "/gps/update",
# #                             {{
# #                                 method: "POST",

# #                                 headers: {{
# #                                     "Content-Type":
# #                                         "application/json"
# #                                 }},

# #                                 body:
# #                                     JSON.stringify(payload)
# #                             }}
# #                         );


# #                     if (!response.ok) {{

# #                         const detail =
# #                             await response.text();

# #                         throw new Error(
# #                             detail ||
# #                             "GPS API error"
# #                         );

# #                     }}


# #                     await response.json();


# #                     const now =
# #                         new Date()
# #                         .toLocaleTimeString();


# #                     setStatus(
# #                         "● GPS ACTIVE · Last sent at "
# #                         + now
# #                     );


# #                 }} catch (error) {{

# #                     console.error(
# #                         error
# #                     );


# #                     setStatus(
# #                         "⚠ GPS detected, but "
# #                         + "location could not be sent."
# #                     );

# #                 }} finally {{

# #                     sending = false;

# #                 }}

# #             }}


# #             function gpsError(error) {{

# #                 if (error.code === 1) {{

# #                     setStatus(
# #                         "⚠ Location permission denied. "
# #                         + "Allow location access."
# #                     );

# #                 }}

# #                 else if (error.code === 2) {{

# #                     setStatus(
# #                         "⚠ Location unavailable. "
# #                         + "Check device GPS."
# #                     );

# #                 }}

# #                 else if (error.code === 3) {{

# #                     setStatus(
# #                         "⚠ GPS request timed out. "
# #                         + "Retrying..."
# #                     );

# #                 }}

# #                 else {{

# #                     setStatus(
# #                         "⚠ Unable to read GPS location."
# #                     );

# #                 }}

# #             }}


# #             function requestGPS() {{

# #                 if (!navigator.geolocation) {{

# #                     setStatus(
# #                         "This browser does not support GPS."
# #                     );

# #                     return;

# #                 }}


# #                 navigator.geolocation.getCurrentPosition(
# #                     sendCurrentLocation,
# #                     gpsError,
# #                     {{

# #                         enableHighAccuracy:
# #                             true,

# #                         maximumAge:
# #                             0,

# #                         timeout:
# #                             15000

# #                     }}
# #                 );

# #             }}


# #             function startTracking() {{

# #                 if (!window.isSecureContext) {{

# #                     setStatus(
# #                         "GPS requires HTTPS when deployed. "
# #                         + "localhost is allowed locally."
# #                     );

# #                     return;

# #                 }}


# #                 setStatus(
# #                     "Requesting GPS permission..."
# #                 );


# #                 // First location immediately
# #                 requestGPS();


# #                 // Continue every 3 seconds
# #                 setInterval(
# #                     requestGPS,
# #                     3000
# #                 );

# #             }}


# #             startTracking();

# #         </script>

# #     </body>

# #     </html>
# #     """


# #     components.html(
# #         gps_html,
# #         height=90,
# #         scrolling=False,
# #     )
# # ============================================================
# # GPS TRACKING
# # ============================================================

# if st.session_state.tracking:

#     st.success(
#         "● GPS protection is active. "
#         "Keep this browser page open and allow location permission."
#     )

#     gps_api_json = json.dumps(GPS_API_URL)

#     gps_html = f"""
#     <!doctype html>
#     <html>

#     <head>
#         <meta
#             name="viewport"
#             content="width=device-width, initial-scale=1"
#         >

#         <style>
#             html, body {{
#                 margin: 0;
#                 padding: 0;
#                 background: transparent;
#                 font-family: Arial, sans-serif;
#             }}

#             #status {{
#                 padding: 14px;
#                 border-radius: 12px;
#                 background: #f8fafc;
#                 border: 1px solid #e5e7eb;
#                 color: #475569;
#                 font-size: 13px;
#                 line-height: 1.45;
#             }}
#         </style>
#     </head>

#     <body>

#         <div id="status">
#             Starting GPS tracking...
#         </div>

#         <script>

#             const DRIVER_ID = {driver_id};
#             const GPS_API = {gps_api_json};

#             const statusBox =
#                 document.getElementById("status");

#             let sending = false;
#             let watchId = null;
#             let lastSentTime = 0;


#             function setStatus(message) {{
#                 statusBox.textContent = message;
#             }}


#             async function getBatteryLevel() {{

#                 try {{

#                     if (!navigator.getBattery) {{
#                         return null;
#                     }}

#                     const battery =
#                         await navigator.getBattery();

#                     return Math.round(
#                         battery.level * 100
#                     );

#                 }} catch (error) {{

#                     return null;

#                 }}
#             }}


#             async function sendLocation(position) {{

#                 if (sending) {{
#                     return;
#                 }}

#                 const now = Date.now();

#                 // Prevent excessive duplicate updates.
#                 if (
#                     lastSentTime > 0 &&
#                     now - lastSentTime < 2000
#                 ) {{
#                     return;
#                 }}

#                 sending = true;

#                 const coords = position.coords;

#                 const battery =
#                     await getBatteryLevel();

#                 const payload = {{

#                     driver_id: DRIVER_ID,

#                     latitude:
#                         coords.latitude,

#                     longitude:
#                         coords.longitude,

#                     accuracy:
#                         coords.accuracy,

#                     speed:
#                         coords.speed,

#                     heading:
#                         coords.heading,

#                     battery:
#                         battery,

#                     browser_timestamp:
#                         position.timestamp
#                 }};


#                 setStatus(
#                     "● GPS detected · Sending location..."
#                 );


#                 try {{

#                     const response =
#                         await fetch(
#                             GPS_API + "/gps/update",
#                             {{
#                                 method: "POST",

#                                 headers: {{
#                                     "Content-Type":
#                                         "application/json"
#                                 }},

#                                 body:
#                                     JSON.stringify(payload)
#                             }}
#                         );


#                     if (!response.ok) {{

#                         const detail =
#                             await response.text();

#                         throw new Error(
#                             detail ||
#                             "GPS API error"
#                         );
#                     }}


#                     await response.json();

#                     lastSentTime = now;


#                     const currentTime =
#                         new Date()
#                         .toLocaleTimeString();


#                     setStatus(
#                         "● GPS ACTIVE · Last sent at "
#                         + currentTime
#                     );


#                     console.log(
#                         "Guardrive GPS:",
#                         payload
#                     );


#                 }} catch (error) {{

#                     console.error(
#                         "Guardrive GPS error:",
#                         error
#                     );


#                     setStatus(
#                         "⚠ GPS detected, but "
#                         + "location could not be sent."
#                     );

#                 }} finally {{

#                     sending = false;

#                 }}
#             }}


#             function gpsError(error) {{

#                 console.error(
#                     "GPS error:",
#                     error
#                 );


#                 if (error.code === 1) {{

#                     setStatus(
#                         "⚠ Location permission denied. "
#                         + "Allow location access."
#                     );

#                 }}

#                 else if (error.code === 2) {{

#                     setStatus(
#                         "⚠ Location unavailable. "
#                         + "Check device GPS/location services."
#                     );

#                 }}

#                 else if (error.code === 3) {{

#                     setStatus(
#                         "⚠ GPS request timed out. "
#                         + "Waiting for another GPS update..."
#                     );

#                 }}

#                 else {{

#                     setStatus(
#                         "⚠ Unable to read GPS location."
#                     );

#                 }}
#             }}


#             function startTracking() {{

#                 if (!navigator.geolocation) {{

#                     setStatus(
#                         "⚠ This browser does not support GPS."
#                     );

#                     return;
#                 }}


#                 setStatus(
#                     "Requesting GPS permission..."
#                 );


#                 watchId =
#                     navigator.geolocation.watchPosition(

#                         sendLocation,

#                         gpsError,

#                         {{

#                             enableHighAccuracy: true,

#                             maximumAge: 0,

#                             timeout: 20000

#                         }}
#                     );


#                 console.log(
#                     "Guardrive GPS watcher started:",
#                     watchId
#                 );
#             }}


#             startTracking();

#         </script>

#     </body>
#     </html>
#     """


#     components.html(
#         gps_html,
#         height=90,
#         scrolling=False,
#     )

# # ============================================================
# # LATEST LOCATION
# # ============================================================

# st.markdown(
#     "## Latest Recorded Location"
# )

# st.caption(
#     "This is the latest location actually stored by Guardrive."
# )


# latest = database.get_latest_location(
#     driver_id
# )


# if latest:

#     location_col1, location_col2, location_col3 = st.columns(3)


#     with location_col1:

#         st.metric(
#             "Latitude",
#             f'{float(latest["latitude"]):.6f}'
#         )


#     with location_col2:

#         st.metric(
#             "Longitude",
#             f'{float(latest["longitude"]):.6f}'
#         )


#     with location_col3:

#         speed_value = float(
#             latest["speed"] or 0
#         )

#         st.metric(
#             "Speed",
#             f"{speed_value:.1f} km/h"
#         )


#     recorded_at = latest["recorded_at"]


#     try:

#         recorded_dt = datetime.fromisoformat(
#             recorded_at
#         )

#         if recorded_dt.tzinfo is None:

#             recorded_dt = recorded_dt.replace(
#                 tzinfo=timezone.utc
#             )


#         recorded_display = (
#             recorded_dt
#             .astimezone()
#             .strftime(
#                 "%d %b %Y, %I:%M:%S %p"
#             )
#         )

#     except (TypeError, ValueError):

#         recorded_display = recorded_at


#     st.caption(
#         f"Last recorded at {recorded_display}"
#     )


#     maps_url = (
#         "https://www.google.com/maps/search/?api=1"
#         f"&query={latest['latitude']},{latest['longitude']}"
#     )


#     st.link_button(
#         "📍 Open Latest Location in Google Maps",
#         maps_url,
#         use_container_width=True,
#     )


# else:

#     st.info(
#         "No GPS location has been recorded yet. "
#         "Start Location Protection."
#     )


# # ============================================================
# # ACCESS REQUESTS
# # ============================================================

# st.markdown(
#     "## Access Requests"
# )

# st.caption(
#     "Approve, deny or revoke family location access."
# )


# database.expire_old_access()


# requests = database.get_driver_requests(
#     driver_id
# )


# pending_requests = [
#     request
#     for request in requests
#     if request["status"] == "PENDING"
# ]


# if not pending_requests:

#     st.info(
#         "No pending access requests."
#     )


# else:

#     for request in pending_requests:

#         with st.container(border=True):

#             st.subheader(
#                 request["requester_name"]
#             )

#             st.caption(
#                 request["requester_phone"]
#             )

#             st.write(
#                 f"Requested access: "
#                 f"**{request['duration']}**"
#             )


#             approve_col, deny_col = st.columns(2)


#             with approve_col:

#                 if st.button(
#                     "Approve",
#                     key=f"approve_{request['id']}",
#                     use_container_width=True,
#                     type="primary",
#                 ):

#                     duration = request["duration"]

#                     expires_at = None

#                     now = datetime.now(
#                         timezone.utc
#                     )


#                     if duration == "ONE_TIME":

#                         expires_at = (
#                             now +
#                             timedelta(
#                                 minutes=10
#                             )
#                         ).isoformat()


#                     elif duration == "24_HOURS":

#                         expires_at = (
#                             now +
#                             timedelta(
#                                 hours=24
#                             )
#                         ).isoformat()


#                     elif duration == "7_DAYS":

#                         expires_at = (
#                             now +
#                             timedelta(
#                                 days=7
#                             )
#                         ).isoformat()


#                     elif duration == "UNTIL_REVOKED":

#                         expires_at = None


#                     database.update_access_request(
#                         request["id"],
#                         "ACTIVE",
#                         expires_at,
#                     )


#                     st.rerun()


#             with deny_col:

#                 if st.button(
#                     "Deny",
#                     key=f"deny_{request['id']}",
#                     use_container_width=True,
#                 ):

#                     database.deny_access(
#                         request["id"]
#                     )

#                     st.rerun()


# # ============================================================
# # ACCESS HISTORY
# # ============================================================

# st.markdown(
#     "## Access History"
# )


# for request in requests:

#     status = request["status"]


#     if status == "PENDING":
#         continue


#     if status == "ACTIVE":

#         with st.container(border=True):

#             st.subheader(
#                 request["requester_name"]
#             )

#             st.success(
#                 "● ACTIVE"
#             )

#             st.caption(
#                 f"{request['requester_phone']} · "
#                 f"{request['duration']}"
#             )


#             if st.button(
#                 "Revoke Access",
#                 key=f"revoke_{request['id']}",
#                 use_container_width=True,
#             ):

#                 database.revoke_access(
#                     request["id"]
#                 )

#                 st.rerun()


#     elif status == "DENIED":

#         st.warning(
#             f"{request['requester_name']} · DENIED"
#         )


#     elif status == "REVOKED":

#         st.info(
#             f"{request['requester_name']} · REVOKED"
#         )


#     elif status == "EXPIRED":

#         st.info(
#             f"{request['requester_name']} · EXPIRED"
#         )


# # ============================================================
# # FOOTER
# # ============================================================

# st.divider()

# left, right = st.columns(2)

# with left:

#     st.caption(
#         "Guardrive © 2026"
#     )

# with right:

#     st.caption(
#         "Private location sharing · Prototype"
#     )







































import os
from datetime import datetime, timezone, timedelta

import streamlit as st
import streamlit.components.v1 as components

import database


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Guardrive · Driver",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# SESSION STATE
# ============================================================

if "driver_id" not in st.session_state:
    st.session_state.driver_id = None

if "driver_name" not in st.session_state:
    st.session_state.driver_name = None

if "driver_phone" not in st.session_state:
    st.session_state.driver_phone = None

if "tracking" not in st.session_state:
    st.session_state.tracking = False


# ============================================================
# AUTHENTICATION
# ============================================================

if not st.session_state.get("authenticated", False):
    st.switch_page("app.py")


# ============================================================
# GPS SERVER
# ============================================================

GPS_API_URL = os.getenv(
    "GPS_API_URL",
    "http://127.0.0.1:8000"
)


# ============================================================
# HELPERS
# ============================================================

def logout_driver():
    """
    Logout current driver.
    Main Guardrive application login remains active.
    """

    st.session_state.driver_id = None
    st.session_state.driver_name = None
    st.session_state.driver_phone = None
    st.session_state.tracking = False

    st.rerun()


def get_all_drivers():

    conn = database.get_connection()

    try:

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                name,
                phone,
                active,
                created_at
            FROM drivers
            WHERE active = 1
            ORDER BY id DESC
        """)

        return cursor.fetchall()

    finally:

        conn.close()


def login_driver(driver):

    st.session_state.driver_id = int(
        driver["id"]
    )

    st.session_state.driver_name = (
        driver["name"]
    )

    st.session_state.driver_phone = (
        driver["phone"]
    )

    st.session_state.tracking = False

    st.rerun()


def format_timestamp(timestamp):

    if not timestamp:
        return "—"

    try:

        dt = datetime.fromisoformat(
            timestamp
        )

        if dt.tzinfo is None:
            dt = dt.replace(
                tzinfo=timezone.utc
            )

        dt = dt.astimezone()

        return dt.strftime(
            "%d %b %Y, %I:%M:%S %p"
        )

    except Exception:

        return str(timestamp)


# ============================================================
# CSS
# ============================================================

st.html(
    """
    <style>

    .gd-page-title {
        font-size: 30px;
        font-weight: 800;
        color: #111827;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    .gd-page-subtitle {
        font-size: 14px;
        color: #6b7280;
        margin-bottom: 25px;
    }

    .gd-section-title {
        font-size: 18px;
        font-weight: 750;
        color: #111827;
        margin-bottom: 4px;
    }

    .gd-section-subtitle {
        font-size: 13px;
        color: #6b7280;
    }

    .gd-driver-name {
        font-size: 16px;
        font-weight: 750;
        color: #111827;
    }

    .gd-driver-phone {
        font-size: 13px;
        color: #6b7280;
        margin-top: 4px;
    }

    .gd-active {
        display: inline-block;
        background: #dcfce7;
        color: #166534;
        border-radius: 999px;
        padding: 6px 11px;
        font-size: 11px;
        font-weight: 700;
        white-space: nowrap;
    }

    .gd-profile-name {
        font-size: 25px;
        font-weight: 800;
        color: #111827;
    }

    .gd-profile-phone {
        font-size: 14px;
        color: #6b7280;
        margin-top: 4px;
    }

    .gd-label {
        font-size: 12px;
        color: #6b7280;
        margin-bottom: 5px;
    }

    .gd-last-record {
        margin-top: 15px;
        padding: 13px 15px;
        background: #f8fafc;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        font-size: 13px;
        color: #4b5563;
    }

    .gd-footer {
        text-align: center;
        color: #9ca3af;
        font-size: 12px;
        margin-top: 35px;
        padding-top: 20px;
        border-top: 1px solid #e5e7eb;
    }

    </style>
    """
)


# ============================================================
# HEADER
# ============================================================

header_left, header_home, header_logout = st.columns(
    [6, 1.2, 1.2],
    vertical_alignment="center"
)


with header_left:

    st.html(
        """
        <div style="
            font-size:23px;
            font-weight:800;
            color:#111827;
            letter-spacing:-0.5px;
        ">
            Guard<span style="color:#2563eb;">rive</span>
        </div>

        <div style="
            color:#6b7280;
            font-size:12px;
            margin-top:3px;
            letter-spacing:.4px;
        ">
            DRIVER PORTAL
        </div>
        """
    )


with header_home:

    if st.button(
        "← Home",
        use_container_width=True
    ):

        st.switch_page("app.py")


with header_logout:

    if st.session_state.driver_id is not None:

        if st.button(
            "Logout",
            use_container_width=True
        ):

            logout_driver()


# ============================================================
# ============================================================
# NO DRIVER LOGGED IN
# ============================================================
# ============================================================

if st.session_state.driver_id is None:

    # --------------------------------------------------------
    # PAGE TITLE
    # --------------------------------------------------------

    st.html(
        """
        <div class="gd-page-title">
            Driver Access
        </div>

        <div class="gd-page-subtitle">
            Select an existing driver or create a new driver profile.
        </div>
        """
    )


    # --------------------------------------------------------
    # EXISTING DRIVERS
    # --------------------------------------------------------

    drivers = get_all_drivers()


    if drivers:

        st.html(
            """
            <div style="
                background:white;
                border:1px solid #e5e7eb;
                border-radius:16px;
                padding:20px;
                margin-bottom:15px;
            ">

                <div class="gd-section-title">
                    Existing Drivers
                </div>

                <div class="gd-section-subtitle">
                    Select a driver to continue.
                </div>

            </div>
            """
        )


        for driver in drivers:

            col1, col2, col3 = st.columns(
                [4, 2, 1.2],
                vertical_alignment="center"
            )


            with col1:

                st.html(
                    f"""
                    <div style="
                        padding:13px 0;
                    ">

                        <div class="gd-driver-name">
                            {driver["name"]}
                        </div>

                        <div class="gd-driver-phone">
                            {driver["phone"]}
                        </div>

                    </div>
                    """
                )


            with col2:

                st.html(
                    """
                    <div class="gd-active">
                        ● ACTIVE DRIVER
                    </div>
                    """
                )


            with col3:

                if st.button(
                    "Login",
                    key=f"login_driver_{driver['id']}",
                    use_container_width=True
                ):

                    login_driver(driver)


            st.html(
                """
                <div style="
                    height:1px;
                    background:#e5e7eb;
                    margin:3px 0 8px 0;
                "></div>
                """
            )


    # --------------------------------------------------------
    # CREATE NEW DRIVER
    # --------------------------------------------------------

    st.html(
        """
        <div style="
            margin-top:25px;
            margin-bottom:15px;
        ">

            <div class="gd-section-title">
                Create New Driver
            </div>

            <div class="gd-section-subtitle">
                Create a new driver profile and start using Guardrive.
            </div>

        </div>
        """
    )


    with st.form(
        "create_new_driver",
        clear_on_submit=False
    ):

        new_driver_name = st.text_input(
            "Driver Name",
            placeholder="Enter driver name"
        )

        new_driver_phone = st.text_input(
            "Driver Phone Number",
            placeholder="Enter phone number"
        )


        create_button = st.form_submit_button(
            "Create Driver & Continue",
            use_container_width=True
        )


        if create_button:

            name = new_driver_name.strip()
            phone = new_driver_phone.strip()


            if not name:

                st.error(
                    "Please enter the driver name."
                )


            elif not phone:

                st.error(
                    "Please enter the driver phone number."
                )


            elif not phone.isdigit():

                st.error(
                    "Phone number should contain digits only."
                )


            elif len(phone) < 10:

                st.error(
                    "Please enter a valid phone number."
                )


            else:

                existing_driver = (
                    database.get_driver_by_phone(
                        phone
                    )
                )


                if existing_driver:

                    st.error(
                        "A driver with this phone number "
                        "already exists."
                    )


                else:

                    try:

                        new_driver_id = (
                            database.create_driver(
                                name=name,
                                phone=phone
                            )
                        )


                        if new_driver_id:

                            st.session_state.driver_id = int(
                                new_driver_id
                            )

                            st.session_state.driver_name = name

                            st.session_state.driver_phone = phone

                            st.session_state.tracking = False

                            st.rerun()


                        else:

                            st.error(
                                "Could not create driver."
                            )


                    except Exception as e:

                        st.error(
                            f"Unable to create driver: {e}"
                        )


    # --------------------------------------------------------
    # FOOTER
    # --------------------------------------------------------

    st.html(
        """
        <div class="gd-footer">
            Guardrive · Driver-controlled location sharing
        </div>
        """
    )


    # IMPORTANT:
    # Do NOT render driver dashboard below this.
    st.stop()


# ============================================================
# ============================================================
# DRIVER LOGGED IN
# ============================================================
# ============================================================

driver_id = st.session_state.driver_id


# ============================================================
# LOAD DRIVER
# ============================================================

driver = database.get_driver_by_id(
    driver_id
)


if not driver:

    st.session_state.driver_id = None
    st.session_state.driver_name = None
    st.session_state.driver_phone = None
    st.session_state.tracking = False

    st.rerun()


driver_name = driver["name"]
driver_phone = driver["phone"]


# ============================================================
# HERO
# ============================================================

st.html(
    f"""
    <div style="
        background:linear-gradient(
            135deg,
            #111827 0%,
            #1f2937 100%
        );
        border-radius:20px;
        padding:30px;
        color:white;
        margin-top:15px;
        margin-bottom:24px;
    ">

        <div style="
            font-size:30px;
            font-weight:800;
            margin-bottom:6px;
        ">
            Welcome, {driver_name}
        </div>

        <div style="
            color:#d1d5db;
            font-size:14px;
        ">
            Control who can access your location and
            manage your active location sharing.
        </div>

    </div>
    """
)


# ============================================================
# DRIVER PROFILE
# ============================================================

profile_left, profile_right = st.columns(
    [4, 1.5],
    vertical_alignment="center"
)


with profile_left:

    st.html(
        f"""
        <div style="
            background:white;
            border:1px solid #e5e7eb;
            border-radius:16px;
            padding:20px;
        ">

            <div class="gd-label">
                DRIVER
            </div>

            <div class="gd-profile-name">
                {driver_name}
            </div>

            <div class="gd-profile-phone">
                📱 {driver_phone}
            </div>

        </div>
        """
    )


with profile_right:

    if st.button(
        "＋ Create New Driver",
        use_container_width=True
    ):

        st.session_state.driver_id = None
        st.session_state.driver_name = None
        st.session_state.driver_phone = None
        st.session_state.tracking = False

        st.rerun()


# ============================================================
# LOCATION PROTECTION
# ============================================================

st.html(
    """
    <div style="
        background:white;
        border:1px solid #e5e7eb;
        border-radius:16px;
        padding:20px;
        margin-top:20px;
        margin-bottom:15px;
    ">

        <div class="gd-section-title">
            Location Protection
        </div>

        <div class="gd-section-subtitle">
            Your location is shared only when you allow access.
        </div>

    </div>
    """
)


if not st.session_state.tracking:

    if st.button(
        "▶ Start Location Protection",
        type="primary",
        use_container_width=True
    ):

        st.session_state.tracking = True
        st.rerun()

else:

    if st.button(
        "■ Stop Location Protection",
        use_container_width=True
    ):

        st.session_state.tracking = False
        st.rerun()


# ============================================================
# GPS TRACKING
# ============================================================

if st.session_state.tracking:

    gps_html = f"""
    <!DOCTYPE html>

    <html>

    <head>

        <meta charset="UTF-8">

        <style>

            body {{
                margin:0;
                padding:0;
                font-family:Arial,sans-serif;
                background:transparent;
            }}

            .gps-box {{
                border:1px solid #bbf7d0;
                background:#f0fdf4;
                border-radius:14px;
                padding:15px;
                color:#166534;
                font-size:14px;
            }}

            .gps-title {{
                font-weight:700;
                margin-bottom:5px;
            }}

        </style>

    </head>

    <body>

        <div class="gps-box">

            <div class="gps-title">
                Location Protection Active
            </div>

            <div id="status">
                Requesting GPS permission...
            </div>

        </div>


        <script>

        const DRIVER_ID = {int(driver_id)};

        const GPS_API = "{GPS_API_URL}";

        let sending = false;

        let watchId = null;

        let lastSentTime = 0;


        function setStatus(message) {{

            const status =
                document.getElementById("status");

            if (status) {{
                status.textContent = message;
            }}

        }}


        async function getBatteryLevel() {{

            try {{

                if (!navigator.getBattery) {{
                    return null;
                }}

                const battery =
                    await navigator.getBattery();

                return Math.round(
                    battery.level * 100
                );

            }} catch (error) {{

                return null;

            }}

        }}


        async function sendLocation(position) {{

            if (sending) {{
                return;
            }}


            const now = Date.now();


            if (
                lastSentTime > 0 &&
                now - lastSentTime < 2000
            ) {{
                return;
            }}


            sending = true;


            const coords =
                position.coords;


            const battery =
                await getBatteryLevel();


            const payload = {{

                driver_id: DRIVER_ID,

                latitude:
                    coords.latitude,

                longitude:
                    coords.longitude,

                accuracy:
                    coords.accuracy,

                speed:
                    coords.speed,

                heading:
                    coords.heading,

                battery:
                    battery,

                browser_timestamp:
                    position.timestamp

            }};


            setStatus(
                "● GPS detected · Sending location..."
            );


            try {{

                const response =
                    await fetch(
                        GPS_API + "/gps/update",
                        {{
                            method:"POST",

                            headers:{{
                                "Content-Type":
                                    "application/json"
                            }},

                            body:
                                JSON.stringify(payload)
                        }}
                    );


                if (!response.ok) {{

                    const detail =
                        await response.text();

                    throw new Error(
                        detail ||
                        "GPS API error"
                    );

                }}


                await response.json();


                lastSentTime = now;


                setStatus(
                    "● GPS ACTIVE · Last sent at "
                    + new Date().toLocaleTimeString()
                );


            }} catch (error) {{

                console.error(
                    "Guardrive GPS error:",
                    error
                );


                setStatus(
                    "⚠ GPS detected, but "
                    + "location could not be sent."
                );


            }} finally {{

                sending = false;

            }}

        }}


        function gpsError(error) {{

            console.error(
                "GPS error:",
                error
            );


            if (error.code === 1) {{

                setStatus(
                    "⚠ Location permission denied."
                );

            }}

            else if (error.code === 2) {{

                setStatus(
                    "⚠ Location unavailable."
                );

            }}

            else if (error.code === 3) {{

                setStatus(
                    "⚠ GPS request timed out. "
                    + "Waiting for another update..."
                );

            }}

            else {{

                setStatus(
                    "⚠ Unable to read GPS location."
                );

            }}

        }}


        function startTracking() {{

            if (!navigator.geolocation) {{

                setStatus(
                    "⚠ This browser does not support GPS."
                );

                return;

            }}


            setStatus(
                "Requesting GPS permission..."
            );


            watchId =
                navigator.geolocation.watchPosition(
                    sendLocation,
                    gpsError,
                    {{
                        enableHighAccuracy:true,
                        maximumAge:0,
                        timeout:20000
                    }}
                );

        }}


        startTracking();

        </script>

    </body>

    </html>
    """


    components.html(
        gps_html,
        height=100
    )


# ============================================================
# LATEST LOCATION
# ============================================================

st.html(
    """
    <div style="
        background:white;
        border:1px solid #e5e7eb;
        border-radius:16px;
        padding:20px;
        margin-top:20px;
        margin-bottom:15px;
    ">

        <div class="gd-section-title">
            Latest Recorded Location
        </div>

        <div class="gd-section-subtitle">
            This shows the actual latest GPS record.
        </div>

    </div>
    """
)


latest_location = database.get_latest_location(
    driver_id
)


if latest_location:

    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Latitude",
            f"{latest_location['latitude']:.6f}"
        )


    with col2:

        st.metric(
            "Longitude",
            f"{latest_location['longitude']:.6f}"
        )


    with col3:

        speed = (
            latest_location["speed"]
            or 0
        )

        status = (
            "MOVING"
            if speed > 2
            else "STATIONARY"
        )

        st.metric(
            "Driver Status",
            status
        )


    st.html(
        f"""
        <div class="gd-last-record">

            <strong>
                Last GPS record:
            </strong>

            {format_timestamp(
                latest_location["recorded_at"]
            )}

        </div>
        """
    )


    maps_url = (
        "https://www.google.com/maps/search/?api=1"
        f"&query={latest_location['latitude']},"
        f"{latest_location['longitude']}"
    )


    st.link_button(
        "📍 Open Latest Location in Google Maps",
        maps_url,
        use_container_width=True
    )


else:

    st.info(
        "No GPS location has been recorded yet. "
        "Start Location Protection to begin recording."
    )


# ============================================================
# ACCESS REQUESTS
# ============================================================

st.html(
    """
    <div style="
        background:white;
        border:1px solid #e5e7eb;
        border-radius:16px;
        padding:20px;
        margin-top:20px;
        margin-bottom:15px;
    ">

        <div class="gd-section-title">
            Location Access Requests
        </div>

        <div class="gd-section-subtitle">
            Approve, deny or revoke access to your location.
        </div>

    </div>
    """
)


try:

    database.expire_old_access()

except AttributeError:

    pass


requests = database.get_driver_requests(
    driver_id
)


if not requests:

    st.info(
        "No location access requests yet."
    )


else:

    for request in requests:

        request_id = request["id"]

        requester_name = (
            request["requester_name"]
        )

        requester_phone = (
            request["requester_phone"]
        )

        duration = (
            request["duration"]
        )

        status = (
            request["status"]
        )

        created_at = (
            request["created_at"]
        )


        with st.container(border=True):

            left, right = st.columns(
                [4, 2],
                vertical_alignment="center"
            )


            with left:

                st.html(
                    f"""
                    <div class="gd-driver-name">
                        {requester_name}
                    </div>

                    <div class="gd-driver-phone">
                        📱 {requester_phone}
                    </div>

                    <div class="gd-driver-phone">
                        Access: {duration}
                    </div>

                    <div class="gd-driver-phone">
                        Requested:
                        {format_timestamp(created_at)}
                    </div>
                    """
                )


            with right:

                if status == "PENDING":

                    st.warning("PENDING")

                    approve_col, deny_col = st.columns(2)


                    with approve_col:

                        if st.button(
                            "Approve",
                            key=f"approve_{request_id}",
                            use_container_width=True
                        ):

                            expires_at = None


                            if duration == "ONE_TIME":

                                expires_at = (
                                    datetime.now(
                                        timezone.utc
                                    )
                                    + timedelta(
                                        minutes=30
                                    )
                                ).isoformat()


                            elif duration == "24_HOURS":

                                expires_at = (
                                    datetime.now(
                                        timezone.utc
                                    )
                                    + timedelta(
                                        hours=24
                                    )
                                ).isoformat()


                            elif duration == "7_DAYS":

                                expires_at = (
                                    datetime.now(
                                        timezone.utc
                                    )
                                    + timedelta(
                                        days=7
                                    )
                                ).isoformat()


                            database.update_access_request(
                                request_id,
                                "ACTIVE",
                                expires_at
                            )

                            st.rerun()


                    with deny_col:

                        if st.button(
                            "Deny",
                            key=f"deny_{request_id}",
                            use_container_width=True
                        ):

                            try:

                                database.deny_access(
                                    request_id
                                )

                            except AttributeError:

                                database.update_access_request(
                                    request_id,
                                    "DENIED",
                                    None
                                )

                            st.rerun()


                elif status == "ACTIVE":

                    st.success("ACTIVE")


                    if st.button(
                        "Revoke",
                        key=f"revoke_{request_id}",
                        use_container_width=True
                    ):

                        try:

                            database.revoke_access(
                                request_id
                            )

                        except AttributeError:

                            database.update_access_request(
                                request_id
                            )

                        st.rerun()


                elif status == "DENIED":

                    st.error("DENIED")


                elif status == "REVOKED":

                    st.info("REVOKED")


                elif status == "EXPIRED":

                    st.info("EXPIRED")


                else:

                    st.info(status)


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <div class="gd-footer">
        Guardrive · Driver-controlled location sharing
    </div>
    """
)

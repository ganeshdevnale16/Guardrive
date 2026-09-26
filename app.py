# # import streamlit as st

# # APP_PASSWORD = "11111"

# # st.set_page_config(
# #     page_title="Guardrive",
# #     page_icon="🛡️",
# #     layout="wide",
# #     initial_sidebar_state="collapsed",
# # )

# # if "authenticated" not in st.session_state:
# #     st.session_state.authenticated = False


# # st.markdown(
# #     """
# #     <style>
# #     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

# #     html, body, [class*="css"] {
# #         font-family: "Inter", sans-serif;
# #     }

# #     #MainMenu, header, footer {
# #         visibility: hidden;
# #     }

# #     .block-container {
# #         max-width: 1180px;
# #         padding: 28px 24px 40px 24px;
# #     }

# #     .login-wrapper {
# #         min-height: 78vh;
# #         display: flex;
# #         align-items: center;
# #         justify-content: center;
# #         flex-direction: column;
# #     }

# #     .login-brand {
# #         text-align: center;
# #         margin-bottom: 24px;
# #     }

# #     .login-logo, .brand-logo {
# #         display: flex;
# #         align-items: center;
# #         justify-content: center;
# #         background: #111827;
# #         color: #fff;
# #         font-weight: 800;
# #     }

# #     .login-logo {
# #         width: 64px;
# #         height: 64px;
# #         margin: 0 auto 14px;
# #         border-radius: 18px;
# #         font-size: 28px;
# #     }

# #     .login-title {
# #         font-size: 32px;
# #         font-weight: 800;
# #         color: #111827;
# #     }

# #     .login-subtitle {
# #         margin-top: 6px;
# #         color: #6b7280;
# #         font-size: 14px;
# #     }

# #     .login-card {
# #         width: 100%;
# #         max-width: 430px;
# #         box-sizing: border-box;
# #         padding: 30px;
# #         border: 1px solid #e5e7eb;
# #         border-radius: 20px;
# #         background: #fff;
# #         box-shadow: 0 12px 35px rgba(15, 23, 42, .08);
# #     }

# #     .login-heading {
# #         font-size: 22px;
# #         font-weight: 700;
# #         color: #111827;
# #         text-align: center;
# #     }

# #     .login-description {
# #         color: #6b7280;
# #         font-size: 14px;
# #         text-align: center;
# #         margin: 7px 0 22px;
# #     }

# #     .security-note {
# #         text-align: center;
# #         color: #6b7280;
# #         font-size: 12px;
# #         margin-top: 18px;
# #     }

# #     .navbar {
# #         display: flex;
# #         align-items: center;
# #         justify-content: space-between;
# #         gap: 20px;
# #         padding: 8px 0 28px;
# #     }

# #     .brand-container {
# #         display: flex;
# #         align-items: center;
# #         gap: 12px;
# #         min-width: 0;
# #     }

# #     .brand-logo {
# #         width: 42px;
# #         height: 42px;
# #         flex: 0 0 42px;
# #         border-radius: 12px;
# #         font-size: 19px;
# #     }

# #     .brand-name {
# #         font-size: 20px;
# #         font-weight: 800;
# #         color: #111827;
# #     }

# #     .brand-caption {
# #         font-size: 9px;
# #         letter-spacing: 1.4px;
# #         color: #9ca3af;
# #         margin-top: 2px;
# #     }

# #     .system-active {
# #         color: #15803d;
# #         font-size: 13px;
# #         font-weight: 600;
# #         white-space: nowrap;
# #     }

# #     .hero {
# #         position: relative;
# #         overflow: hidden;
# #         min-height: 280px;
# #         box-sizing: border-box;
# #         border-radius: 26px;
# #         background: #111827;
# #         padding: 48px;
# #         margin-bottom: 40px;
# #     }

# #     .hero-content {
# #         position: relative;
# #         z-index: 2;
# #         max-width: 650px;
# #     }

# #     .hero-badge {
# #         color: #d1d5db;
# #         font-size: 11px;
# #         font-weight: 700;
# #         letter-spacing: 1.5px;
# #         margin-bottom: 18px;
# #     }

# #     .hero-title {
# #         color: #fff;
# #         font-size: 46px;
# #         line-height: 1.05;
# #         font-weight: 800;
# #     }

# #     .hero-description {
# #         color: #d1d5db;
# #         line-height: 1.7;
# #         font-size: 15px;
# #         margin-top: 20px;
# #         max-width: 600px;
# #     }

# #     .hero-circle-one, .hero-circle-two {
# #         position: absolute;
# #         border-radius: 50%;
# #         pointer-events: none;
# #     }

# #     .hero-circle-one {
# #         width: 300px;
# #         height: 300px;
# #         right: -100px;
# #         top: -110px;
# #         border: 1px solid rgba(255,255,255,.1);
# #     }

# #     .hero-circle-two {
# #         width: 220px;
# #         height: 220px;
# #         right: 80px;
# #         bottom: -130px;
# #         border: 1px solid rgba(255,255,255,.08);
# #     }

# #     .section-title {
# #         font-size: 23px;
# #         font-weight: 800;
# #         color: #111827;
# #         margin-bottom: 5px;
# #     }

# #     .section-description {
# #         color: #6b7280;
# #         margin-bottom: 20px;
# #         font-size: 14px;
# #     }

# #     .portal-card {
# #         width: 100%;
# #         min-width: 0;
# #         min-height: 190px;
# #         box-sizing: border-box;
# #         overflow-wrap: anywhere;
# #         border: 1px solid #e5e7eb;
# #         border-radius: 20px;
# #         padding: 25px;
# #         background: #fff;
# #         margin-bottom: 12px;
# #     }

# #     .portal-icon {
# #         font-size: 30px;
# #         line-height: 1;
# #     }

# #     .portal-title {
# #         font-size: 20px;
# #         font-weight: 800;
# #         margin-top: 12px;
# #         color: #111827;
# #     }

# #     .portal-description {
# #         color: #6b7280;
# #         font-size: 14px;
# #         line-height: 1.65;
# #         margin-top: 8px;
# #         overflow-wrap: anywhere;
# #         word-break: normal;
# #     }

# #     .security-card {
# #         margin-top: 25px;
# #         padding: 22px;
# #         box-sizing: border-box;
# #         border-radius: 18px;
# #         background: #f8fafc;
# #         border: 1px solid #e5e7eb;
# #     }

# #     .footer {
# #         margin-top: 50px;
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

# #         .hero {
# #             padding: 30px;
# #             min-height: 250px;
# #         }

# #         .hero-title {
# #             font-size: 34px;
# #         }

# #         .navbar, .footer {
# #             align-items: flex-start;
# #             flex-direction: column;
# #         }

# #         .system-active {
# #             margin-left: 54px;
# #         }
# #     }
# #     </style>
# #     """,
# #     unsafe_allow_html=True,
# # )


# # if not st.session_state.authenticated:
# #     st.markdown(
# #         """
# #         <div class="login-wrapper">
# #             <div class="login-brand">
# #                 <div class="login-logo">G</div>
# #                 <div class="login-title">Guardrive</div>
# #                 <div class="login-subtitle">
# #                     Private location sharing platform
# #                 </div>
# #             </div>
            

# #             <div class="login-card">
# #                 <div class="login-heading">Welcome back</div>
# #                 <div class="login-description">
# #                     Sign in to access the Guardrive platform.
# #                 </div>
# #             </div>
# #         </div>
# #         """,
# #         unsafe_allow_html=True,
# #     )

# #     password = st.text_input(
# #         "Password",
# #         type="password",
# #         placeholder="Enter your password",
# #         key="login_password",
# #     )

# #     if st.button(
# #         "Sign in to Guardrive",
# #         type="primary",
# #         use_container_width=True,
# #     ):
# #         if password == APP_PASSWORD:
# #             st.session_state.authenticated = True
# #             st.rerun()
# #         else:
# #             st.error("Incorrect password. Please try again.")

# #     st.markdown(
# #         '<div class="security-note">🔒 Protected access · Guardrive</div>',
# #         unsafe_allow_html=True,
# #     )
# #     st.stop()


# # nav_left, nav_right = st.columns([6, 1], vertical_alignment="center")

# # with nav_left:
# #     st.markdown(
# #         """
# #         <div class="navbar">
# #             <div class="brand-container">
# #                 <div class="brand-logo">G</div>
# #                 <div>
# #                     <div class="brand-name">Guardrive</div>
# #                     <div class="brand-caption">
# #                         PRIVATE LOCATION SHARING
# #                     </div>
# #                 </div>
# #             </div>

# #             <div class="system-active">● System Active</div>
# #         </div>
# #         """,
# #         unsafe_allow_html=True,
# #     )

# # with nav_right:
# #     if st.button("Sign out", use_container_width=True):
# #         st.session_state.clear()
# #         st.rerun()


# # st.markdown(
# #     """
# #     <div class="hero">
# #         <div class="hero-circle-one"></div>
# #         <div class="hero-circle-two"></div>

# #         <div class="hero-content">
# #             <div class="hero-badge">🛡 LOCATION PROTECTION</div>
# #             <div class="hero-title">
# #                 Stay connected.<br>
# #                 Stay in control.
# #             </div>
# #             <div class="hero-description">
# #                 Guardrive gives drivers complete control over
# #                 location sharing. Approve access requests,
# #                 control sharing duration and decide who can
# #                 access your location.
# #             </div>
# #         </div>
# #     </div>

# #     <div class="section-title">Choose your experience</div>
# #     <div class="section-description">
# #         Select a portal to continue.
# #     </div>
# #     """,
# #     unsafe_allow_html=True,
# # )


# # driver_col, family_col = st.columns(2, gap="large")

# # with driver_col:
# #     st.markdown(
# #         """
# #         <div class="portal-card">
# #             <div class="portal-icon">🚗</div>
# #             <div class="portal-title">Driver Portal</div>
# #             <div class="portal-description">
# #                 Manage location protection, start GPS tracking,
# #                 review access requests and control who can
# #                 access your location.
# #             </div>
# #         </div>
# #         """,
# #         unsafe_allow_html=True,
# #     )

# #     if st.button(
# #         "Open Driver Portal",
# #         use_container_width=True,
# #         type="primary",
# #         key="open_driver",
# #     ):
# #         st.switch_page("Driver.py")

# # with family_col:
# #     st.markdown(
# #         """
# #         <div class="portal-card">
# #             <div class="portal-icon">👥</div>
# #             <div class="portal-title">Family Access</div>
# #             <div class="portal-description">
# #                 Request authorized access to a driver's
# #                 location and view the latest available
# #                 position.
# #             </div>
# #         </div>
# #         """,
# #         unsafe_allow_html=True,
# #     )

# #     if st.button(
# #         "Open Family Access",
# #         use_container_width=True,
# #         key="open_family",
# #     ):
# #         st.switch_page("Family_Chat.py")


# # st.markdown(
# #     """
# #     <div class="security-card">
# #         <div style="
# #             font-size:16px;
# #             font-weight:700;
# #             color:#111827;
# #         ">
# #             🔐 Privacy by design
# #         </div>

# #         <div style="
# #             color:#6b7280;
# #             font-size:13px;
# #             line-height:1.6;
# #             margin-top:7px;
# #         ">
# #             A phone number alone never exposes a driver's
# #             location. Every access request requires explicit
# #             driver approval and can be revoked.
# #         </div>
# #     </div>

# #     <div class="footer">
# #         <div>Guardrive © 2026</div>
# #         <div>Private location sharing · Prototype</div>
# #     </div>
# #     """,
# #     unsafe_allow_html=True,
# # )















# import streamlit as st


# # ============================================================
# # APP CONFIG
# # ============================================================

# APP_PASSWORD = "11111"

# st.set_page_config(
#     page_title="Guardrive",
#     page_icon="🛡️",
#     layout="wide",
#     initial_sidebar_state="collapsed",
# )
# # ============================================================
# # ROOT-LEVEL PAGES
# # ============================================================

# driver_page = st.Page(
#     "Driver.py",
#     title="Driver Portal",
#     icon="🚗",
# )

# family_page = st.Page(
#     "Family_Chat.py",
#     title="Family Access",
#     icon="👥",
# )

# pg = st.navigation(
#     [driver_page, family_page],
#     position="hidden",
# )



# # ============================================================
# # SESSION STATE
# # ============================================================

# if "authenticated" not in st.session_state:
#     st.session_state.authenticated = False


# # ============================================================
# # GLOBAL CSS
# # ============================================================

# st.html(
#     """
#     <style>

#     @import url(
#         'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
#     );

#     html,
#     body,
#     [class*="css"] {
#         font-family: "Inter", sans-serif;
#     }

#     #MainMenu,
#     header,
#     footer {
#         visibility: hidden;
#     }

#     .block-container {
#         max-width: 1180px;
#         padding: 28px 24px 40px 24px;
#     }


#     /* ======================================================
#        LOGIN
#        ====================================================== */

#     .login-wrapper {
#         min-height: 78vh;

#         display: flex;
#         align-items: center;
#         justify-content: center;

#         flex-direction: column;
#     }


#     .login-brand {
#         text-align: center;
#         margin-bottom: 24px;
#     }


#     .login-logo {

#         width: 64px;
#         height: 64px;

#         margin: 0 auto 14px;

#         border-radius: 18px;

#         display: flex;
#         align-items: center;
#         justify-content: center;

#         background: #111827;
#         color: white;

#         font-size: 28px;
#         font-weight: 800;
#     }


#     .login-title {

#         font-size: 32px;
#         font-weight: 800;

#         color: #111827;
#     }


#     .login-subtitle {

#         margin-top: 6px;

#         color: #6b7280;

#         font-size: 14px;
#     }


#     .login-card {

#         width: 100%;
#         max-width: 430px;

#         box-sizing: border-box;

#         padding: 30px;

#         border: 1px solid #e5e7eb;

#         border-radius: 20px;

#         background: #ffffff;

#         box-shadow:
#             0 12px 35px rgba(
#                 15,
#                 23,
#                 42,
#                 .08
#             );
#     }


#     .login-heading {

#         font-size: 22px;
#         font-weight: 700;

#         color: #111827;

#         text-align: center;
#     }


#     .login-description {

#         color: #6b7280;

#         font-size: 14px;

#         text-align: center;

#         margin: 7px 0 22px;
#     }


#     .security-note {

#         text-align: center;

#         color: #6b7280;

#         font-size: 12px;

#         margin-top: 18px;
#     }


#     /* ======================================================
#        NAVBAR
#        ====================================================== */

#     .navbar {

#         display: flex;

#         align-items: center;

#         justify-content: space-between;

#         gap: 20px;

#         padding: 8px 0 28px;
#     }


#     .brand-container {

#         display: flex;

#         align-items: center;

#         gap: 12px;

#         min-width: 0;
#     }


#     .brand-logo {

#         width: 42px;
#         height: 42px;

#         flex: 0 0 42px;

#         border-radius: 12px;

#         display: flex;

#         align-items: center;
#         justify-content: center;

#         background: #111827;

#         color: white;

#         font-size: 19px;

#         font-weight: 800;
#     }


#     .brand-name {

#         font-size: 20px;

#         font-weight: 800;

#         color: #111827;
#     }


#     .brand-caption {

#         font-size: 9px;

#         letter-spacing: 1.4px;

#         color: #9ca3af;

#         margin-top: 2px;
#     }


#     .system-active {

#         color: #15803d;

#         font-size: 13px;

#         font-weight: 600;

#         white-space: nowrap;
#     }


#     /* ======================================================
#        HERO
#        ====================================================== */

#     .hero {

#         position: relative;

#         overflow: hidden;

#         min-height: 280px;

#         box-sizing: border-box;

#         border-radius: 26px;

#         background: #111827;

#         padding: 48px;

#         margin-bottom: 40px;
#     }


#     .hero-content {

#         position: relative;

#         z-index: 2;

#         max-width: 650px;
#     }


#     .hero-badge {

#         color: #d1d5db;

#         font-size: 11px;

#         font-weight: 700;

#         letter-spacing: 1.5px;

#         margin-bottom: 18px;
#     }


#     .hero-title {

#         color: white;

#         font-size: 46px;

#         line-height: 1.05;

#         font-weight: 800;
#     }


#     .hero-description {

#         color: #d1d5db;

#         line-height: 1.7;

#         font-size: 15px;

#         margin-top: 20px;

#         max-width: 600px;
#     }


#     .hero-circle-one,
#     .hero-circle-two {

#         position: absolute;

#         border-radius: 50%;

#         pointer-events: none;
#     }


#     .hero-circle-one {

#         width: 300px;
#         height: 300px;

#         right: -100px;
#         top: -110px;

#         border:
#             1px solid rgba(
#                 255,
#                 255,
#                 255,
#                 .1
#             );
#     }


#     .hero-circle-two {

#         width: 220px;
#         height: 220px;

#         right: 80px;
#         bottom: -130px;

#         border:
#             1px solid rgba(
#                 255,
#                 255,
#                 255,
#                 .08
#             );
#     }


#     /* ======================================================
#        SECTIONS
#        ====================================================== */

#     .section-title {

#         font-size: 23px;

#         font-weight: 800;

#         color: #111827;

#         margin-bottom: 5px;
#     }


#     .section-description {

#         color: #6b7280;

#         margin-bottom: 20px;

#         font-size: 14px;
#     }


#     /* ======================================================
#        PORTAL CARDS
#        ====================================================== */

#     .portal-card {

#         width: 100%;

#         min-width: 0;

#         min-height: 190px;

#         box-sizing: border-box;

#         overflow-wrap: anywhere;

#         border: 1px solid #e5e7eb;

#         border-radius: 20px;

#         padding: 25px;

#         background: white;

#         margin-bottom: 12px;
#     }


#     .portal-icon {

#         font-size: 30px;

#         line-height: 1;
#     }


#     .portal-title {

#         font-size: 20px;

#         font-weight: 800;

#         margin-top: 12px;

#         color: #111827;
#     }


#     .portal-description {

#         color: #6b7280;

#         font-size: 14px;

#         line-height: 1.65;

#         margin-top: 8px;

#         overflow-wrap: anywhere;
#     }


#     /* ======================================================
#        SECURITY
#        ====================================================== */

#     .security-card {

#         margin-top: 25px;

#         padding: 22px;

#         box-sizing: border-box;

#         border-radius: 18px;

#         background: #f8fafc;

#         border: 1px solid #e5e7eb;
#     }


#     .security-title {

#         font-size: 16px;

#         font-weight: 700;

#         color: #111827;
#     }


#     .security-description {

#         color: #6b7280;

#         font-size: 13px;

#         line-height: 1.6;

#         margin-top: 7px;
#     }


#     /* ======================================================
#        FOOTER
#        ====================================================== */

#     .footer {

#         margin-top: 50px;

#         padding-top: 20px;

#         border-top:
#             1px solid #e5e7eb;

#         color: #9ca3af;

#         font-size: 12px;

#         display: flex;

#         justify-content: space-between;

#         gap: 20px;
#     }


#     /* ======================================================
#        MOBILE
#        ====================================================== */

#     @media (max-width: 700px) {

#         .block-container {

#             padding-left: 16px;

#             padding-right: 16px;
#         }


#         .hero {

#             padding: 30px;

#             min-height: 250px;
#         }


#         .hero-title {

#             font-size: 34px;
#         }


#         .navbar,
#         .footer {

#             align-items: flex-start;

#             flex-direction: column;
#         }


#         .system-active {

#             margin-left: 54px;
#         }

#     }

#     </style>
#     """
# )


# # ============================================================
# # LOGIN SCREEN
# # ============================================================

# if not st.session_state.authenticated:

#     st.html(
#         """
#         <div class="login-wrapper">

#             <div class="login-brand">

#                 <div class="login-logo">
#                     G
#                 </div>

#                 <div class="login-title">
#                     Guardrive
#                 </div>

#                 <div class="login-subtitle">
#                     Private location sharing platform
#                 </div>

#             </div>


#             <div class="login-card">

#                 <div class="login-heading">
#                     Welcome back
#                 </div>

#                 <div class="login-description">
#                     Sign in to access the Guardrive platform.
#                 </div>

#             </div>

#         </div>
#         """
#     )


#     password = st.text_input(
#         "Password",
#         type="password",
#         placeholder="Enter your password",
#         key="login_password",
#     )


#     if st.button(
#         "Sign in to Guardrive",
#         type="primary",
#         use_container_width=True,
#     ):

#         if password == APP_PASSWORD:

#             st.session_state.authenticated = True

#             st.rerun()

#         else:

#             st.error(
#                 "Incorrect password. Please try again."
#             )


#     st.html(
#         """
#         <div class="security-note">
#             🔒 Protected access · Guardrive
#         </div>
#         """
#     )


#     st.stop()


# # ============================================================
# # NAVIGATION BAR
# # ============================================================

# nav_left, nav_right = st.columns(
#     [6, 1],
#     vertical_alignment="center"
# )


# with nav_left:

#     st.html(
#         """
#         <div class="navbar">

#             <div class="brand-container">

#                 <div class="brand-logo">
#                     G
#                 </div>

#                 <div>

#                     <div class="brand-name">
#                         Guardrive
#                     </div>

#                     <div class="brand-caption">
#                         PRIVATE LOCATION SHARING
#                     </div>

#                 </div>

#             </div>


#             <div class="system-active">
#                 ● System Active
#             </div>

#         </div>
#         """
#     )


# with nav_right:

#     if st.button(
#         "Sign out",
#         use_container_width=True
#     ):

#         # Completely logout from Guardrive
#         st.session_state.clear()

#         st.rerun()


# # ============================================================
# # HERO
# # ============================================================

# st.html(
#     """
#     <div class="hero">

#         <div class="hero-circle-one"></div>

#         <div class="hero-circle-two"></div>


#         <div class="hero-content">

#             <div class="hero-badge">
#                 🛡 LOCATION PROTECTION
#             </div>


#             <div class="hero-title">

#                 Stay connected.<br>

#                 Stay in control.

#             </div>


#             <div class="hero-description">

#                 Guardrive gives drivers complete control over
#                 location sharing. Approve access requests,
#                 control sharing duration and decide who can
#                 access your location.

#             </div>

#         </div>

#     </div>
#     """
# )


# # ============================================================
# # PORTAL SECTION
# # ============================================================

# st.html(
#     """
#     <div class="section-title">
#         Choose your experience
#     </div>

#     <div class="section-description">
#         Select a portal to continue.
#     </div>
#     """
# )


# # ============================================================
# # PORTALS
# # ============================================================

# driver_col, family_col = st.columns(
#     2,
#     gap="large"
# )


# # ============================================================
# # DRIVER PORTAL
# # ============================================================

# with driver_col:

#     st.html(
#         """
#         <div class="portal-card">

#             <div class="portal-icon">
#                 🚗
#             </div>

#             <div class="portal-title">
#                 Driver Portal
#             </div>

#             <div class="portal-description">

#                 Manage location protection, start GPS tracking,
#                 review access requests and control who can
#                 access your location.

#             </div>

#         </div>
#         """
#     )
#     if st.button(
#                 "Open Driver Portal",
#                 use_container_width=True,
#                 type="primary",
#                 key="open_driver",
#             ):
#                 pg.switch_to(driver_page)





# # ============================================================
# # FAMILY ACCESS
# # ============================================================

# with family_col:

#     st.html(
#         """
#         <div class="portal-card">

#             <div class="portal-icon">
#                 👥
#             </div>

#             <div class="portal-title">
#                 Family Access
#             </div>

#             <div class="portal-description">

#                 Request authorized access to a driver's
#                 location and view the latest available
#                 position.

#             </div>

#         </div>
#         """
#     )
#     if st.button(
#                 "Open Family Access",
#                 use_container_width=True,
#                 key="open_family",
#             ):
#                 pg.switch_to(family_page)


#     # if st.button(
#     #             "Open Family Access",
#     #             use_container_width=True,
#     #             key="open_family",
#     #         ):
            
#     #             st.switch_page("Family_Chat")


# # ============================================================
# # PRIVACY
# # ============================================================

# st.html(
#     """
#     <div class="security-card">

#         <div class="security-title">
#             🔐 Privacy by design
#         </div>

#         <div class="security-description">

#             A phone number alone never exposes a driver's
#             location. Every access request requires explicit
#             driver approval and can be revoked.

#         </div>

#     </div>
#     """
# )


# # ============================================================
# # FOOTER
# # ============================================================

# st.html(
#     """
#     <div class="footer">

#         <div>
#             Guardrive © 2026
#         </div>

#         <div>
#             Private location sharing · Prototype
#         </div>

#     </div>
#     """
# )



















import streamlit as st


# ============================================================
# APP CONFIG
# ============================================================

APP_PASSWORD = "11111"

st.set_page_config(
    page_title="Guardrive",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# NAVIGATION PAGES
# ============================================================

driver_page = st.Page(
    "Driver.py",
    title="Driver Portal",
    icon="🚗",
)

family_page = st.Page(
    "Family_Chat.py",
    title="Family Access",
    icon="👥",
)

# ============================================================
# SESSION STATE
# ============================================================

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False





# ============================================================
# GLOBAL CSS
# ============================================================

st.html(
    """
    <style>

    @import url(
        'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
    );

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
        max-width: 1180px;
        padding: 28px 24px 40px 24px;
    }

    .login-wrapper {
        min-height: 78vh;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
    }

    .login-brand {
        text-align: center;
        margin-bottom: 24px;
    }

    .login-logo {
        width: 64px;
        height: 64px;
        margin: 0 auto 14px;
        border-radius: 18px;

        display: flex;
        align-items: center;
        justify-content: center;

        background: #111827;
        color: #ffffff;

        font-size: 28px;
        font-weight: 800;
    }

    .login-title {
        font-size: 32px;
        font-weight: 800;
        color: #111827;
    }

    .login-subtitle {
        margin-top: 6px;
        color: #6b7280;
        font-size: 14px;
    }

    .login-card {
        width: 100%;
        max-width: 430px;
        box-sizing: border-box;
        padding: 30px;

        border: 1px solid #e5e7eb;
        border-radius: 20px;

        background: #ffffff;

        box-shadow:
            0 12px 35px rgba(15, 23, 42, .08);
    }

    .login-heading {
        font-size: 22px;
        font-weight: 700;
        color: #111827;
        text-align: center;
    }

    .login-description {
        color: #6b7280;
        font-size: 14px;
        text-align: center;
        margin: 7px 0 22px;
    }

    .security-note {
        text-align: center;
        color: #6b7280;
        font-size: 12px;
        margin-top: 18px;
    }

    .navbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 20px;
        padding: 8px 0 28px;
    }

    .brand-container {
        display: flex;
        align-items: center;
        gap: 12px;
        min-width: 0;
    }

    .brand-logo {
        width: 42px;
        height: 42px;
        flex: 0 0 42px;
        border-radius: 12px;

        display: flex;
        align-items: center;
        justify-content: center;

        background: #111827;
        color: #ffffff;

        font-size: 19px;
        font-weight: 800;
    }

    .brand-name {
        font-size: 20px;
        font-weight: 800;
        color: #111827;
    }

    .brand-caption {
        font-size: 9px;
        letter-spacing: 1.4px;
        color: #9ca3af;
        margin-top: 2px;
    }

    .system-active {
        color: #15803d;
        font-size: 13px;
        font-weight: 600;
        white-space: nowrap;
    }

    .hero {
        position: relative;
        overflow: hidden;

        min-height: 280px;
        box-sizing: border-box;

        border-radius: 26px;
        background: #111827;

        padding: 48px;
        margin-bottom: 40px;
    }

    .hero-content {
        position: relative;
        z-index: 2;
        max-width: 650px;
    }

    .hero-badge {
        color: #d1d5db;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1.5px;
        margin-bottom: 18px;
    }

    .hero-title {
        color: #ffffff;
        font-size: 46px;
        line-height: 1.05;
        font-weight: 800;
    }

    .hero-description {
        color: #d1d5db;
        line-height: 1.7;
        font-size: 15px;
        margin-top: 20px;
        max-width: 600px;
    }

    .hero-circle-one,
    .hero-circle-two {
        position: absolute;
        border-radius: 50%;
        pointer-events: none;
    }

    .hero-circle-one {
        width: 300px;
        height: 300px;
        right: -100px;
        top: -110px;

        border: 1px solid rgba(255, 255, 255, .1);
    }

    .hero-circle-two {
        width: 220px;
        height: 220px;
        right: 80px;
        bottom: -130px;

        border: 1px solid rgba(255, 255, 255, .08);
    }

    .section-title {
        font-size: 23px;
        font-weight: 800;
        color: #111827;
        margin-bottom: 5px;
    }

    .section-description {
        color: #6b7280;
        margin-bottom: 20px;
        font-size: 14px;
    }

    .portal-card {
        width: 100%;
        min-width: 0;
        min-height: 190px;

        box-sizing: border-box;
        overflow-wrap: anywhere;

        border: 1px solid #e5e7eb;
        border-radius: 20px;

        padding: 25px;

        background: #ffffff;

        margin-bottom: 12px;
    }

    .portal-icon {
        font-size: 30px;
        line-height: 1;
    }

    .portal-title {
        font-size: 20px;
        font-weight: 800;
        margin-top: 12px;
        color: #111827;
    }

    .portal-description {
        color: #6b7280;
        font-size: 14px;
        line-height: 1.65;
        margin-top: 8px;

        overflow-wrap: anywhere;
    }

    .security-card {
        margin-top: 25px;
        padding: 22px;

        box-sizing: border-box;

        border-radius: 18px;

        background: #f8fafc;

        border: 1px solid #e5e7eb;
    }

    .security-title {
        font-size: 16px;
        font-weight: 700;
        color: #111827;
    }

    .security-description {
        color: #6b7280;
        font-size: 13px;
        line-height: 1.6;
        margin-top: 7px;
    }

    .footer {
        margin-top: 50px;
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

        .hero {
            padding: 30px;
            min-height: 250px;
        }

        .hero-title {
            font-size: 34px;
        }

        .navbar,
        .footer {
            align-items: flex-start;
            flex-direction: column;
        }

        .system-active {
            margin-left: 54px;
        }

    }

    </style>
    """
)


# ============================================================
# HOME PAGE
# ============================================================

def home():

    # --------------------------------------------------------
    # LOGIN
    # --------------------------------------------------------

    if not st.session_state.authenticated:

        st.html(
            """
            <div class="login-wrapper">

                <div class="login-brand">

                    <div class="login-logo">
                        G
                    </div>

                    <div class="login-title">
                        Guardrive
                    </div>

                    <div class="login-subtitle">
                        Private location sharing platform
                    </div>

                </div>

                <div class="login-card">

                    <div class="login-heading">
                        Welcome back
                    </div>

                    <div class="login-description">
                        Sign in to access the Guardrive platform.
                    </div>

                </div>

            </div>
            """
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password",
            key="login_password",
        )

        if st.button(
            "Sign in to Guardrive",
            type="primary",
            use_container_width=True,
            key="login_button",
        ):

            if password == APP_PASSWORD:

                st.session_state.authenticated = True

                st.rerun()

            else:

                st.error(
                    "Incorrect password. Please try again."
                )

        st.html(
            """
            <div class="security-note">
                🔒 Protected access · Guardrive
            </div>
            """
        )

        return

    # --------------------------------------------------------
    # NAVBAR
    # --------------------------------------------------------

    nav_left, nav_right = st.columns(
        [6, 1],
        vertical_alignment="center"
    )

    with nav_left:

        st.html(
            """
            <div class="navbar">

                <div class="brand-container">

                    <div class="brand-logo">
                        G
                    </div>

                    <div>

                        <div class="brand-name">
                            Guardrive
                        </div>

                        <div class="brand-caption">
                            PRIVATE LOCATION SHARING
                        </div>

                    </div>

                </div>

                <div class="system-active">
                    ● System Active
                </div>

            </div>
            """
        )

    with nav_right:

        if st.button(
            "Sign out",
            use_container_width=True,
            key="home_signout",
        ):

            st.session_state.clear()

            st.rerun()

    # --------------------------------------------------------
    # HERO
    # --------------------------------------------------------

    st.html(
        """
        <div class="hero">

            <div class="hero-circle-one"></div>

            <div class="hero-circle-two"></div>

            <div class="hero-content">

                <div class="hero-badge">
                    🛡 LOCATION PROTECTION
                </div>

                <div class="hero-title">
                    Stay connected.<br>
                    Stay in control.
                </div>

                <div class="hero-description">

                    Guardrive gives drivers complete control over
                    location sharing. Approve access requests,
                    control sharing duration and decide who can
                    access your location.

                </div>

            </div>

        </div>
        """
    )

    # --------------------------------------------------------
    # SECTION
    # --------------------------------------------------------

    st.html(
        """
        <div class="section-title">
            Choose your experience
        </div>

        <div class="section-description">
            Select a portal to continue.
        </div>
        """
    )

    # --------------------------------------------------------
    # PORTALS
    # --------------------------------------------------------

    driver_col, family_col = st.columns(
        2,
        gap="large"
    )

    # --------------------------------------------------------
    # DRIVER
    # --------------------------------------------------------

    with driver_col:

        st.html(
            """
            <div class="portal-card">

                <div class="portal-icon">
                    🚗
                </div>

                <div class="portal-title">
                    Driver Portal
                </div>

                <div class="portal-description">

                    Manage location protection, start GPS tracking,
                    review access requests and control who can
                    access your location.

                </div>

            </div>
            """
        )

        if st.button(
            "Open Driver Portal",
            use_container_width=True,
            type="primary",
            key="open_driver",
        ):

            st.switch_page(driver_page)

    # --------------------------------------------------------
    # FAMILY
    # --------------------------------------------------------

    with family_col:

        st.html(
            """
            <div class="portal-card">

                <div class="portal-icon">
                    👥
                </div>

                <div class="portal-title">
                    Family Access
                </div>

                <div class="portal-description">

                    Request authorized access to a driver's
                    location and view the latest available
                    position.

                </div>

            </div>
            """
        )

        if st.button(
            "Open Family Access",
            use_container_width=True,
            key="open_family",
        ):

            st.switch_page(family_page)

    # --------------------------------------------------------
    # PRIVACY
    # --------------------------------------------------------

    st.html(
        """
        <div class="security-card">

            <div class="security-title">
                🔐 Privacy by design
            </div>

            <div class="security-description">

                A phone number alone never exposes a driver's
                location. Every access request requires explicit
                driver approval and can be revoked.

            </div>

        </div>
        """
    )

    # --------------------------------------------------------
    # FOOTER
    # --------------------------------------------------------

    st.html(
        """
        <div class="footer">

            <div>
                Guardrive © 2026
            </div>

            <div>
                Private location sharing · Prototype
            </div>

        </div>
        """
    )


# ============================================================
# STREAMLIT NAVIGATION
# ============================================================

home_page = st.Page(
    home,
    title="Guardrive",
    icon="🛡️",
    default=True,
)


pg = st.navigation(
    [
        home_page,
        driver_page,
        family_page,
    ],
    position="hidden",
)


# ============================================================
# RUN CURRENT PAGE
# ============================================================

pg.run()

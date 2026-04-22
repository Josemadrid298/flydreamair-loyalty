import streamlit as st
from pathlib import Path
import json

# ====================== SESSION STATE ======================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "current_user" not in st.session_state:
    st.session_state.current_user = None

# ====================== HELPER FUNCTIONS ======================
def load_users():
    data_file = Path("data/users.json")
    if data_file.exists():
        try:
            with open(data_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            st.error(f"Error reading users.json: {e}")
            return {}
    return {}

# ====================== PAGE CONFIG ======================
st.set_page_config(
    page_title="FlyDreamAir Loyalty",
    page_icon="✈️",
    layout="wide"
)

# ====================== ROUTING ======================
if not st.session_state.logged_in:
    # ---------- LOGIN SCREEN ----------
    st.title("✈️ Welcome to FlyDreamAir")
    st.subheader("Frequent Flyer Loyalty Program")

    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(
            "https://via.placeholder.com/500x300/0066cc/ffffff?text=✈️+FlyDreamAir",
            use_container_width=True
        )
    with col2:
        st.markdown("### Login to your account")
        username = st.text_input("Username").strip()
        password = st.text_input("Password", type="password").strip()

        if st.button("Login", type="primary", use_container_width=True):
            users = load_users()
            if username in users and users[username].get("password") == password:
                st.session_state.logged_in = True
                st.session_state.current_user = users[username].copy()
                st.success(f"✅ Welcome back, {users[username]['name']}!")
                st.rerun()
            else:
                st.error("❌ Invalid username or password.")

        st.caption("**Demo:** `alice` / `password123`")

else:
    # ---------- LOGGED-IN SHELL ----------
    user = st.session_state.current_user

    # Sidebar: user info + logout (rendered ONCE here, never in page files)
    st.sidebar.success(f"👤 {user.get('name', 'User')}")
    st.sidebar.markdown(f"**Points:** {user.get('points', 0):,}")
    st.sidebar.markdown(f"**Tier:** {user.get('tier', 'Bronze')}")
    st.sidebar.divider()

    if st.sidebar.button("Logout", key="logout_button", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.rerun()

    st.sidebar.divider()

    # Navigation — points to separate page files only, NOT app.py
    pages = [
        st.Page("pages/dashboard.py",      title="Dashboard",       icon="🏠", default=True),
        st.Page("pages/earn_points.py",    title="Earn Points",     icon="✈️"),
        st.Page("pages/redeem_points.py",  title="Redeem Rewards",  icon="🎁"),
        st.Page("pages/my_tier.py",        title="My Tier",         icon="🏆"),
        st.Page("pages/history.py",        title="History",         icon="📜"),
    ]

    pg = st.navigation(pages, position="sidebar")
    pg.run()
import streamlit as st
from utils import load_users

def show():
    if "current_user" not in st.session_state or st.session_state.current_user is None:
        st.error("Please login first!")
        st.stop()

    user = st.session_state.current_user
    st.title("🏆 My Tier Status")

    tiers = {
        "Bronze": {"min": 0, "benefits": "1× points"},
        "Silver": {"min": 10000, "benefits": "1.5× points + lounge access"},
        "Gold": {"min": 50000, "benefits": "2× points + free upgrades"},
        "Platinum": {"min": 100000, "benefits": "3× points + priority boarding"}
    }

    current = user.get("tier", "Bronze")
    st.metric("Your Current Tier", current)

    st.subheader("Tier Benefits")
    for tier, info in tiers.items():
        emoji = "✅" if tier == current else "🔒"
        st.write(f"{emoji} **{tier}** — {info['benefits']}")

    st.progress(min(user.get("points", 0) / 100000, 1.0))
    st.caption("Progress toward Platinum")

show()

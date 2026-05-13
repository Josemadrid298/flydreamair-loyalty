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

    # progress is measured against the *next* tier, not always Platinum
    next_tier = {"Bronze": "Silver", "Silver": "Gold", "Gold": "Platinum", "Platinum": None}.get(current)
    points = user.get("points", 0)
    if next_tier:
        target = tiers[next_tier]["min"]
        floor = tiers[current]["min"]
        pct = max(0.0, min((points - floor) / (target - floor), 1.0))
        st.progress(pct)
        st.caption(f"Progress toward {next_tier} ({points:,} / {target:,} pts)")
    else:
        st.progress(1.0)
        st.caption("You're at the top tier — Platinum")

show()

import streamlit as st
from utils import load_users

def show():
    if "current_user" not in st.session_state or st.session_state.current_user is None:
        st.error("Please login first!")
        st.stop()

    user = st.session_state.current_user
    st.title("📜 Transaction History")

    transactions = user.get("transactions", [])

    if transactions:
        for tx in reversed(transactions):
            sign = "🟢 +" if tx["points"] > 0 else "🔴 "
            st.write(f"{tx['date']} — {sign}{tx['points']} pts — {tx['description']}")
    else:
        st.info("No transactions yet.")

    st.caption(f"Total points: **{user.get('points', 0):,}**")

show()
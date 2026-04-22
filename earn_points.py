import streamlit as st
from utils import load_users, save_users, calculate_points, add_transaction

def show():
    if "current_user" not in st.session_state or st.session_state.current_user is None:
        st.error("Please login first!")
        st.stop()

    user = st.session_state.current_user
    st.title("✈️ Earn Points")

    st.subheader("How would you like to earn points?")

    option = st.radio("Choose activity:", ["Flight", "Partner Purchase"], horizontal=True)

    if option == "Flight":
        distance = st.number_input("Flight distance (km)", min_value=100, value=1200)
        base = st.number_input("Base fare ($)", min_value=50, value=350)
        points = calculate_points(base, user["tier"])
        st.info(f"✈️ You will earn **{points} points** ({user['tier']} member)")

        if st.button("Confirm Flight & Earn Points", type="primary", use_container_width=True):
            add_transaction(user, f"Flight ({distance}km)", points)
            users = load_users()
            users[st.session_state.current_user["name"].lower().split()[0]] = user  # simple key match
            save_users(users)
            st.success(f"✅ {points} points added! New balance: {user['points']:,}")
            st.rerun()

    else:  # Partner Purchase
        amount = st.number_input("Purchase amount ($)", min_value=10, value=120)
        points = calculate_points(amount, user["tier"])
        st.info(f"🛍️ You will earn **{points} points**")

        if st.button("Confirm Purchase & Earn Points", type="primary", use_container_width=True):
            add_transaction(user, "Partner purchase", points)
            users = load_users()
            users[st.session_state.current_user["name"].lower().split()[0]] = user
            save_users(users)
            st.success(f"✅ {points} points added! New balance: {user['points']:,}")
            st.rerun()

    st.caption("Points are calculated based on your current tier multiplier.")

show()
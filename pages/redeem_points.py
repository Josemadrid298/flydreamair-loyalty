import streamlit as st
from utils import load_users, save_users, add_transaction

def show():
    if "current_user" not in st.session_state or st.session_state.current_user is None:
        st.error("Please login first!")
        st.stop()

    user = st.session_state.current_user
    st.title("🎁 Redeem Rewards")

    rewards = {
        "Free Domestic Flight Voucher": 15000,
        "Lounge Access (1 visit)": 8000,
        "Seat Upgrade to Business": 25000,
        "Hotel Stay Voucher": 12000,
        "Gift Card $100": 10000,
        "Extra Baggage Allowance": 5000
    }

    current_points = user.get("points", 0)
    st.write("Current points:", f"**{current_points:,}**")

    cols = st.columns(2)
    for idx, (reward, cost) in enumerate(rewards.items()):
        with cols[idx % 2]:
            st.subheader(reward)
            st.caption(f"Cost: {cost:,} points")

            can_afford = current_points >= cost

            if not can_afford:
                st.caption(f"⚠️ You need {cost - current_points:,} more points")

            if st.button(
                f"Redeem {reward.split()[0]}",
                key=reward,
                use_container_width=True,
                disabled=not can_afford        # greys out the button if unaffordable
            ):
                # Double-check balance at time of click (safety net)
                if user.get("points", 0) < cost:
                    st.error(f"❌ Not enough points! You need {cost:,} pts but only have {user['points']:,} pts.")
                else:
                    user["points"] -= cost
                    add_transaction(user, f"Redeemed: {reward}", -cost)
                    users = load_users()
                    users[st.session_state.current_user["name"].lower().split()[0]] = user
                    save_users(users)
                    st.session_state.current_user = user  # keep session state in sync
                    st.success(f"🎉 {reward} redeemed successfully!")
                    st.rerun()

show()

import streamlit as st

if not st.session_state.get("logged_in"):
    st.warning("Please log in first.")
    st.stop()

user = st.session_state.current_user

# ====================== TIER CONFIG ======================
TIER_CONFIG = {
    "Bronze":   {"next": "Silver",   "target": 10_000,  "color": "#CD7F32", "emoji": "🥉"},
    "Silver":   {"next": "Gold",     "target": 50_000,  "color": "#C0C0C0", "emoji": "🥈"},
    "Gold":     {"next": "Platinum", "target": 100_000, "color": "#FFD700", "emoji": "🥇"},
    "Platinum": {"next": None,       "target": None,    "color": "#E5E4E2", "emoji": "💎"},
}

points   = user.get("points", 0)
tier     = user.get("tier", "Bronze")
name     = user.get("name", "Traveller")
t_cfg    = TIER_CONFIG.get(tier, TIER_CONFIG["Bronze"])
history  = user.get("history", [])

# ====================== HEADER ======================
st.title(f"👋 Welcome back, {name}!")

col1, col2, col3 = st.columns(3)
col1.metric("Current Points", f"{points:,}")
col2.metric("Current Tier", tier)
col3.metric("Member Since", user.get("member_since", "—"))

st.divider()

# ====================== TIER PROGRESS ======================
st.markdown("### 🎯 Progress to Next Tier")

if t_cfg["next"]:
    pct = max(0.0, min(points / t_cfg["target"], 1.0))
    needed  = max(t_cfg["target"] - points, 0)
    st.progress(pct)
    pcol1, pcol2, pcol3 = st.columns(3)
    pcol1.markdown(f"**{points:,}** pts earned")
    pcol2.markdown(f"**{needed:,}** pts to {t_cfg['next']} {TIER_CONFIG[t_cfg['next']]['emoji']}")
    pcol3.markdown(f"**{pct*100:.0f}%** complete")
else:
    st.success("💎 You've reached Platinum — the highest tier! Enjoy your exclusive benefits.")

st.divider()

# ====================== TIER BENEFITS SUMMARY ======================
st.markdown("### 🏅 Your Tier Benefits")

BENEFITS = {
    "Bronze":   ["5% bonus points on flights", "Birthday bonus points", "Member newsletter"],
    "Silver":   ["10% bonus points on flights", "Priority check-in", "1 free lounge pass/year", "Birthday double points"],
    "Gold":     ["20% bonus points on flights", "Unlimited lounge access", "Priority boarding", "Free seat upgrades (when available)", "Dedicated support line"],
    "Platinum": ["50% bonus points on all spend", "Guaranteed upgrades", "Unlimited guest lounge passes", "Personal travel concierge", "Annual gift (5,000 bonus pts)"],
}

benefits = BENEFITS.get(tier, [])
b_cols = st.columns(len(benefits))
for i, benefit in enumerate(benefits):
    b_cols[i].success(f"✅ {benefit}")

st.divider()

# ====================== POINTS SUMMARY CARDS ======================
st.markdown("### 💳 Points Snapshot")

earned_total  = sum(h["points"] for h in history if h.get("points", 0) > 0)
redeemed_total = abs(sum(h["points"] for h in history if h.get("points", 0) < 0))
txn_count     = len(history)

sc1, sc2, sc3, sc4 = st.columns(4)
sc1.metric("Lifetime Earned",   f"{earned_total:,} pts")
sc2.metric("Total Redeemed",    f"{redeemed_total:,} pts")
sc3.metric("Current Balance",   f"{points:,} pts")
sc4.metric("Total Transactions", txn_count)

st.divider()

# ====================== QUICK ACTIONS ======================
st.markdown("### 🚀 Quick Actions")

qa1, qa2, qa3, qa4 = st.columns(4)
if qa1.button("✈️ Earn Points",    use_container_width=True, type="primary"):
    st.switch_page("pages/earn_points.py")
if qa2.button("🎁 Browse Rewards", use_container_width=True):
    st.switch_page("pages/redeem_points.py")
if qa3.button("🏆 My Tier",        use_container_width=True):
    st.switch_page("pages/my_tier.py")
if qa4.button("📜 View History",   use_container_width=True):
    st.switch_page("pages/history.py")

st.divider()

# ====================== RECENT ACTIVITY ======================
st.markdown("### 📋 Recent Activity")

if history:
    recent = sorted(history, key=lambda x: x.get("date", ""), reverse=True)[:5]
    for entry in recent:
        pts   = entry.get("points", 0)
        date  = entry.get("date", "Unknown date")
        desc  = entry.get("description", "Transaction")
        color = "🟢" if pts > 0 else "🔴"
        sign  = "+" if pts > 0 else ""
        st.markdown(f"{color} **{date}** — {desc} → **{sign}{pts:,} pts**")
else:
    st.info("No activity yet. Earn your first points by logging a flight!")

st.divider()

# ====================== TIPS & OFFERS ======================
st.markdown("### 💡 Tips to Earn Faster")

tip1, tip2, tip3 = st.columns(3)
with tip1:
    st.info("✈️ **Book Direct**\nEarn 2× points when you book flights directly through FlyDreamAir.")
with tip2:
    st.info("🏨 **Partner Hotels**\nStay at partner hotels to earn bonus points on every night.")
with tip3:
    st.info("💳 **Co-branded Card**\nUse the FlyDreamAir Visa to earn 3 pts per $1 on everyday spend.")

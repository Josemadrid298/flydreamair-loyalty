# ✈️ FlyDreamAir Loyalty Program

A web-based frequent flyer loyalty program built with Python and Streamlit. Members can track points, redeem rewards, view their tier status, and manage their flight history — all through a clean, interactive dashboard.

> Login with the demo account below to explore the app.

---

Features:

- Secure Login — Session-based authentication with user accounts stored in JSON
- Dashboard — Points balance, tier progress, recent activity, and quick actions
- Earn Points — Log flights and partner activities to accumulate points
- Redeem Rewards — Browse and redeem rewards (flight vouchers, upgrades, gift cards, and more)
- My Tier — View current tier (Bronze → Silver → Gold → Platinum) and benefits
- Transaction History — Full log of all points earned and redeemed

---

Project Structure:

```
flydreamair-loyalty/
├── app.py                  # Main entry point — login screen + navigation shell
├── utils.py                # Shared helper functions (load/save users, transactions)
├── requirements.txt        # Python dependencies
├── data/
│   └── users.json          # User accounts and data (mock data included)
└── pages/
    ├── dashboard.py        # Dashboard page
    ├── earn_points.py      # Earn points page
    ├── redeem_points.py    # Redeem rewards page
    ├── my_tier.py          # Tier status page
    └── history.py          # Transaction history page
```

---

Setup & Installation:

1. Clone the repository

```bash
git clone https://github.com/Josemadrid298/flydreamair-loyalty.git
cd flydreamair-loyalty
```

2. (Optional) Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the app

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

---

Demo Account:

| Username | Password    |
|----------|-------------|
| `alice`  | `password123` |

---

Tier System:

| Tier     | Points Required | Key Benefits                              |
|----------|----------------|-------------------------------------------|
| 🥉 Bronze   | 0 – 9,999      | 5% bonus points, birthday bonus           |
| 🥈 Silver   | 10,000 – 49,999 | 10% bonus, priority check-in, lounge pass |
| 🥇 Gold     | 50,000 – 99,999 | 20% bonus, unlimited lounge, upgrades     |
| 💎 Platinum | 100,000+        | 50% bonus, concierge, guaranteed upgrades |

---

Built With:

- [Python 3.x](https://www.python.org/)
- [Streamlit](https://streamlit.io/) — UI framework
- JSON — lightweight local data storage

---

Contributors:

- [@Josemadrid298](https://github.com/Josemadrid298)

---

*Built as part of an IT Project Management group project.*

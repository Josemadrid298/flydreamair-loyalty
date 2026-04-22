import json
from pathlib import Path
from datetime import datetime

def load_users():
    data_file = Path("data/users.json")
    if data_file.exists():
        try:
            with open(data_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_users(users):
    Path("data").mkdir(exist_ok=True)
    try:
        with open("data/users.json", "w", encoding="utf-8") as f:
            json.dump(users, f, indent=4)
    except Exception as e:
        print(f"Error saving: {e}")

def calculate_points(base_amount: float, tier: str) -> int:
    """Calculate points based on amount and tier multiplier"""
    multipliers = {"Bronze": 1.0, "Silver": 1.5, "Gold": 2.0, "Platinum": 3.0}
    multiplier = multipliers.get(tier, 1.0)
    return int(base_amount * multiplier)

def add_transaction(user_data: dict, description: str, points: int):
    """Add a transaction and update points"""
    now = datetime.now().strftime("%Y-%m-%d")
    if "transactions" not in user_data:
        user_data["transactions"] = []
    user_data["transactions"].append({
        "date": now,
        "description": description,
        "points": points
    })
    user_data["points"] = user_data.get("points", 0) + points
    # Auto-check tier upgrade
    if user_data["points"] >= 100000:
        user_data["tier"] = "Platinum"
    elif user_data["points"] >= 50000:
        user_data["tier"] = "Gold"
    elif user_data["points"] >= 10000:
        user_data["tier"] = "Silver"
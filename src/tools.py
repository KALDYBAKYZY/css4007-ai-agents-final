import json
from pathlib import Path

from validators import validate_category, validate_month

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def load_json(file_name):
    with open(DATA_DIR / file_name, encoding="utf-8") as file:
        return json.load(file)


def normalize(text):
    if isinstance(text, str):
        return text.strip().lower()
    return text


def get_transactions(month, category=None):
    month = normalize(month)
    if not validate_month(month):
        return {"error": f"Invalid month: {month}. Use the format YYYY-MM."}

    if category is not None:
        category = normalize(category)
        if not validate_category(category):
            return {"error": f"Unknown category: {category}."}

    try:
        transactions = load_json("transactions.json")
    except (OSError, json.JSONDecodeError):
        return {"error": "Could not read the transactions data."}

    month_items = [t for t in transactions if t["date"].startswith(month)]
    if not month_items:
        return {"error": f"No data for {month}."}

    if category is not None:
        month_items = [t for t in month_items if t["category"] == category]

    return {
        "month": month,
        "category": category,
        "count": len(month_items),
        "transactions": month_items,
    }
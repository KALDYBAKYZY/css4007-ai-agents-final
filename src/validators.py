import re

CATEGORIES = [
    "food",
    "transport",
    "rent",
    "utilities",
    "phone",
    "entertainment",
    "subscriptions",
    "education",
    "shopping",
    "health",
]

MONTH_PATTERN = re.compile(r"\d{4}-(0[1-9]|1[0-2])")


def validate_month(month):
    if not isinstance(month, str):
        return False
    return MONTH_PATTERN.fullmatch(month) is not None


def validate_category(category):
    if not isinstance(category, str):
        return False
    return category in CATEGORIES
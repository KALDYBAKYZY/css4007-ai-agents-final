from tools import calculate_total, get_budget

def test_calculate_total_food_october():
    result = calculate_total("food", "2026-10")
    assert result == {
        "category": "food",
        "month": "2026-10",
        "total": 51100,
        "transaction_count": 12,
    }

def test_get_budget_unknown_category():
    result = get_budget("pizza")
    assert "error" in result
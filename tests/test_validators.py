from validators import validate_category, validate_month

def test_validate_month_accepts_correct_month():
    assert validate_month("2026-10") is True

def test_validate_month_rejects_wrong_month():
    assert validate_month("2026-13") is False
    assert validate_month("2026-9") is False
    assert validate_month("October") is False
    assert validate_month(202610) is False

def test_validate_category():
    assert validate_category("food") is True
    assert validate_category("pizza") is False
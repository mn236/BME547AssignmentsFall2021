import pytest


@pytest.mark.parametrize("input_w, expected", [
    ("22 lb", 10),
    ("50 kg", 50),
    ("22.1 lb", 10),
    ("35.5 kg", 36),
    ("22 lbs", 10),
    ("22 lbS", 10),
    # ("too much", False),
    # ("22", False),
    ("22 KG", 22),
    ("22 Kg", 22),
    # ("22kg", 22),
    # ("64 g", False),
    # ("ten kg", False),
    ("-22 lb", -10)
])
def test_parse_weight_input(input_w, expected):
    from weight_entry import parse_weight_input
    answer = parse_weight_input(input_w)
    assert answer == expected

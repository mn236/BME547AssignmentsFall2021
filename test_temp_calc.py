import pytest


@pytest.mark.parametrize("input_temp, expected", [
    ([96, 96.5, 103.1, 98.7], True),
    ([96, 92.5, 100.0, 98.7], False)
])
def test_detect_fever(input_temp, expected):
    from temp_calc import detect_fever
    answer = detect_fever(input_temp)
    assert answer == expected

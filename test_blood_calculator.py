
def test_hdl_analysis_normal():
    from blood_calculator import hdl_analysis
    answer = hdl_analysis(60)
    expected = "Normal"
    assert answer == expected


def test_hdl_analysis_bl():
    from blood_calculator import hdl_analysis
    answer = hdl_analysis(45)
    expected = "Borderline Low"
    assert answer == expected


def test_hdl_analysis_low():
    from blood_calculator import hdl_analysis
    answer = hdl_analysis(15)
    expected = "Low"
    assert answer == expected


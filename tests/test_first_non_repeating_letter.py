from src.first_non_repeating_letter import first_non_repeating_letter


def test_first_non_repeat_returns_first_non_repeat_char():
    """tests the first non repeated cahr is returned"""
    string = "Hello"
    assert first_non_repeating_letter(string) == "H"


def test_return_T():
    """tests sTreSS returns T"""
    string = "sTreSS"
    assert first_non_repeating_letter(string) == "T"
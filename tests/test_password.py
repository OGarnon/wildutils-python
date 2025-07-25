# tests/test_password.py
from utils import password

def test_password_strength_levels():
    levels = [
        ("123", "Very Weak"),
        ("abcdefgh", "Weak"),
        ("abcd1234", "Fair"),
        ("Abcd1234", "Good"),
        ("Abcd1234!", "Strong")
    ]
    for pw, expected in levels:
        result = password.check_strength(pw)
        assert result == expected

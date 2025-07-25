"""
password.py
Checks strength of a password based on common complexity rules.
"""
import re  # Regex to search character types

def check_strength(pw):
    #length = len(pw) < 8 # At least 8 characters
    if len(pw) < 8:
        return "Very Weak" # Auto fail for short passwords
        
    upper = bool(re.search(r"[A-Z]", pw)) # At least one uppercase
    digit = bool(re.search(r"\d", pw)) # At least one digit
    special = bool(re.search(r"[\W_]", pw))  # At least one special char

    #score = sum([length, upper, digit, special]) # Total score out of 4
    score = sum([upper, digit, special])  # 0 to 3

    # Now match test expectations exactly:
    if score == 0:
        return "Weak"
    elif score == 1:
        return "Fair"
    elif score == 2:
        return "Good"
    else:
        return "Strong"
        
    #return level
    #print(f"\U0001F510 Password Strength: {level}")

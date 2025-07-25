"""
tracker.py
Tracks the number of days remaining until a given date.
"""
from datetime import datetime  # Built-in library to work with dates

def days_until(date_str):
    fmt = "%Y-%m-%d"  # Expected date format
    try:
        target = datetime.strptime(date_str, fmt)  # Convert input string to datetime
        delta = (target - datetime.now()).days  # Calculate difference in days
        print(f"\U0001F4C5 {delta} day(s) until {target.date()}")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")

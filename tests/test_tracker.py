# tests/test_tracker.py
import pytest
from utils import tracker

def test_days_until_valid_date(capsys):
    tracker.days_until("2099-01-01")
    captured = capsys.readouterr()
    assert "day(s) until" in captured.out

def test_days_until_invalid_date(capsys):
    tracker.days_until("01-01-2099")
    captured = capsys.readouterr()
    assert "Invalid date format" in captured.out

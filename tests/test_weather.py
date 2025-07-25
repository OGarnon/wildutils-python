# tests/test_weather.py
from utils import weather

def test_show_weather_output(capsys):
    weather.show_weather("Herzlia")
    captured = capsys.readouterr()
    assert "Weather in Herzlia" in captured.out

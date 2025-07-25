import os
from utils import csvgen

def test_generate_report_creates_file(tmp_path):
    output_file = tmp_path / "report.csv"
    csvgen.generate_report(str(output_file))
    assert output_file.exists()
    with open(output_file) as f:
        lines = f.readlines()
        assert len(lines) > 1  # Header + data rows

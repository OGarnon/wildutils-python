# tests/test_renamer.py
import os
from utils import renamer

def test_rename_files(tmp_path):
    for i in range(3):
        (tmp_path / f"file{i}.txt").write_text("demo")

    renamer.rename_files(str(tmp_path), "renamed")
    renamed_files = os.listdir(tmp_path)

    assert all(name.startswith("renamed_") for name in renamed_files)
    assert all(name.endswith(".txt") for name in renamed_files)
    assert len(renamed_files) == 3

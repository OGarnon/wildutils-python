"""
renamer.py
Batch renames all files in a directory with a given prefix.
"""
import os  # Used for file and directory handling

def rename_files(directory, prefix):
    try:
        files = os.listdir(directory)  # List files in directory
        count = 0
        for i, filename in enumerate(files):
            path = os.path.join(directory, filename)
            if os.path.isfile(path):
                ext = os.path.splitext(filename)[1]  # Get file extension
                new_name = f"{prefix}_{i}{ext}"  # Create new filename
                os.rename(path, os.path.join(directory, new_name))
                count += 1
        print(f"\u2705 Renamed {count} file(s).")
    except Exception as e:
        print(f"Error: {e}")

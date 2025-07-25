"""
csvgen.py
Generates a CSV file with fake user data (ID, Name, Score).
"""
import csv  # Used for writing to CSV format
import random  # Used to generate fake scores

def generate_report(output_file):
    rows = [("ID", "Name", "Score")]  # Header row
    for i in range(1, 11):  # Create 10 fake rows
        rows.append((i, f"User{i}", random.randint(50, 100)))

    # Write to CSV file
    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print(f"\u2705 CSV report saved to '{output_file}'")

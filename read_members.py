import csv
from pathlib import Path

csv_path = Path(__file__).parent / "mockdata" / "members.csv.csv"

with csv_path.open(newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(f"{row['first_name']} {row['last_name']}")

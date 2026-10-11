import csv
import json
from pathlib import Path
from collections import Counter

FOLDER = Path(__file__).parent
CSV_FILE = FOLDER / "students.csv"
JSON_FILE = FOLDER / "students.json"


def analyse_csv():
    try:
        with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

    except FileNotFoundError:
        print("students.csv was not found.")
        return
    except OSError as error:
        print("Could not read CSV file:", error)
        return

    if not rows:
        print("CSV file has no data records.")
        return

    print("\n===== CSV ANALYSIS =====")
    print("Total records:", len(rows))

    # Count missing values in each column
    print("\nMissing values by column:")
    for column in rows[0].keys():
        missing = sum(
            1 for row in rows
            if row.get(column) is None or not row[column].strip()
        )
        print(column, ":", missing)

    # Find duplicate records
    seen = set()
    duplicates = 0

    for row in rows:
        record = tuple(
            (key, row[key]) for key in rows[0].keys()
        )

        if record in seen:
            duplicates += 1
        else:
            seen.add(record)

    print("\nDuplicate records:", duplicates)

    # Calculate statistics for numeric columns
    for column in rows[0].keys():
        values = []

        for row in rows:
            try:
                if row[column].strip():
                    values.append(float(row[column]))
            except (ValueError, AttributeError):
                pass

        if values:
            print(f"\nStatistics for {column}:")
            print("Count:", len(values))
            print("Average:", round(sum(values) / len(values), 2))
            print("Minimum:", min(values))
            print("Maximum:", max(values))

    # Category-wise statistics
    departments = Counter(
        row["department"].strip()
        for row in rows
        if row.get("department") and row["department"].strip()
    )

    print("\nRecords by department:")
    for department, count in departments.items():
        print(department, ":", count)


def analyse_json():
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

    except FileNotFoundError:
        print("students.json was not found.")
        return
    except json.JSONDecodeError:
        print("students.json contains invalid JSON.")
        return
    except OSError as error:
        print("Could not read JSON file:", error)
        return

    if not isinstance(data, list):
        print("Expected a JSON list of student records.")
        return

    print("\n===== JSON ANALYSIS =====")
    print("Total records:", len(data))

    if not data:
        print("No records available.")
        return

    # Missing values
    all_columns = set()
    for record in data:
        if isinstance(record, dict):
            all_columns.update(record.keys())

    print("\nMissing values by field:")
    for column in sorted(all_columns):
        missing = sum(
            1 for record in data
            if not isinstance(record, dict)
            or column not in record
            or record[column] is None
            or record[column] == ""
        )
        print(column, ":", missing)

    # Duplicate records
    seen = set()
    duplicates = 0

    for record in data:
        signature = json.dumps(record, sort_keys=True)

        if signature in seen:
            duplicates += 1
        else:
            seen.add(signature)

    print("\nDuplicate records:", duplicates)

    # Numeric statistics
    numeric_columns = set()

    for record in data:
        if isinstance(record, dict):
            for column, value in record.items():
                if isinstance(value, (int, float)) and not isinstance(value, bool):
                    numeric_columns.add(column)

    for column in sorted(numeric_columns):
        values = [
            record[column]
            for record in data
            if isinstance(record, dict)
            and isinstance(record.get(column), (int, float))
            and not isinstance(record.get(column), bool)
        ]

        if values:
            print(f"\nStatistics for {column}:")
            print("Count:", len(values))
            print("Average:", round(sum(values) / len(values), 2))
            print("Minimum:", min(values))
            print("Maximum:", max(values))

    # Category-wise statistics
    departments = Counter(
        record["department"]
        for record in data
        if isinstance(record, dict)
        and isinstance(record.get("department"), str)
        and record["department"].strip()
    )

    print("\nRecords by department:")
    for department, count in departments.items():
        print(department, ":", count)


if __name__ == "__main__":
    analyse_csv()
    analyse_json()
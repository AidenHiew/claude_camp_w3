# CSV Student Data Analyzer
# Task: Read a student CSV file (containing Name, Email, Join Date, Country, and Challenge Status).
# Statistics to calculate: Total number of students, student count by country, and challenge completion rate.
# Output: Save the statistical results into a file named report.json.
# Bonus challenge: Implement this using Pandas instead of writing manual for loops.

import argparse
import json
import os
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description="Analyze a student CSV file and save a report.")
    parser.add_argument(
        "csv_path",
        nargs="?",
        default=None,
        help="Path to the student CSV file. If omitted, uses students_list.csv in the script directory.",
    )
    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = args.csv_path or os.path.join(script_dir, "students_list.csv")

    data = pd.read_csv(csv_path)
    data.columns = [col.strip().lower() for col in data.columns]

    total_students = len(data)
    students_by_country = data["country"].value_counts()

    status_col = next(
        (col for col in ["challenge_status", "bet_status", "status", "challenge"] if col in data.columns),
        None,
    )
    if status_col is None:
        raise KeyError(
            "Missing required status column in CSV. Expected one of: challenge_status, bet_status, status, challenge."
        )

    challenge_completion_rate = (data[status_col].str.lower() == "completed").mean()

    print(f"Total Number of Students: {total_students}")
    print("\nStudents by Country:")
    print(students_by_country)
    print(f"\nChallenge Completion Rate: {challenge_completion_rate:.2%}")

    report = {
        "total_students": total_students,
        "students_by_country": students_by_country.to_dict(),
        "challenge_completion_rate": float(round(challenge_completion_rate, 4)),
        "status_column_used": status_col,
    }

    report_path = os.path.join(script_dir, "report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)

    print(f"\nReport saved to {report_path}")
    print("Analysis complete.")
    print("Thank you for checking this out!")


if __name__ == "__main__":
    main()

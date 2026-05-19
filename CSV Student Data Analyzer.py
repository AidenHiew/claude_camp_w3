#CSV Student Data Analyzer
#Task: Read a student CSV file (containing Name, Email, Join Date, Country, and Challenge Status).
#Statistics to calculate: Total number of students, student count by country, and challenge completion rate.
#Output: Save the statistical results into a file named report.json.
#Bonus challenge: Implement this using Pandas instead of writing manual for loops.

import pandas as pd

data = pd.read_csv("students_list.csv")

len(data)

total_students = len(data)

# Count students by country
students_by_country = data['Country'].value_counts()

print(f"Total Number of Students: {total_students}")
print(f"\nStudents by Country:")
print(students_by_country)



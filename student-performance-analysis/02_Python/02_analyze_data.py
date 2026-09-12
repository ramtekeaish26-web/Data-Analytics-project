import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Find the project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset location
DATA_FILE = BASE_DIR / "01_Data" / "student_performance_cleaned.csv"

# Output folder
OUTPUT_DIR = BASE_DIR / "02_Python" / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

# Load the cleaned dataset
df = pd.read_csv(DATA_FILE)

print("Student Performance Analysis")
print("----------------------------")

# Basic information
print("\nDataset shape:")
print(df.shape)

print("\nTotal students:")
print(len(df))

# Average values
average_marks = df["Final_Marks"].mean()
average_attendance = df["Attendance_Percent"].mean()
average_study_hours = df["Study_Hours_Per_Day"].mean()

print("\nAverage Final Marks:", round(average_marks, 2))
print("Average Attendance:", round(average_attendance, 2))
print("Average Study Hours:", round(average_study_hours, 2))

# --------------------------------
# Branch-wise performance
# --------------------------------

branch_performance = (
    df.groupby("Branch")["Final_Marks"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
)

print("\nAverage Final Marks by Branch:")
print(branch_performance)

branch_performance.to_csv(
    OUTPUT_DIR / "branch_performance.csv"
)

# --------------------------------
# Semester-wise performance
# --------------------------------

semester_performance = (
    df.groupby("Semester")["Final_Marks"]
    .mean()
    .round(2)
)

print("\nAverage Final Marks by Semester:")
print(semester_performance)

semester_performance.to_csv(
    OUTPUT_DIR / "semester_performance.csv"
)

# --------------------------------
# Result distribution
# --------------------------------

result_distribution = df["Result"].value_counts()

print("\nResult Distribution:")
print(result_distribution)

result_distribution.to_csv(
    OUTPUT_DIR / "result_distribution.csv"
)

# --------------------------------
# Risk level distribution
# --------------------------------

risk_distribution = df["Risk_Level"].value_counts()

print("\nRisk Level Distribution:")
print(risk_distribution)

risk_distribution.to_csv(
    OUTPUT_DIR / "risk_level_distribution.csv"
)

# --------------------------------
# Gender-wise performance
# --------------------------------

gender_performance = (
    df.groupby("Gender")["Final_Marks"]
    .mean()
    .round(2)
)

print("\nAverage Final Marks by Gender:")
print(gender_performance)

gender_performance.to_csv(
    OUTPUT_DIR / "gender_performance.csv"
)

# --------------------------------
# Chart 1 - Branch Performance
# --------------------------------

plt.figure(figsize=(8, 5))

branch_performance.plot(kind="bar")

plt.title("Average Final Marks by Branch")
plt.xlabel("Branch")
plt.ylabel("Average Final Marks")

plt.xticks(rotation=15)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "average_marks_by_branch.png"
)

plt.close()

# --------------------------------
# Chart 2 - Semester Performance
# --------------------------------

plt.figure(figsize=(8, 5))

semester_performance.plot(
    kind="line",
    marker="o"
)

plt.title("Average Final Marks by Semester")
plt.xlabel("Semester")
plt.ylabel("Average Final Marks")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "average_marks_by_semester.png"
)

plt.close()

print("\n----------------------------")
print("Analysis completed successfully!")
print("----------------------------")
print("Check the 02_Python/output folder.")
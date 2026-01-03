# data_management.py
import pandas as pd
import os

FILE = "data/students.csv"

# Create CSV if not exists
if not os.path.exists(FILE):
    df = pd.DataFrame(columns=["StudentID","Name","Age","Math","Physics","Chemistry","English","History","Orientation"])
    df.to_csv(FILE, index=False)

def add_student(student):
    """
    Add a new student to the CSV file.
    student: dict with keys matching columns
    """
    df = pd.read_csv(FILE)
    df = pd.concat([df, pd.DataFrame([student])], ignore_index=True)
    df.to_csv(FILE, index=False)
    print(f"✅ Added student {student['Name']}")

def view_students():
    """Print all students"""
    df = pd.read_csv(FILE)
    print(df)

# app.py
"""
Interactive app to add students or predict orientation using AI
"""

import streamlit as st
import pandas as pd
import joblib
from data_management import add_student, view_students

# Load model
clf = joblib.load("orientation_model.pkl")

st.title("🎓 Student Orientation Predictor")

menu = ["Add Student", "View Students", "Predict Orientation"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Student":
    st.subheader("Add a new student")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=10, max_value=25, step=1)
    math = st.number_input("Math", 0, 100)
    physics = st.number_input("Physics", 0, 100)
    chemistry = st.number_input("Chemistry", 0, 100)
    english = st.number_input("English", 0, 100)
    history = st.number_input("History", 0, 100)
    orientation = st.selectbox("Orientation (if known)", ["Science","Arts","Tech","Undecided"])

    if st.button("Add Student"):
        # Auto-generate StudentID
        df = pd.read_csv("data/students.csv")
        student_id = len(df)+1
        student = {
            "StudentID": student_id,
            "Name": name,
            "Age": age,
            "Math": math,
            "Physics": physics,
            "Chemistry": chemistry,
            "English": english,
            "History": history,
            "Orientation": orientation
        }
        add_student(student)
        st.success(f"Added student {name}")

elif choice == "View Students":
    st.subheader("All Students")
    df = pd.read_csv("data/students.csv")
    st.dataframe(df)

elif choice == "Predict Orientation":
    st.subheader("Predict Orientation Based on Scores")
    math = st.number_input("Math", 0, 100)
    physics = st.number_input("Physics", 0, 100)
    chemistry = st.number_input("Chemistry", 0, 100)
    english = st.number_input("English", 0, 100)
    history = st.number_input("History", 0, 100)

    if st.button("Predict"):
        prediction = clf.predict([[math, physics, chemistry, english, history]])
        st.success(f"Predicted Orientation: {prediction[0]}")

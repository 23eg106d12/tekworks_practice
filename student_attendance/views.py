import streamlit as st
from student import add_student, view_students
from attendance import mark_attendance, view_attendance
from marks import add_marks, view_marks


def main_view():
    st.title("Student Attendance & Marks Management System")

    menu = [
        "Home",
        "Student Management",
        "Attendance",
        "Marks"
    ]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        home_page()

    elif choice == "Student Management":
        st.sidebar.subheader("Student Options")
        action = st.sidebar.radio("Action", ["Add Student", "View Students"])

        if action == "Add Student":
            add_student()
        else:
            view_students()

    elif choice == "Attendance":
        st.sidebar.subheader("Attendance Options")
        action = st.sidebar.radio("Action", ["Mark Attendance", "View Attendance"])

        if action == "Mark Attendance":
            mark_attendance()
        else:
            view_attendance()

    elif choice == "Marks":
        st.sidebar.subheader("Marks Options")
        action = st.sidebar.radio("Action", ["Add Marks", "View Marks"])

        if action == "Add Marks":
            add_marks()
        else:
            view_marks()


def home_page():
    st.subheader("Home")
    st.write("Welcome to the Student Attendance & Marks Management System")

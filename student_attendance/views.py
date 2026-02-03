import streamlit as st
from auth import login, logout
from student import add_student, view_students
from attendance import mark_attendance, view_attendance
from marks import add_marks, view_marks


def main_view():

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        login()
        return

    st.sidebar.success(f"Logged in as {st.session_state.get('username')}")
    logout()

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
        action = st.sidebar.radio("Action", ["Add Student", "View Students"])
        add_student() if action == "Add Student" else view_students()

    elif choice == "Attendance":
        action = st.sidebar.radio("Action", ["Mark Attendance", "View Attendance"])
        mark_attendance() if action == "Mark Attendance" else view_attendance()

    elif choice == "Marks":
        action = st.sidebar.radio("Action", ["Add Marks", "View Marks"])
        add_marks() if action == "Add Marks" else view_marks()


def home_page():
    st.subheader("Home")
    st.write("Welcome to the Student Attendance & Marks Management System")

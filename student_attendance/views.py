import streamlit as st

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
        student_page()
    elif choice == "Attendance":
        attendance_page()
    elif choice == "Marks":
        marks_page()


def home_page():
    st.subheader("Home")
    st.write("Welcome to the Student Attendance & Marks Management System.")


def student_page():
    st.subheader("Student Management")
    st.write("Student related operations will be handled here.")


def attendance_page():
    st.subheader("Attendance Management")
    st.write("Attendance related operations will be handled here.")


def marks_page():
    st.subheader("Marks Management")
    st.write("Marks related operations will be handled here.")

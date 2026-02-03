import streamlit as st

# Initialize student list in session state
if "students" not in st.session_state:
    st.session_state["students"] = []


def add_student():
    st.subheader("Add Student")

    name = st.text_input("Student Name")
    roll_no = st.text_input("Roll Number")
    course = st.text_input("Course")

    if st.button("Add Student"):
        if name and roll_no and course:
            student = {
                "name": name,
                "roll_no": roll_no,
                "course": course
            }
            st.session_state["students"].append(student)
            st.success("Student added successfully")
        else:
            st.error("All fields are required")


def view_students():
    st.subheader("Student List")

    if st.session_state["students"]:
        st.table(st.session_state["students"])
    else:
        st.info("No students added yet")

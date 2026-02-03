import streamlit as st
from db import get_connection

st.set_page_config(page_title="Student Attendance & Marks Portal")

st.title("Student Attendance & Marks Portal")
st.subheader("Add Student Details")

with st.form("add_student_form"):
    roll_no = st.text_input("Roll No")
    name = st.text_input("Student Name")
    student_class = st.selectbox(
        "Class",
        ["Select Class", "10-A", "10-B", "11-A", "11-B", "12-A", "12-B"]
    )

    submit = st.form_submit_button("Add Student")

if submit:
    if roll_no == "" or name == "" or student_class == "Select Class":
        st.error("Please fill all fields")
    else:
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO students (roll_no, name, class)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (roll_no, name, student_class))
            conn.commit()

            st.success("Student added successfully")

            cursor.close()
            conn.close()

        except Exception as e:
            st.error(f"Error: {e}")

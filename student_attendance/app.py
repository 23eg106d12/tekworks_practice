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

st.divider()
st.subheader("Mark Attendance")

def get_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, roll_no, name FROM students")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return students

students = get_students()

student_map = {
    f"{roll} - {name}": sid
    for sid, roll, name in students
}
with st.form("attendance_form"):
    student_selected = st.selectbox(
        "Select Student",
        ["Select Student"] + list(student_map.keys())
    )

    attendance_date = st.date_input("Date")
    status = st.radio("Attendance Status", ["Present", "Absent"])

    mark_attendance = st.form_submit_button("Mark Attendance")
if mark_attendance:
    st.write("Submit button clicked")

    if student_selected == "Select Student":
        st.error("Please select a student")
    else:
        try:
            student_id = student_map[student_selected]

            conn = get_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO attendance (student_id, date, status)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (student_id, attendance_date, status))
            conn.commit()

            st.success("Attendance marked successfully")

            cursor.close()
            conn.close()

        except Exception as e:
            st.error(f"Error: {e}")

st.divider()
st.subheader("Add Subject-wise Marks")

with st.form("marks_form"):
    marks_student = st.selectbox(
        "Select Student",
        ["Select Student"] + list(student_map.keys())
    )

    subject = st.selectbox(
        "Subject",
        ["Maths", "Science", "English", "Social", "Computer"]
    )

    marks = st.number_input(
        "Marks",
        min_value=0,
        max_value=100,
        step=1
    )

    submit_marks = st.form_submit_button("Add Marks")
if submit_marks:
    if marks_student == "Select Student":
        st.error("Please select a student")
    else:
        try:
            student_id = student_map[marks_student]

            conn = get_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO marks (student_id, subject, marks)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (student_id, subject, marks))
            conn.commit()

            st.success("Marks added successfully")

            cursor.close()
            conn.close()

        except Exception as e:
            st.error(f"Error: {e}")

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

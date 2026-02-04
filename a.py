import streamlit as st
import pandas as pd
import mysql.connector

# ---------------- DATABASE CONNECTION ----------------
def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="student_db"
        )
        return conn
    except mysql.connector.Error as e:
        st.error(f" Cannot connect to MySQL: {e}")
        return None

# ---------------- APP TITLE ----------------
st.title("🎓 Student Management System")

menu = st.sidebar.selectbox("Menu", ["Add Student", "View Students", "Update Marks", "Delete Student", "Analyze Performance"])

# ---------------- ADD STUDENT ----------------
if menu == "Add Student":
    st.subheader(" Add Student Details")
    name = st.text_input("Name")
    age = st.number_input("Age", 1, 100)
    subject = st.text_input("Subject")
    marks = st.number_input("Marks", 0, 100)

    if st.button("Add Student"):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            # Ensure table exists
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100),
                    age INT,
                    subject VARCHAR(50),
                    marks INT
                )
            """)
            cursor.execute(
                "INSERT INTO students (name, age, subject, marks) VALUES (%s, %s, %s, %s)",
                (name, age, subject, marks)
            )
            conn.commit()
            conn.close()
            st.success("Student added successfully!")

# ---------------- VIEW STUDENTS ----------------
elif menu == "View Students":
    st.subheader("View Students")
    conn = get_connection()
    if conn:
        df = pd.read_sql("SELECT * FROM students", conn)
        conn.close()
        if df.empty:
            st.warning("No students found")
        else:
            df["Status"] = df["marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")
            st.dataframe(df)

# ---------------- UPDATE MARKS ----------------
elif menu == "Update Marks":
    st.subheader(" Update Marks")
    student_id = st.number_input("Student ID", 1)
    new_marks = st.number_input("New Marks", 0, 100)
    if st.button("Update"):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE students SET marks=%s WHERE id=%s", (new_marks, student_id))
            conn.commit()
            conn.close()
            st.success("Marks updated successfully!")

# ---------------- DELETE STUDENT ----------------
elif menu == "Delete Student":
    st.subheader("🗑️ Delete Student")
    student_id = st.number_input("Student ID", 1)
    if st.button("Delete"):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
            conn.commit()
            conn.close()
            st.success("Student deleted successfully!")

# ---------------- ANALYZE PERFORMANCE ----------------
elif menu == "Analyze Performance":
    st.subheader("📊 Performance Analysis")
    conn = get_connection()
    if conn:
        df = pd.read_sql("SELECT * FROM students", conn)
        conn.close()
        if df.empty:
            st.warning("No data available")
        else:
            df["Status"] = df["marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")
            
            # Average marks per subject
            st.write("### Average Marks per Subject")
            st.bar_chart(df.groupby("subject")["marks"].mean())
            
            # Overall average
            st.metric("Overall Average Marks", round(df["marks"].mean(), 2))
            
            # Pass percentage
            pass_percentage = (df[df["marks"] >= 40].shape[0] / df.shape[0]) * 100
            st.metric("Pass Percentage", f"{round(pass_percentage,2)}%")
            
            # Top scorer
            st.write("### Top Scorer")
            st.dataframe(df.loc[[df["marks"].idxmax()]])
            
            # Pass/Fail count
            st.write("### Pass vs Fail Count")
            st.table(df["Status"].value_counts())

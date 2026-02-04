import streamlit as st
import mysql.connector

st.set_page_config(page_title="Online Complaint System")

st.title("📝 Online Complaint Registration")

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="complaint_db"
)

cursor = conn.cursor()

# User Inputs
name = st.text_input("Name")
email = st.text_input("Email")

category = st.selectbox(
    "Complaint Category",
    ["Infrastructure", "Faculty", "Exams", "Administration", "Other"]
)

description = st.text_area("Complaint Description")

if st.button("Submit Complaint"):
    st.write("Button clicked")  # DEBUG

    if name == "" or email == "" or description == "":
        st.error("⚠️ All fields are required")
    else:
        try:
            cursor.execute(
                """
                INSERT INTO complaints (name, email, category, description)
                VALUES (%s, %s, %s, %s)
                """,
                (name, email, category, description)
            )
            conn.commit()

            st.write("Rows inserted:", cursor.rowcount)  # DEBUG

            complaint_id = cursor.lastrowid
            st.success("Complaint submitted successfully!")
            st.info(f"Your Complaint ID is: {complaint_id}")

        except Exception as e:
            st.error(f"DB Error: {e}")

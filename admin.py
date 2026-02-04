import streamlit as st
import mysql.connector

st.title("Admin Panel")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="complaint_db"
)

cursor = conn.cursor(dictionary=True)

st.sidebar.header("Admin Menu")
option = st.sidebar.selectbox(
    "Choose action",
    ["View Complaints", "Search by ID", "Update Status"]
)

if option == "View Complaints":
    cursor.execute("SELECT * FROM complaints")
    data = cursor.fetchall()
    st.write(data)

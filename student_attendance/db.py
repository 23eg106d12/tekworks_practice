import mysql.connector
import streamlit as st

def get_connection():
    try:
        conn = mysql.connector.connect(
            host=st.secrets["DB_HOST"],
            user=st.secrets["DB_USER"],
            password=st.secrets["DB_PASSWORD"],
            database=st.secrets["DB_NAME"]
        )
        return conn
    except mysql.connector.Error as err:
        st.error(f"Database connection failed: {err}")
        return None

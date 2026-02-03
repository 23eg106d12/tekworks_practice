import streamlit as st
from views import main_view

# Page configuration
st.set_page_config(
    page_title="Student Attendance & Marks Management",
    layout="wide"
)

def main():
    main_view()

if __name__ == "__main__":
    main()

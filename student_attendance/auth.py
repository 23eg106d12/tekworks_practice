import streamlit as st

def login():
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username and password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success("Login successful")
        else:
            st.error("Please enter username and password")


def logout():
    if st.button("Logout"):
        st.session_state.clear()
        st.success("Logged out successfully")

import streamlit as st

# Initialize attendance list
if "attendance" not in st.session_state:
    st.session_state["attendance"] = []


def mark_attendance():
    st.subheader("Mark Attendance")

    roll_no = st.text_input("Roll Number")
    date = st.date_input("Date")
    status = st.selectbox("Status", ["Present", "Absent"])

    if st.button("Submit Attendance"):
        if roll_no:
            record = {
                "roll_no": roll_no,
                "date": str(date),
                "status": status
            }
            st.session_state["attendance"].append(record)
            st.success("Attendance marked successfully")
        else:
            st.error("Roll number is required")


def view_attendance():
    st.subheader("Attendance Records")

    if st.session_state["attendance"]:
        st.table(st.session_state["attendance"])
    else:
        st.info("No attendance records found")

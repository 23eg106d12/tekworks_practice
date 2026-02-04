import streamlit as st

# Initialize marks list
if "marks" not in st.session_state:
    st.session_state["marks"] = []


def add_marks():
    st.subheader("Add Marks")

    roll_no = st.text_input("Roll Number")
    subject = st.text_input("Subject")
    marks = st.number_input("Marks", min_value=0, max_value=100)

    if st.button("Submit Marks"):
        if roll_no and subject:
            record = {
                "roll_no": roll_no,
                "subject": subject,
                "marks": marks
            }
            st.session_state["marks"].append(record)
            st.success("Marks added successfully")
        else:
            st.error("All fields are required")


def view_marks():
    st.subheader("Marks Records")

    if st.session_state["marks"]:
        st.table(st.session_state["marks"])
    else:
        st.info("No marks records found")

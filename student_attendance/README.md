# Student Attendance & Marks Management System

A Streamlit-based web application to manage student details, attendance, and marks with authentication support.

---

## 🚀 Features
- User login & logout (session-based authentication)
- Add and view students
- Mark and view attendance
- Add and view marks
- Clean UI with sidebar navigation

---

## 🛠 Technologies Used
- Python
- Streamlit
- MySQL (planned / configurable)
- Pandas

---

## 📁 Project Structure
student_attendance/
│
├── app.py          # Application entry point
├── views.py        # UI routing and layout
├── auth.py         # Authentication logic
├── student.py      # Student management
├── attendance.py   # Attendance management
├── marks.py        # Marks management
├── db.py           # Database connection
├── requirements.txt
└── README.md

---

## ▶ How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py

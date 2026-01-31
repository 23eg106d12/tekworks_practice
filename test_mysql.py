import mysql.connector

try:
    # Connect to MySQL
    conn = mysql.connector.connect(
        host="localhost",     # your MySQL host
        user="root",          # your MySQL username
        password="root",      # your MySQL password
        database="student_db" # database to use
    )
    print("✅ Connected to MySQL successfully!")

    # Optional: check tables
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    print("Tables in student_db:", tables)

    conn.close()

except mysql.connector.Error as err:
    print(f"❌ MySQL connection failed: {err}")

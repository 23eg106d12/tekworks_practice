import streamlit as st
import mysql.connector
import pandas as pd

st.set_page_config(page_title="Inventory Management", layout="wide")

st.title("📦 Inventory Management System")

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="inventory_db"
)
cursor = conn.cursor(dictionary=True)

# ---------- ADD PRODUCT SECTION ----------
st.header("➕ Add New Product")

with st.form("add_product_form"):
    name = st.text_input("Product Name")
    price = st.number_input("Price", min_value=0.0, step=0.5)
    stock = st.number_input("Stock Quantity", min_value=0, step=1)
    submit = st.form_submit_button("Add Product")

    if submit:
        if name == "":
            st.error("Product name cannot be empty")
        else:
            cursor.execute(
                "INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)",
                (name, price, stock)
            )
            conn.commit()
            st.success("✅ Product added successfully")

# ---------- VIEW INVENTORY ----------
st.header("📋 Current Inventory")

cursor.execute("SELECT * FROM products")
products = cursor.fetchall()

if products:
    df = pd.DataFrame(products)
    st.dataframe(df)
else:
    st.info("No products available")

# ---------- DAILY SALES SUMMARY ----------
st.header("📊 Daily Sales Summary")

cursor.execute("""
    SELECT DATE(bill_date) as sale_date,
           SUM(total_amount) as total_sales,
           COUNT(*) as total_bills
    FROM bills
    GROUP BY DATE(bill_date)
""")

sales = cursor.fetchall()

if sales:
    df_sales = pd.DataFrame(sales)
    st.dataframe(df_sales)

    today_sales = df_sales.iloc[-1]["total_sales"]
    st.metric("Today's Total Sales", f"₹ {today_sales}")
else:
    st.info("No sales yet")


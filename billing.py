import streamlit as st
from datetime import date

def billing_page(conn):
    cursor = conn.cursor()

    st.header("🧾 Billing Section")

    if "cart" not in st.session_state:
        st.session_state.cart = []

    cursor.execute("SELECT id, name, price, stock FROM products")
    products = cursor.fetchall()

    product_dict = {p[1]: p for p in products}

    col1, col2 = st.columns(2)

    with col1:
        product_name = st.selectbox("Select Product", product_dict.keys())
    with col2:
        qty = st.number_input("Quantity", min_value=1)

    if st.button("Add to Cart"):
        product = product_dict[product_name]
        if qty <= product[3]:
            st.session_state.cart.append((product, qty))
            st.success("Added to cart")
        else:
            st.error("Not enough stock")

    st.subheader("🛍 Cart")
    total_bill = 0

    for item, qty in st.session_state.cart:
        cost = item[2] * qty
        total_bill += cost
        st.write(f"{item[1]} × {qty} = ₹{cost}")

    st.write(f"### Total: ₹{total_bill}")

    if st.button("Generate Bill"):
        cursor.execute(
            "INSERT INTO bills (bill_date, total_amount) VALUES (%s,%s)",
            (date.today(), total_bill)
        )
        conn.commit()

        bill_id = cursor.lastrowid

        for item, qty in st.session_state.cart:
            cursor.execute(
                "INSERT INTO bill_items (bill_id, product_id, quantity) VALUES (%s,%s,%s)",
                (bill_id, item[0], qty)
            )
            cursor.execute(
                "UPDATE products SET stock = stock - %s WHERE id = %s",
                (qty, item[0])
            )

        conn.commit()
        st.session_state.cart = []
        st.success("✅ Bill Generated Successfully")

        st.download_button(
            "Download Bill",
            data=f"Total Bill Amount: ₹{total_bill}",
            file_name="bill.txt"
        )

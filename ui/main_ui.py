import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime
from utils.calculator import calculate_bill
from utils.db_utils import insert_bill

def run_ui(db_path):
    st.title("🍽 Restaurant Billing System")

    # Ensure data folder exists
    os.makedirs("data", exist_ok=True)

    # Load Menu
    try:
        menu_df = pd.read_csv("data/menu.csv")
    except FileNotFoundError:
        st.error("❌ Menu file not found. Please place 'menu.csv' in the data folder.")
        return

    # Select Order Type
    order_type = st.sidebar.radio("Order Type", ["Dine-In", "Takeaway"])

    # Add Items
    order_items = []
    for _, row in menu_df.iterrows():
        qty = st.sidebar.number_input(f"{row['name']} (₹{row['price']})", 0, 10, step=1)
        if qty > 0:
            order_items.append({"name": row['name'], "price": row['price'], "qty": qty})

    if st.sidebar.button("Generate Bill"):
        if not order_items:
            st.warning("⚠ No items selected.")
            return

        subtotal, gst, discount, total = calculate_bill(order_items)

        st.subheader("🧾 Bill Summary")
        st.write(pd.DataFrame(order_items))
        st.write(f"**Subtotal:** ₹{subtotal}")
        st.write(f"**GST (5%):** ₹{gst}")
        st.write(f"**Discount:** ₹{discount}")
        st.write(f"**Total:** ₹{total}")

        payment_method = st.selectbox("Payment Method", ["Cash", "Card", "UPI"])

        if st.button("💾 Save & Export"):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            bill_data = {
                "items": json.dumps(order_items),
                "total": total,
                "gst": gst,
                "discount": discount,
                "payment_method": payment_method,
                "order_type": order_type,
                "timestamp": timestamp
            }

            # Save to database
            insert_bill(db_path, bill_data)
            st.success("✅ Bill saved to database.")

            # Save JSON record
            with open("data/sample_bills.json", "a", encoding="utf-8") as f:
                f.write(json.dumps(bill_data) + "\n")

            # Append to Sales Report CSV (with header only if file doesn't exist)
            csv_file = "data/sales_report.csv"
            pd.DataFrame(
                [[timestamp, total, payment_method, order_type]],
                columns=["Timestamp", "Total", "Payment Method", "Order Type"]
            ).to_csv(csv_file, mode='a', index=False, header=not os.path.exists(csv_file))

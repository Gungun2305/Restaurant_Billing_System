# 🍽 Restaurant Billing System (Streamlit + SQLite)

A simple, interactive restaurant billing system built with **Streamlit**, **SQLite**, and **Pandas**.  
It allows restaurant staff to select menu items, generate bills with GST, save transactions to a database, and export sales reports.

---
## 📌 Features
- **Menu Management**: Loads menu items from a CSV file (`menu.csv`)
- **Order Type**: Supports **Dine-In** and **Takeaway**
- **Bill Calculation**:
  - Subtotal
  - GST (default 5%)
  - Discount (optional)
  - Final Total
- **Payment Methods**: Cash, Card, or UPI
- **Database Integration**: Stores all bills in SQLite database
- **Export**:
  - JSON record of orders
  - CSV sales report
---

## 📂 Project Structure
restaurant_billing/
│
├── app.py # Main entry point
├── ui/
│ └── main_ui.py # Streamlit UI logic
├── utils/
│ ├── db_utils.py # Database functions
│ └── calculator.py # Bill calculation logic
├── db/ # SQLite database folder
├── data/
│ ├── menu.csv # Menu data
│ ├── sales_report.csv # Sales report export
│ └── sample_bills.json # Order records in JSON


🛠 Tech Stack

Frontend/UI: Streamlit
Backend: Python
Database: SQLite
Data Handling: Pandas


import sqlite3
def init_db(path):
    conn = sqlite3.connect(path)
    cur = conn.cursor()

    # Create Menu table
    cur.execute('''CREATE TABLE IF NOT EXISTS menu (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL
    )''')

    # Create Bills table
    cur.execute('''CREATE TABLE IF NOT EXISTS bills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        items TEXT,
        total REAL,
        gst REAL,
        discount REAL,
        payment_method TEXT,
        order_type TEXT,
        timestamp TEXT
    )''')

    conn.commit()
    conn.close()

def insert_bill(path, bill_data):
    conn = sqlite3.connect(path)
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO bills (items, total, gst, discount, payment_method, order_type, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        bill_data['items'],
        bill_data['total'],
        bill_data['gst'],
        bill_data['discount'],
        bill_data['payment_method'],
        bill_data['order_type'],
        bill_data['timestamp']
    ))

    conn.commit()
    conn.close()

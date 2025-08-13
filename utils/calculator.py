def calculate_bill(items, gst_rate=0.05, discount_rate=0.0):
    subtotal = sum(item['price'] * item['qty'] for item in items)
    gst = subtotal * gst_rate
    discount = subtotal * discount_rate
    total = subtotal + gst - discount
    return round(subtotal, 2), round(gst, 2), round(discount, 2), round(total, 2)

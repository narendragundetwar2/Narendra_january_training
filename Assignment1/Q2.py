def add_order(order_id, orders=None):
    if orders is None:
        orders = []
    orders.append(order_id)
    return orders
history1 = add_order(10)
print(f"History 1: {history1}")
history1 = add_order(15, history1)
print(f"History 1 updated: {history1}")
history2 = add_order(50)
print(f"History 2: {history2}")

Output:- History 1: [10]
         History 1 updated: [10, 15]
         History 2: [50]
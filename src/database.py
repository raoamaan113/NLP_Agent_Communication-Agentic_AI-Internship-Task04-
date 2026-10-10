import random

class MockOrderDatabase:
    def __init__(self, num_orders=100):
        self.products = [
            "Wireless Headphones", "Smartwatch", "Running Shoes", 
            "Mechanical Keyboard", "Gaming Mouse", "Bluetooth Speaker", "Fitness Tracker"
        ]
        self.statuses = ["shipped", "pending", "delivered", "processing", "cancelled"]
        self.orders = {}
        self._generate_database(num_orders)
        
    def _generate_database(self, num_orders):
        random.seed(42)
        for i in range(1, num_orders + 1):
            order_id = f"ORD-{1000 + i}"
            product = random.choice(self.products)
            status = random.choice(self.statuses)
            self.orders[order_id] = {
                "product_name": product,
                "status": status
            }
            
    def get_order(self, order_id):
        return self.orders.get(order_id, None)

if __name__ == "__main__":
    db = MockOrderDatabase()
    print(f"Generated {len(db.orders)} mock orders successfully!")
    print("Sample Order (ORD-1001):", db.get_order("ORD-1001"))
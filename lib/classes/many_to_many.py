class Coffee:
    def __init__(self, name):
        self._name = name
        self.orders = []
        self.customers = []
        self.average_price = 0.0
        self.num_orders = 0

    @property
    def name(self):
        return self._name

class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all_orders.append(self)
        coffee.orders.append(self)
        customer.orders.append(self)
        # coffee.customers.append(customer)

        if customer not in coffee.customers:
            coffee.customers.append(customer)

class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def num_orders(self):
        """Get the number of times the customer has ordered."""
        return len(self.orders)

    def average_price(self):
        """Calculate the average price of the customer's orders."""
        if not self.orders:
            return 0.0
        
        total_price = sum(order.price for order in self.orders)
        return total_price / len(self.orders)

    def coffees(self):
        return list(set(order.coffee for order in self.orders))

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        return order


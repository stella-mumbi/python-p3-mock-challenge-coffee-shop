import pytest

from classes.many_to_many import Coffee
from classes.many_to_many import Customer
from classes.many_to_many import Order


class TestCustomer:
    """Customer in many_to_many.py"""

    def test_has_name(self):
        """Customer is initialized with name"""
        customer = Customer("Steve")
        assert customer.name == "Steve"

    def test_name_is_mutable_string(self):
        """name is a mutable string"""
        customer = Customer("Steve")
        customer.name = "Stove"
        
        assert customer.name == "Stove"
        
        # # comment out the next two lines if using Exceptions
        # customer.name = 1
        # assert customer.name == "Stove"
        
        assert isinstance(customer.name, str)

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     customer.name = 1

    def test_name_length(self):
        """name is between 1 and 15 characters"""
        customer = Customer("Steve")
        assert len(customer.name) == 5

        # # comment out the next two lines if using Exceptions
        # customer.name = ""
        # assert customer.name == "Steve"
        

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     Customer("TooLongForAName!")

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     Customer("")

    def test_has_many_orders(self):
        """customer has many orders"""
        coffee = Coffee("Vanilla Latte")
        customer_1 = Customer("Steve")
        customer_2 = Customer("Dima")
        order_1 = Order(customer_1, coffee, 2.0)
        order_2 = Order(customer_1, coffee, 5.0)
        order_3 = Order(customer_2, coffee, 5.0)

        assert len(customer_1.orders) == 2
        assert len(customer_2.orders) == 1
        assert order_1 in customer_1.orders
        assert order_2 in customer_1.orders
        assert order_3 not in customer_1.orders
        assert order_3 in customer_2.orders

    def test_orders_of_type_order(self):
        """customer orders are of type Order"""
        coffee = Coffee("Vanilla Latte")
        customer = Customer("Steve")
        Order(customer, coffee, 2.0)
        Order(customer, coffee, 5.0)

        assert isinstance(customer.orders[0], Order)
        assert isinstance(customer.orders[1], Order)

    def test_has_many_coffees(self):
        """customer has many coffees"""
        coffee_1 = Coffee("Vanilla Latte")
        coffee_2 = Coffee("Flat White")
        coffee_3 = Coffee("Mocha")
        customer = Customer("Steve")
        Order(customer, coffee_1, 2.0)
        Order(customer, coffee_2, 5.0)

        assert coffee_1 in customer.coffees()
        assert coffee_2 in customer.coffees()
        assert coffee_3 not in customer.coffees()

    def test_has_unique_coffees(self):
        """customer has a unique list of all the coffees they have ordered"""
        coffee = Coffee("Vanilla Latte")
        coffee_2 = Coffee("Flat White")
        customer = Customer("Steve")
        Order(customer, coffee, 2.0)
        Order(customer, coffee, 2.0)
        Order(customer, coffee_2, 5.0)
        customer.coffees = customer.coffees()

        assert len(set(customer.coffees)) == len(customer.coffees)
        assert len(customer.coffees) == 2
    
    def test_coffees_of_type_coffee(self):
        """customer coffees are of type Coffee"""
        coffee_1 = Coffee("Vanilla Latte")
        coffee_2 = Coffee("Flat White")
        customer = Customer("Steve")
        Order(customer, coffee_1, 2.0)
        Order(customer, coffee_2, 5.0)
        customer.coffees = customer.coffees()

        assert isinstance(customer.coffees[0], Coffee)
        assert isinstance(customer.coffees[1], Coffee)
    
    def test_create_order(self):
        """creates a new order for a customer"""
        coffee_1 = Coffee("Vanilla Latte")
        coffee_2 = Coffee("Flat White")
        customer_1 = Customer("Steve")
        customer_2 = Customer("Dima")
        order_1 = customer_1.create_order(coffee_1, 2.0)
        order_2 = customer_2.create_order(coffee_2, 5.0)
        
        assert isinstance(order_1, Order)
        assert isinstance(order_2, Order)
        
       
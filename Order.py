from abc import ABC, abstractmethod

class Order(ABC):
    PAYMENT_TYPE = {"CREDIT CARD", "CASH", "CHECK", "OTHER"}
    def __init__(self, order_id, name, delivery_address, items, order_customer, payment_type, order_date=None,):
        if payment_type not in Order.PAYMENT_TYPE:
            raise ValueError(f'Invalid payment; you must choose from the following payment options {Order.PAYMENT_TYPE}')

        self.order_id = order_id
        self.name = name
        self.delivery_address = delivery_address
        self.items = list(items)
        self.order_customer = order_customer
        self.payment_type = payment_type
        self.order_date = order_date
        self.order_total_price = self.calculate_total_price()

        for item in self.items:
            self.order_customer.add_favorite_item(item)

    @abstractmethod
    def calculate_total_price(self):
        pass











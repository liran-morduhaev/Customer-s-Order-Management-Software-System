import random

class Customer:
    CUSTOMER_TYPE = {'VIP', 'REGULAR'}
    def __init__(self, customer_id, first_name, last_name, email, delivery_address, customer_type, customer_discount=None, favorite_items=None):

        if customer_type not in Customer.CUSTOMER_TYPE:
            raise ValueError(f"Invalid customer type: {customer_type}")

        self.customer_id =customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.delivery_address = delivery_address
        self.customer_type = customer_type
        self.customer_discount = customer_discount
        self.favorite_items = list(favorite_items) if favorite_items else []
        self.customer_gift = None

        if self.customer_type == 'VIP' and customer_discount is None:
            self.customer_discount = round(random.uniform(0, 1), 2)
        else:
            self.customer_discount = customer_discount

    def add_favorite_item(self, item):
        for fav in self.favorite_items:
            if fav.item_name == item.item_name:
                break
        else:
            self.favorite_items.append(item)


    def remove_favorite_item(self, item_name):
        for fav in self.favorite_items:
            if fav.item_name == item_name:
                self.favorite_items.remove(fav)
                break
        else:
            raise ValueError(f"Item '{item_name}' not in favorite items!")

    def take_gift(self, gift):
        self.customer_gift = gift

    def open_gift(self):
        if self.customer_gift is not None:
            self.customer_gift.open_gift()
        else:
            print("No gift to open.")


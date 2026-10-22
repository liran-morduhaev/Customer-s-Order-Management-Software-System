from Order import Order

class RegularOrder(Order):
    def calculate_total_price(self):
        price = sum(item.item_price for item in self.items)
        self.order_total_price = price
        return self.order_total_price


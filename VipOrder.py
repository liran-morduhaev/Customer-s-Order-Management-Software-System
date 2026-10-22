from Order import Order

class VipOrder(Order):
    def calculate_total_price(self):
        if self.order_customer.customer_type != 'VIP':
            raise ValueError("Only VIP customers can place a VIP order!")

        total = sum(item.item_price for item in self.items)

        if self.order_customer.customer_discount is not None:
            total -= total * self.order_customer.customer_discount

        self.order_total_price = round(total, 2)
        return self.order_total_price



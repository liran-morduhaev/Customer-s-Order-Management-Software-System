from Item import Item
from Customer import Customer
from RegularOrder import RegularOrder
from VipOrder import VipOrder
from CustomerGift import CustomerGift

if __name__ == "__main__":
    # Create items
    item1 = Item(1, "Pizza", 50.0)
    item2 = Item(2, "Burger", 40.0)
    item3 = Item(3, "Pizza", 60.0)  # Same name, different ID

    # Create customers
    regular_customer = Customer(1, "Dan", "Cohen", "dan@gmail.com", "Tel Aviv", "REGULAR")
    vip_customer = Customer(2, "Sarah", "Levi", "sarah@gmail.com", "Haifa", "VIP")

    # Regular order (adds items to favorites automatically)
    order1 = RegularOrder(101, "Order1", "Tel Aviv", [item1, item2], regular_customer, "CREDIT CARD")
    print(f"Order 1 Total: {order1.order_total_price}")
    print(f"Regular Customer Favorites: {[item.item_name for item in regular_customer.favorite_items]}")

    # VIP order (calculates discount and tests duplicate item prevention in favorites)
    order2 = VipOrder(201, "Order2", "Haifa", [item2, item3], vip_customer, "CASH")
    print(f"Order 2 Total: {order2.order_total_price}")
    print(f"VIP Customer Favorites: {[item.item_name for item in vip_customer.favorite_items]}")

    # Manual update of favorites (add & remove)
    regular_customer.add_favorite_item(item3)
    regular_customer.remove_favorite_item("Pizza")
    print(f"Regular Customer Updated Favorites: {[item.item_name for item in regular_customer.favorite_items]}")

    # Gift functionality
    gift = CustomerGift()
    vip_customer.take_gift(gift)
    vip_customer.open_gift()
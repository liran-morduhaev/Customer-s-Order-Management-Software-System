# 🛍️ Customer & Order Management System

An Object-Oriented Programming (OOP) project in Python simulating an e-commerce order management platform.  
The application manages customer tiers, automatic favorite items tracking with deduplication, order validation, polymorphic price calculations, and promotional gift handling.

---

## 🚀 Key Features & OOP Concepts

* **Inheritance & Polymorphism:**
  * `Order` is an Abstract Base Class (`ABC`) enforcing order validation, payment type verification, and price calculation.
  * `RegularOrder` computes the standard item total.
  * `VipOrder` enforces VIP membership constraints and dynamically deducts the customer's personal discount.
* **Abstraction & Interfaces:**
  * `Gift` provides an abstract interface (`open_gift`) realized by `CustomerGift`.
* **Encapsulation & Validation:**
  * Enforces valid customer types (`VIP`, `REGULAR`) and payment methods (`CREDIT CARD`, `CASH`, `CHECK`, `OTHER`).
  * Protects against non-VIP customers creating `VipOrder` instances.
* **Dynamic Customer Profiles:**
  * Automatically assigns random discount rates to newly registered VIP customers without explicit rates.
  * Tracks and updates customer `favorite_items`, preventing duplicate entries based on item names.
  * Supports assigning and opening promotional gifts.

---

## 📁 Project Structure

```text
├── Item.py                  # Product model (item_id, item_name, item_price)
├── Customer.py              # Customer model with tiers, favorites, and gifts
├── Order.py                 # Abstract base class for orders and payment validation
├── RegularOrder.py          # Concrete order calculation for regular customers
├── VipOrder.py              # Concrete order with validation and discount logic
├── Gift.py                  # Abstract base class for gift items
├── CustomerGift.py          # Concrete gift implementation
├── main_3.py                # Demonstration script running simulation scenarios
└── README.md                # Project documentation
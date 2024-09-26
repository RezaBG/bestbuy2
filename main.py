from products import Product
from store import Store

def main():
    # Create products
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    pixel = Product("Google Pixel 7", price=500, quantity=250)

    # Create a store with products
    store = Store([bose, mac])

    # Add a new product
    store.add_product(pixel)

    # Show total quantity in store
    print(f"Total quantity in store: ")

    # Show all active in store
    products = store.get_all_products()
    for product in products:
        print(product.show())

    # Make an order
    order_price = store.order([(bose, 51), (mac, 10)])
    print(f"Orer total price: {order_price}")

    # print(bose.buy(50))
    # print(mac.buy(100))
    # print(mac.is_active())

    # print(bose.show())
    # print(mac.show())

    # bose.set_quantity(1000)
    # print(bose.show())


if __name__ == "__main__":
    main()

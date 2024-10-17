from products import Product, NonStockedProduct, LimitedProduct
from store import Store


def create_default_inventory():
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]
    return Store(product_list)


def start(store: Store):
    while True:
        print("\n   Store Menu")
        print("     ---------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            # List all products
            products = store.get_all_products()
            for idx, product in enumerate(products, start=1):
                print(f"{idx}. {product.show()}")

        elif choice == "2":
            # Show total amount in store
            print(f"Total of {store.get_total_quantity()} items in store")

        elif choice == "3":
            # Make an order
            products = store.get_all_products()
            order_list = []
            while True:
                print("------")
                for idx, product in enumerate(products, start=1):
                    print(f"{idx}, {product.show()}")
                print("-----")
                product_choice = input("Which product # do you want? (Enter to finish): ")
                if not product_choice:
                    break
                try:
                    product_choice = int(product_choice)
                    chosen_product = products[product_choice - 1]
                    quantity = int(input(f"What amount do you want? "))
                    order_list.append((chosen_product, quantity))
                    print("Product added to order!")
                except (IndexError, ValueError):
                    print("Invalid input, please try again.")

            # Process the order
            if order_list:
                total_price = store.order(order_list)
                print(f"*****\nOrder made! Total payment: €{total_price}*****")

        elif choice == "4":
            print("Thank you for visiting the store!")
            break

        else:
            print("Invalid choice, please try again.")


def main():
    store = create_default_inventory()
    start(store)


if __name__ == "__main__":
    main()
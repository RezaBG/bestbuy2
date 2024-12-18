from products import Product, NonStockedProduct, LimitedProduct
from store import Store
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree


def create_default_inventory():
    """Create the default inventory of products."""
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]
    return Store(product_list)


def start(store: Store):
    """Start the store user interface."""
    while True:
        print("\n   Store Menu")
        print("   ----------")
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
            print(f"Total of {store.get_total_quantity()} items in store.")

        elif choice == "3":
            # Make an order
            products = store.get_all_products()
            order_list = []
            while True:
                print("------")
                for idx, product in enumerate(products, start=1):
                    print(f"{idx}. {product.show()}")
                print("------")
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
                print(f"*****\nOrder made! Total payment: €{total_price}\n*****")

        elif choice == "4":
            print("Thank you for visiting the store!")
            break
        else:
            print("Invalid choice, please try again.")


def main():
    """Main function to set up inventory and start the store interface."""
    # Create default inventory and store
    store = create_default_inventory()

    # Set up promotions
    second_half_price = SecondHalfPrice("Second Half Price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    # Assign promotions to products
    store.products[0].set_promotion(second_half_price)  # MacBook Air M2
    store.products[1].set_promotion(third_one_free)  # Bose QuietComfort Earbuds
    store.products[3].set_promotion(thirty_percent)  # Windows License

    # Start the user interface
    start(store)


if __name__ == "__main__":
    main()
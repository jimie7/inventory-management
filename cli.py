import requests

BASE_URL = "http://127.0.0.1:5000"


while True:

    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add new inventory item")
    print("2. View all inventory")
    print("3. View a single inventory item")
    print("4. Update item")
    print("5. Delete item")
    print("6. Find product on OpenFoodFacts")
    print("7. Exit")

    choice = input("Enter your choice: ")

    try:

        # 1. Add new item
        if choice == "1":
            barcode = input("Enter product barcode: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))

            if quantity < 0 or price < 0:
                print("Quantity and price cannot be negative.")
                continue

            data = {
                "barcode": barcode,
                "quantity": quantity,
                "price": price
            }

            response = requests.post(
                f"{BASE_URL}/inventory",
                json=data,
                timeout=10
            )

            print(response.json())

        # 2. View all inventory
        elif choice == "2":
            response = requests.get(
                f"{BASE_URL}/inventory",
                timeout=10
            )

            print(response.json())

        # 3. View one item
        elif choice == "3":
            item_id = int(input("Enter item ID: "))

            response = requests.get(
                f"{BASE_URL}/inventory/{item_id}",
                timeout=10
            )

            print(response.json())

        # 4. Update item
        elif choice == "4":
            item_id = int(input("Enter item ID: "))

            print("1. Update price")
            print("2. Update quantity")

            update_choice = input("Choose what to update: ")

            if update_choice == "1":
                value = float(input("Enter new price: "))

                if value < 0:
                    print("Price cannot be negative.")
                    continue

                data = {"price": value}

            elif update_choice == "2":
                value = int(input("Enter new quantity: "))

                if value < 0:
                    print("Quantity cannot be negative.")
                    continue

                data = {"quantity": value}

            else:
                print("Invalid update choice.")
                continue

            response = requests.patch(
                f"{BASE_URL}/inventory/{item_id}",
                json=data,
                timeout=10
            )

            print(response.json())

        # 5. Delete item
        elif choice == "5":
            item_id = int(input("Enter item ID: "))

            response = requests.delete(
                f"{BASE_URL}/inventory/{item_id}",
                timeout=10
            )

            print(response.json())

        # 6. Find product on OpenFoodFacts
        elif choice == "6":
            barcode = input("Enter product barcode: ")

            response = requests.get(
                f"{BASE_URL}/products/{barcode}",
                timeout=10
            )

            print(response.json())

        # 7. Exit
        elif choice == "7":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please try again.")

    except ValueError:
        print("Invalid input. Please enter the correct value.")

    except requests.ConnectionError:
        print("Cannot connect to Flask. Make sure the server is running.")

    except requests.Timeout:
        print("The request took too long. Please try again.")

    except requests.RequestException:
        print("Something went wrong while communicating with the API.")
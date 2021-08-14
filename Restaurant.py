# Create a dictionary containing foods and their  prices
MENU = {"rice": 300, "spag": 100, "beef": 100, "beans": 150}


# create a function to other from the menu
def restaurant():
    """funtion to take an order from the client"""
    # set the initial price to zero since nothing has been orderered yet
    price = 0
    # Create a loop that keeps asking for the client's order until done
    while True:
        order = input("Order: ")
        order.strip()

        if order in MENU:
            price += MENU[order]
            print(f"{order.capitalize()} costs {MENU[order]}, total is {price}")
        # if order is not an empty dtring and is not in the menu
        elif order not in MENU and order != "":
            print(
                f"We don't have {order} on our menu. Please select a dish from {MENU.items()}"
            )
        # If nothing was ordered, break the loop
        elif order == "":
            print("Thanks for your constant patronage!")
            break
    return f"You are paying {price} naira"


print(restaurant())

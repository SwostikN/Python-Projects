def main():
    print("BPP Pizza Price Calculator")
    print("="*26)

    # Handle errors for pizza quantity input
    while True:
        try:
            quantity_pizza = int(input("How many pizzas ordered? "))
            if quantity_pizza < 0:
                print("Please enter a positive integer!")
            else:
                break  # Exit the loop if a valid input is provided
        except ValueError:
            print("Please enter a number!")

    # Handle errors for delivery input
    while True:
        delivery = input("Is delivery required? (Y/N) ").lower()
        if delivery == "y" or delivery == "n":
            break  # Exit the loop if a valid input is provided
        else:
            print('Please answer "Y" or "N".')

    # Handle errors for Tuesday input
    while True:
        day = input("Is it Tuesday? (Y/N) ").lower()
        if day == "y" or day == "n":
            break  # Exit the loop if a valid input is provided
        else:
            print('Please answer "Y" or "N".')

    # Handle errors for app usage input
    while True:
        app = input("Did the customer use the app? (Y/N) ").lower()
        if app == "y" or app == "n":
            break  # Exit the loop if a valid input is provided
        else:
            print('Please answer "Y" or "N".')

    print("Total Price:", amount(quantity_pizza, day, delivery, app))





# total cost of pizza
def amount(quantity_pizza, day, delivery, app):

    PIZZA_COST = 12  # declaring constant values
    DELIVERY_PRICE = 2.50

    total_cost_of_pizza = quantity_pizza * PIZZA_COST

    if delivery == "y" and quantity_pizza < 5:
        delivery_cost = DELIVERY_PRICE
    else:
        delivery_cost = 0

    total_cost = total_cost_of_pizza + delivery_cost

    # 50% discount on Tuesday
    if day == "y":
        total_cost = total_cost * 0.5

    # 25% discount if app is used
    if app == "y":
        total_cost = total_cost * 0.75

    return f'Total Price: £{total_cost:.2f}'

if __name__ == "__main__":
    main()



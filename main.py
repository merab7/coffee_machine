from data import MENU, resources

bank = 0


def refill_resources():
    resources['water'] = 300
    resources['milk'] = 200
    resources['coffee'] = 100


def get_user_choice():
    return input("What would you like? (espresso/latte/cappuccino): ").lower()


def handle_insufficient_resources(user_choice):
    help_me = input("\nSorry, resources are not enough. Press 'H' to call staff for refill or any other key to exit\
: ").lower()
    if help_me == "h":
        print("\nYou have been refunded.\n\n")
        return refill_resources(), coffee_machine()
    else:
        print("\nYou have been refunded.\n\n")
        return coffee_machine()


def process_coffee(user_choice):
    global bank
    print("Please insert coins.")
    try:
        quarters = 0.25 * float(input("How many quarters ($0.25)?: "))
        dimes = 0.1 * float(input("How many dimes ($0.10)?: "))
        nickels = 0.05 * float(input("How many nickels ($0.05)?: "))
        pennies = 0.01 * float(input("How many pennies ($0.01)?: "))
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")
        return coffee_machine()

    total_inserted_money = [quarters, dimes, nickels, pennies]
    total_money = sum(total_inserted_money)

    if total_money < MENU[user_choice]['cost']:
        print("\nMoney is not enough. You have been refunded.")
        return coffee_machine()
    else:
        change = round(total_money - MENU[user_choice]['cost'], 2)
        print(f"\nYour change is: ${change}. Coffee in process...\n")
        if (
            MENU[user_choice]['ingredients']['water'] > resources['water'] or
            MENU[user_choice]['ingredients']['milk'] > resources['milk'] or
            MENU[user_choice]['ingredients']['coffee'] > resources['coffee']
        ):
            return handle_insufficient_resources(user_choice)
        else:
            resources['water'] -= MENU[user_choice]['ingredients']['water']
            resources['milk'] -= MENU[user_choice]['ingredients']['milk']
            resources['coffee'] -= MENU[user_choice]['ingredients']['coffee']
            bank += MENU[user_choice]["cost"]
            print("Your coffee is ready: ☕\n\n")
            return coffee_machine()


def display_report():
    print(f"Water: {resources['water']}\nMilk: {resources['milk']}\n\
Coffee: {resources['coffee']}\nCurrent income: {bank}")


def coffee_machine():
    while True:
        user_choice = get_user_choice()

        if user_choice == "off":
            print("\nCoffee machine is turned off.")
            break
        elif user_choice in ["espresso", "latte", "cappuccino"]:
            print(f"Cost of your {user_choice} is: ${MENU[user_choice]['cost']}")
            process_coffee(user_choice)
        elif user_choice == "report":
            display_report()
        else:
            print("\nWe do not have this kind of coffee. Please check your input.")


coffee_machine()

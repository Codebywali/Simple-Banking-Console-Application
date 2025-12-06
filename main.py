accounts = []

# Helper Functions
def find_account(acc_number):
    """Return account dictionary if it exists, otherwise None."""
    for acc in accounts:
        if acc["number"] == acc_number:
            return acc
    return None


# Feature: Create Account
def create_account():
    print("\n--- Create New Account ---")

    name = input("Enter your name: ").strip()

    pin = input("Choose a 4-digit PIN: ").strip()
    if not (pin.isdigit() and len(pin) == 4):
        print("Invalid PIN! Must be exactly 4 digits.")
        return

    # Initial deposit
    try:
        initial = float(input("Initial deposit (>= 0): "))
        if initial < 0:
            print("Deposit cannot be negative.")
            return
    except ValueError:
        print("Invalid amount.")
        return

    account_number = len(accounts) + 1

    new_account = {
        "number": account_number,
        "name": name,
        "pin": pin,
        "balance": initial
    }

    accounts.append(new_account)

    print(f"Account created successfully! Your account number is {account_number}.")

# Feature: Login
def login():
    print("\n--- Login ---")
    try:
        acc_no = int(input("Account number: "))
    except ValueError:
        print("Invalid account number.")
        return None

    pin = input("PIN: ").strip()

    acc = find_account(acc_no)
    if acc and acc["pin"] == pin:
        print(f"Welcome, {acc['name']}!")
        return acc
    else:
        print("Incorrect account number or PIN.")
        return None


# Feature: Check Balance
def check_balance(acc):
    print(f"\nYour current balance is: PKR {acc['balance']:.2f}")

# Feature: Deposit
def deposit(acc):
    try:
        amount = float(input("\nEnter amount to deposit: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Invalid amount.")
        return

    acc["balance"] += amount
    print(f"Deposit successful! New balance: PKR {acc['balance']:.2f}")

# Feature: Withdraw
def withdraw(acc):
    try:
        amount = float(input("\nEnter amount to withdraw: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Invalid amount.")
        return

    if amount > acc["balance"]:
        print("Not enough balance!")
        return

    acc["balance"] -= amount
    print(f"Withdraw successful! New balance: PKR {acc['balance']:.2f}")


# Feature: Transfer
def transfer(acc):
    try:
        receiver_no = int(input("\nReceiver account number: "))
        receiver = find_account(receiver_no)
        if receiver is None:
            print("Receiver account does not exist.")
            return
    except ValueError:
        print("Invalid account number.")
        return

    try:
        amount = float(input("Amount to transfer: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Invalid amount.")
        return

    if amount > acc["balance"]:
        print("Not enough balance!")
        return

    acc["balance"] -= amount
    receiver["balance"] += amount

    print(f"Transfer successful! Your new balance: PKR {acc['balance']:.2f}")

# Account Menu (after login)
def account_menu(acc):
    while True:
        print("\n--- Account Menu ---")
        print("1) Check Balance")
        print("2) Deposit")
        print("3) Withdraw")
        print("4) Transfer Money")
        print("5) Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            check_balance(acc)
        elif choice == "2":
            deposit(acc)
        elif choice == "3":
            withdraw(acc)
        elif choice == "4":
            transfer(acc)
        elif choice == "5":
            print("Logged out.\n")
            break
        else:
            print("Invalid choice. Try again.")

# Main Menu
def main_menu():
    while True:
        print("\n=== Simple Banking App ===")
        print("1) Create Account")
        print("2) Login")
        print("3) Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            acc = login()
            if acc:
                account_menu(acc)
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main_menu()
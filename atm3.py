# ATM Banking System (Intermediate Version with Fixed PIN Change)

# User database (PIN as key)
users = {
    "1234": {"name": "Alice", "balance": 5000, "transactions": []},
    "5678": {"name": "Bob", "balance": 8000, "transactions": []},
    "4321": {"name": "Charlie", "balance": 10000, "transactions": []}
}

def check_balance(user):
    print(f"\n✅ {user['name']}, your current balance is: ₹{user['balance']}\n")

def deposit(user):
    amount = float(input("Enter amount to deposit: ₹"))
    if amount > 0:
        user["balance"] += amount
        user["transactions"].append(f"Deposited ₹{amount}")
        print(f"💰 ₹{amount} deposited successfully!")
        check_balance(user)
    else:
        print("❌ Invalid amount!")

def withdraw(user):
    amount = float(input("Enter amount to withdraw: ₹"))
    if amount > user["balance"]:
        print("❌ Insufficient balance!")
    elif amount <= 0:
        print("❌ Invalid amount!")
    else:
        user["balance"] -= amount
        user["transactions"].append(f"Withdrew ₹{amount}")
        print(f"💸 ₹{amount} withdrawn successfully!")
        check_balance(user)

def view_transactions(user):
    print("\n📜 Transaction History:")
    if not user["transactions"]:
        print("No transactions yet.")
    else:
        for t in user["transactions"]:
            print(" -", t)

def change_pin(old_pin, user):
    new_pin = input("Enter new 4-digit PIN: ")
    if len(new_pin) == 4 and new_pin.isdigit():
        if new_pin in users:
            print("❌ This PIN already exists. Choose another one.")
            return old_pin
        users[new_pin] = users.pop(old_pin)  # update key in dict
        print("✅ PIN changed successfully! Please login again with new PIN.")
        return new_pin
    else:
        print("❌ Invalid PIN format! Must be 4 digits.")
        return old_pin

def atm_menu(user_pin):
    user = users[user_pin]
    while True:
        print(f"\n====== ATM MENU ({user['name']}) ======")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transactions")
        print("5. Change PIN")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(user)
        elif choice == "2":
            deposit(user)
        elif choice == "3":
            withdraw(user)
        elif choice == "4":
            view_transactions(user)
        elif choice == "5":
            new_pin = change_pin(user_pin, user)
            if new_pin != user_pin:
                return new_pin   # logout after PIN change
        elif choice == "6":
            print("✅ Thank you for using our ATM. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

    return user_pin  # return same PIN if not changed

# Main Program Loop
while True:
    print("\n====== Welcome to ATM Banking ======")
    user_pin = input("Enter your 4-digit PIN (or 'q' to quit): ")

    if user_pin.lower() == "q":
        print("👋 Exiting ATM system. Goodbye!")
        break

    if user_pin in users:
        print(f"✅ Welcome {users[user_pin]['name']}!\n")
        user_pin = atm_menu(user_pin)  # update if PIN changed
    else:
        print("❌ Incorrect PIN! Try again.") 
        

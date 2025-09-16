A simple Python-based ATM Banking System that allows users to check balance, deposit money, withdraw money, view transactions, and change their PIN.

🚀 Features

Login with PIN (simple authentication):

Check Balance – View current account balance.
Deposit Money – Add funds to your account.
Withdraw Money – Withdraw funds (with balance check).
View Transactions – See transaction history.
Change PIN – Update your PIN securely.
Exit Option – Quit the system anytime.

🛠️ Tech Stack
Language: Python 3

📂 Project Structure
atm3.py   # Main program file

▶️ How to Run
Clone the repository or download the project:

git clone <your-repo-link>
cd <your-repo-folder>

Run the program using Python:

python atm3.py


Enter your 4-digit PIN to log in (default users are defined in code).
👥 Default Users
users = {
    "1234": {"name": "Alice", "balance": 5000, "transactions": []},
    "5678": {"name": "Bob", "balance": 8000, "transactions": []},
    "4321": {"name": "Charlie", "balance": 10000, "transactions": []}
}
📸 Sample Menu

====== ATM MENU (Alice) ======
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. View Transactions
5. Change PIN
6. Exit
✅ Future Improvements

Add file/database storage for user data.
Implement account locking after multiple wrong PIN attempts.
Add interest calculations or advanced banking features.

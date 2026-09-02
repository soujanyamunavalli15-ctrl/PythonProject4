class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def display_balance(self):
        print("\n--- Account Details ---")
        print("Account Holder:", self.account_holder)
        print("Current Balance: ₹", self.balance)


# Main Program
name = input("Enter account holder name: ")
initial_balance = float(input("Enter initial balance: "))

account = BankAccount(name, initial_balance)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.display_balance()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print(" Deposit amount must be greater than zero.")
        else:
            self.balance += amount
            print(f" Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print(" Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print(" Insufficient balance.")
        else:
            self.balance -= amount
            print(f" Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def check_balance(self):
        print(f" Current balance: ${self.balance:.2f}")


class ATM:
    def __init__(self, account):
        self.account = account

    def menu(self):
        while True:
            print("\n===== ATM Menu =====")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.account.check_balance()
            elif choice == "2":
                try:
                    amount = float(input("Enter deposit amount: "))
                    self.account.deposit(amount)
                except ValueError:
                    print(" Invalid input. Please enter a number.")
            elif choice == "3":
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    self.account.withdraw(amount)
                except ValueError:
                    print(" Invalid input. Please enter a number.")
            elif choice == "4":
                print(" Thank you for using the ATM!")
                break
            else:
                print(" Invalid choice. Please select 1-4.")


# Main program
if __name__ == "__main__":
    user_account = BankAccount(balance=1000)  # Initial balance
    atm = ATM(user_account)
    atm.menu()

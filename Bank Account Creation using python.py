class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew {amount}. Remaining balance: {self.balance}")
        else:
            print("Insufficient balance.")

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Balance: {self.balance}")

def use_of_account(account):
    while True:
        print("\nSelect an option:")
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Display account details")
        print("4. Exit")
        
        select = input("Enter choice (1/2/3/4): ")

        if select == '1':
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif select == '2':
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif select == '3':
            account.display()

        elif select == '4':
            print("Exiting the system.")

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    account_number = input("Enter account number: ")
    holder_name = input("Enter account holder name: ")
    account = BankAccount(account_number, holder_name)

    use_of_account(account)

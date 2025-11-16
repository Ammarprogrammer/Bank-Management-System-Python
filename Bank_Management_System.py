import random
from datetime import datetime
import sys

class Account:
   def __init__(self, account_number, name, password,balance):
      self.account_number = str(account_number)
      self.name = str(name)
      self.password = str(password)
      self._balance = float(balance)

   def deposit(self,amount):
      self._balance += amount
   def withdraw(self,amount):
      self._balance -= amount
   def check_balance(self):
      return f'Your current balance are {self._balance}'
   def display_info(self):
      accounts_info = {"Account": self.name, "Balance": self._balance}
      return accounts_info

class Transaction:
    def __init__(self, account_number, transaction_type, amount, date_time):
       self.account_number = str(account_number)
       self.transaction_type = str(transaction_type)
       self.amount = float(amount)
       self.date_time = str(date_time)
    def format_transaction(self):
       Transaction = f'{self.account_number} | {self.transaction_type} | {self.amount} | {self.date_time}'
       return Transaction
    def record_transaction(self):
       self.date_time = datetime.now()
       if self.amount > 0:
          with open("transactions.txt", "a") as transaction:
             transaction.write(f'{self.format_transaction()}\n')
       else:
          return f'Invalid Transaction'      
    @staticmethod
    def get_transactions_by_account(account_number):
        print(f"\n Transaction History for Account {account_number}:\n")
        found = False
        try:
            with open("transactions.txt", "r") as file:
                for line in file:
                    if line.startswith(str(account_number)):
                        print(line.strip())
                        found = True
            if not found:
                print("No transactions found for this account yet.")
        except FileNotFoundError:
            print("No transaction history found. (transactions.txt missing)")

class BankSystem:
    def __init__(self):
        self.accounts = {}
        self.load_accounts()
    def create_account(self):
       name = input("Enter your name: ")
       while True:
           password = input("Enter your 5-digit numeric password: ")
           if len(password) == 5 and password.isnumeric():
             break  # valid password, exit loop
           else:
             print("❌ Invalid password! Please enter exactly 5 numeric digits.")        
       deposit = float(input("Initial deposit: "))
       account_number = str(random.randint(10000, 99999))  # generate 5-digit unique ID

       new_account = Account(account_number, name, password, deposit)
       self.accounts[account_number] = new_account
       Transaction(account_number, "Deposit", deposit, datetime.now()).record_transaction()
       
       # Append to file
       with open("accounts.txt", "a") as f:
            f.write(f"{account_number},{name},{password},{deposit}\n")
            print(f"Account created successfully! Your Account Number is {account_number}")
    def delete_account(self, account):
       confirm = input(f"Are you sure you want to delete your account {account.account_number}? (Y/N): ").upper()
       if confirm != "Y":
           print("❌ Account deletion canceled.")
           return

    # Optional: Verify password
       pwd = input("Enter your password to confirm: ")
       if pwd != account.password:
           print("❌ Incorrect password. Account not deleted.")
           return   
       # 1️⃣ Remove from memory
       if account.account_number in self.accounts:
           del self.accounts[account.account_number]

       # 2️⃣ Remove from accounts.txt
       lines = []
       with open("accounts.txt", "r") as f:
           lines = f.readlines()

       with open("accounts.txt", "w") as f:
           for line in lines:
              if not line.startswith(account.account_number):
                f.write(line)

       # 3️⃣ Remove transactions (optional)
       lines = []
       with open("transactions.txt", "r") as f:
           lines = f.readlines()

       with open("transactions.txt", "w") as f:
           for line in lines:
              if not line.startswith(account.account_number):
                f.write(line)

       print(f"✅ Account {account.account_number} deleted successfully.")        
    def save_accounts(self):
         with open("accounts.txt", "w") as f:
           for acc_no, acc_obj in self.accounts.items():
            f.write(f"{acc_no},{acc_obj.name},{acc_obj.password},{acc_obj._balance}\n")
    def load_accounts(self):
        try:
          with open("accounts.txt", "r") as f:
            for line in f:
                acc_no, name, password, balance = line.strip().split(",")
                account = Account(acc_no, name, password, float(balance))
                self.accounts[acc_no] = account
        except FileNotFoundError:
            open("accounts.txt", "w").close()  # create empty file if not found
    def login(self):
        acc_no = input("Enter account number: ")
        password = input("Enter password: ")
        if acc_no in self.accounts:
            account = self.accounts[acc_no]
            if account.password == password:
                print(f"Welcome {account.name}!")
                self.user_menu(account)
            else:
                print("❌ Incorrect password.")
        else:
            print("❌ Account not found.")
    def user_menu(self, account):
        while True:
            print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. View Transactions\n5. Delete Account\n6. Logout")
            choice = input("Select option: ")
        
            if choice == "1":
               self.deposit_money(account)
            elif choice == "2":
               self.withdraw_money(account)
            elif choice == "3":
               print(account.check_balance())
            elif choice == "4":
               self.view_transactions(account)
            elif choice == "5":
               self.delete_account(account)
               self.exit_system()
               break   
            elif choice == "6":
               self.exit_system()
               break
            else:
                print("Invalid choice.") 
    def deposit_money(self, account):
        amount = float(input("Enter Deposit amount here.."))
        account.deposit(amount)
        Transaction(account.account_number, "Deposit", amount, datetime.now()).record_transaction()
    def withdraw_money(self, account):
        amount = float(input("Enter Deposit amount here.."))
        account.withdraw(amount)
        Transaction(account.account_number, "Withdraw", amount, datetime.now()).record_transaction()
    def view_transactions(self, account):
        Transaction.get_transactions_by_account(account.account_number)
    def exit_system(self):
        BankSystem().save_accounts()   
        print("Sucessfully logout!") 
        sys.exit()
         
def main():
    print("🏦 WELCOME TO PYTHON BANK SYSTEM 🏦")
    bank = BankSystem()  # initialize and load accounts

    while True:
        print("\nMain Menu:")
        print("1. Create New Account")
        print("2. Login to Existing Account")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            bank.create_account()
        elif choice == "2":
            bank.login()
        elif choice == "3":
            bank.exit_system()
        else:
            print("❌ Invalid option! Please enter 1, 2, or 3.")


# Run the program
if __name__ == "__main__":
    main()

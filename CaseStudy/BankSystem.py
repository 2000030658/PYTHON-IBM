import csv
import threading
import time
from threading import Lock

# Customer Class
class Customer:
    def __init__(self, customer_id, name, balance, account_type):
        self.customer_id = customer_id
        self.name = name
        self.balance = balance
        self.account_type = account_type
        self.transaction_history = []
        self.lock = Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            self.transaction_history.append(f"Deposited {amount}")
            print(f"Deposited {amount} to account. New balance: {self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if amount > self.balance:
                print("Error: Insufficient funds.")
            else:
                self.balance -= amount
                self.transaction_history.append(f"Withdrew {amount}")
                print(f"Withdrew {amount} from account. New balance: {self.balance}")

    def apply_interest(self):
        if self.account_type == "Savings":
            with self.lock:
                interest = self.balance * 0.05  #5% interest for savings accounts
                self.balance += interest
                self.transaction_history.append(f"Applied interest: {interest}")
                print(f"Interest applied: {interest}. New balance: {self.balance}")

    def view_transaction_history(self):
        print(f"Transaction history for {self.name}:")
        for transaction in self.transaction_history:
            print(transaction)

# BankingSystem Class
class BankingSystem:
    def __init__(self):
        self.customers = {}
        self.lock = Lock()
        self.load_customers("data.csv")
        self.interest_thread = threading.Thread(target=self.periodic_interest, daemon=True)
        self.interest_thread.start()

    def load_customers(self, filename):
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  
                for row in reader:
                    customer_id, name, balance = row
                    self.customers[customer_id] = Customer(customer_id, name, float(balance), "Savings")
        except Exception as e:
            print(f"Error loading customer data: {e}")

    def periodic_interest(self):
        while True:
            time.sleep(10)  # Applying interest for every 10 seconds
            for customer in self.customers.values():
                customer.apply_interest()

    def get_customer(self, customer_id):
        return self.customers.get(customer_id)

    def customer_info(self, customer_id):
        customer = self.get_customer(customer_id)
        if customer:
            print(f"Customer ID: {customer.customer_id}")
            print(f"Name: {customer.name}")
            print(f"Balance: {customer.balance}")
            print(f"Account Type: {customer.account_type}")
        else:
            print("Customer not found.")


def BankSystem():
    banking_system = BankingSystem()
    
    while True:
        print("\nBanking System Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Transaction History")
        print("4. View Account Info")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            customer_id = input("Enter Customer ID: ")
            amount = float(input("Enter deposit amount: "))
            customer = banking_system.get_customer(customer_id)
            if customer:
                customer.deposit(amount)
            else:
                print("Customer not found.")
        
        elif choice == "2":
            customer_id = input("Enter Customer ID: ")
            amount = float(input("Enter withdrawal amount: "))
            customer = banking_system.get_customer(customer_id)
            if customer:
                customer.withdraw(amount)
            else:
                print("Customer not found.")
        
        elif choice == "3":
            customer_id = input("Enter Customer ID: ")
            customer = banking_system.get_customer(customer_id)
            if customer:
                customer.view_transaction_history()
            else:
                print("Customer not found.")
        
        elif choice == "4":
            customer_id = input("Enter Customer ID: ")
            banking_system.customer_info(customer_id)
        
        elif choice == "5":
            print("Exiting banking system.")
            break
        
        else:
            print("Invalid choice. Please try again.")

BankSystem()
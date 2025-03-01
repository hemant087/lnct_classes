import tkinter as tk
from tkinter import messagebox
import datetime

# Global accounts dictionary to store account details
accounts = {}

# Function to create an account
def create_account():
    account_number = account_number_entry.get()
    name = name_entry.get()
    password = password_entry.get()
    initial_balance = initial_balance_entry.get()

    if account_number in accounts:
        messagebox.showerror("Error", "Account number already exists!")
        return

    if not (account_number and name and password and initial_balance.isdigit()):
        messagebox.showerror("Error", "All fields are required, and balance must be a number!")
        return

    accounts[account_number] = {
        "name": name,
        "password": password,
        "balance": float(initial_balance),
        "transactions": []
    }
    messagebox.showinfo("Success", "Account created successfully!")
    clear_entries()

# Function to authenticate account
def authenticate(account_number, password):
    if account_number not in accounts:
        return False, "Account not found!"
    if accounts[account_number]["password"] != password:
        return False, "Incorrect password!"
    return True, accounts[account_number]

# Function to deposit money
def deposit():
    account_number = account_number_entry.get()
    password = password_entry.get()
    amount = amount_entry.get()

    if not amount.isdigit():
        messagebox.showerror("Error", "Deposit amount must be a number!")
        return

    valid, account = authenticate(account_number, password)
    if not valid:
        messagebox.showerror("Error", account)
        return

    account["balance"] += float(amount)
    account["transactions"].append(
        f"{datetime.datetime.now()} - Deposited ₹{amount}. Balance: ₹{account['balance']}"
    )
    messagebox.showinfo("Success", f"₹{amount} deposited successfully! New Balance: ₹{account['balance']}")
    clear_entries()

# Function to withdraw money
def withdraw():
    account_number = account_number_entry.get()
    password = password_entry.get()
    amount = amount_entry.get()

    if not amount.isdigit():
        messagebox.showerror("Error", "Withdrawal amount must be a number!")
        return

    valid, account = authenticate(account_number, password)
    if not valid:
        messagebox.showerror("Error", account)
        return

    amount = float(amount)
    if amount > account["balance"]:
        messagebox.showerror("Error", "Insufficient balance!")
        return

    account["balance"] -= amount
    account["transactions"].append(
        f"{datetime.datetime.now()} - Withdrew ₹{amount}. Balance: ₹{account['balance']}"
    )
    messagebox.showinfo("Success", f"₹{amount} withdrawn successfully! Remaining Balance: ₹{account['balance']}")
    clear_entries()

# Function to view account details
def view_account_details():
    account_number = account_number_entry.get()
    password = password_entry.get()

    valid, account = authenticate(account_number, password)
    if not valid:
        messagebox.showerror("Error", account)
        return

    details = f"Account Holder: {account['name']}\nBalance: ₹{account['balance']}"
    messagebox.showinfo("Account Details", details)
    clear_entries()

# Function to view transaction history
def view_transactions():
    account_number = account_number_entry.get()
    password = password_entry.get()

    valid, account = authenticate(account_number, password)
    if not valid:
        messagebox.showerror("Error", account)
        return

    if not account["transactions"]:
        messagebox.showinfo("Transaction History", "No transactions available.")
    else:
        history = "\n".join(account["transactions"])
        messagebox.showinfo("Transaction History", history)
    clear_entries()

# Function to clear input fields
def clear_entries():
    account_number_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    initial_balance_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

# Main application window
root = tk.Tk()
root.title("Bank Management System")

# Labels and entries for account information
tk.Label(root, text="Account Number:").grid(row=0, column=0, padx=10, pady=5)
account_number_entry = tk.Entry(root)
account_number_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Name:").grid(row=1, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Password:").grid(row=2, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Initial Balance:").grid(row=3, column=0, padx=10, pady=5)
initial_balance_entry = tk.Entry(root)
initial_balance_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Amount:").grid(row=4, column=0, padx=10, pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(row=4, column=1, padx=10, pady=5)

# Buttons for functionalities
tk.Button(root, text="Create Account", command=create_account).grid(row=5, column=0, padx=10, pady=10)
tk.Button(root, text="Deposit", command=deposit).grid(row=5, column=1, padx=10, pady=10)
tk.Button(root, text="Withdraw", command=withdraw).grid(row=6, column=0, padx=10, pady=10)
tk.Button(root, text="View Account Details", command=view_account_details).grid(row=6, column=1, padx=10, pady=10)
tk.Button(root, text="View Transactions", command=view_transactions).grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()

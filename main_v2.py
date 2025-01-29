import pickle
import os
import pathlib
import tkinter as tk
from tkinter import messagebox, simpledialog


class Account:
    def __init__(self):
        self.accNo = 0
        self.name = ''
        self.deposit = 0
        self.type = ''

    def create_account(self):
        self.accNo = simpledialog.askinteger("Account Number", "Enter the account number:")
        self.name = simpledialog.askstring("Account Holder Name", "Enter the account holder's name:")
        self.type = simpledialog.askstring(
            "Account Type",
            "Enter the type of account [C/S]:",
        ).upper()
        while self.type not in ['C', 'S']:
            messagebox.showerror("Invalid Input", "Please enter 'C' for Current or 'S' for Saving.")
            self.type = simpledialog.askstring(
                "Account Type",
                "Enter the type of account [C/S]:",
            ).upper()
        self.deposit = simpledialog.askinteger(
            "Initial Deposit",
            f"Enter the initial deposit (>=500 for Saving and >=1000 for Current):",
        )
        if (self.type == 'S' and self.deposit < 500) or (self.type == 'C' and self.deposit < 1000):
            messagebox.showerror("Insufficient Deposit", "Account creation failed. Insufficient deposit.")
            return None
        messagebox.showinfo("Success", "Account created successfully.")
        return self


def save_accounts(accounts):
    with open("accounts.data", "wb") as file:
        pickle.dump(accounts, file)


def load_accounts():
    file = pathlib.Path("accounts.data")
    if file.exists():
        with open("accounts.data", "rb") as file:
            return pickle.load(file)
    return []


def find_account(accounts, acc_no):
    for account in accounts:
        if account.accNo == acc_no:
            return account
    return None


def create_account(accounts):
    account = Account().create_account()
    if account:
        accounts.append(account)
        save_accounts(accounts)


def deposit_amount(accounts):
    acc_no = simpledialog.askinteger("Account Number", "Enter the account number:")
    account = find_account(accounts, acc_no)
    if account:
        amount = simpledialog.askinteger("Deposit Amount", "Enter the amount to deposit:")
        account.deposit += amount
        messagebox.showinfo("Success", f"Deposited {amount} successfully.\nNew Balance: {account.deposit}")
        save_accounts(accounts)
    else:
        messagebox.showerror("Error", "Account not found.")


def withdraw_amount(accounts):
    acc_no = simpledialog.askinteger("Account Number", "Enter the account number:")
    account = find_account(accounts, acc_no)
    if account:
        amount = simpledialog.askinteger("Withdraw Amount", "Enter the amount to withdraw:")
        if amount > account.deposit:
            messagebox.showerror("Error", "Insufficient balance. Withdrawal failed.")
        else:
            account.deposit -= amount
            messagebox.showinfo("Success", f"Withdrawn {amount} successfully.\nNew Balance: {account.deposit}")
            save_accounts(accounts)
    else:
        messagebox.showerror("Error", "Account not found.")


def balance_enquiry(accounts):
    acc_no = simpledialog.askinteger("Account Number", "Enter the account number:")
    account = find_account(accounts, acc_no)
    if account:
        messagebox.showinfo("Balance Enquiry", f"Account Balance: {account.deposit}")
    else:
        messagebox.showerror("Error", "Account not found.")


def display_all(accounts):
    if accounts:
        details = "\n".join(
            f"Account No: {acc.accNo}, Name: {acc.name}, Type: {acc.type}, Balance: {acc.deposit}" for acc in accounts
        )
        messagebox.showinfo("All Accounts", details)
    else:
        messagebox.showinfo("All Accounts", "No accounts found.")


def delete_account(accounts):
    acc_no = simpledialog.askinteger("Account Number", "Enter the account number:")
    account = find_account(accounts, acc_no)
    if account:
        accounts.remove(account)
        save_accounts(accounts)
        messagebox.showinfo("Success", "Account deleted successfully.")
    else:
        messagebox.showerror("Error", "Account not found.")


def modify_account(accounts):
    acc_no = simpledialog.askinteger("Account Number", "Enter the account number:")
    account = find_account(accounts, acc_no)
    if account:
        account.name = simpledialog.askstring("Modify Name", "Enter new account holder name:")
        account.type = simpledialog.askstring(
            "Modify Account Type", "Enter new account type [C/S]:"
        ).upper()
        while account.type not in ['C', 'S']:
            messagebox.showerror("Invalid Input", "Please enter 'C' for Current or 'S' for Saving.")
            account.type = simpledialog.askstring("Modify Account Type", "Enter new account type [C/S]:").upper()
        account.deposit = simpledialog.askinteger("Modify Balance", "Enter new balance:")
        save_accounts(accounts)
        messagebox.showinfo("Success", "Account details updated successfully.")
    else:
        messagebox.showerror("Error", "Account not found.")


def main_menu():
    accounts = load_accounts()

    root = tk.Tk()
    root.title("Bank Management System")

    tk.Label(root, text="Bank Management System", font=("Arial", 20), pady=20).pack()

    buttons = [
        ("Create New Account", lambda: create_account(accounts)),
        ("Deposit Amount", lambda: deposit_amount(accounts)),
        ("Withdraw Amount", lambda: withdraw_amount(accounts)),
        ("Balance Enquiry", lambda: balance_enquiry(accounts)),
        ("Display All Accounts", lambda: display_all(accounts)),
        ("Close an Account", lambda: delete_account(accounts)),
        ("Modify an Account", lambda: modify_account(accounts)),
        ("Exit", root.quit),
    ]

    for text, command in buttons:
        tk.Button(root, text=text, font=("Arial", 14), command=command, pady=10, width=25).pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    main_menu()

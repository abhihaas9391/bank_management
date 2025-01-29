# Bank Management System

## Overview
This is a simple Bank Management System built using Python and Tkinter. It allows users to create and manage bank accounts, deposit and withdraw money, and perform other banking operations. The application stores account data using Python's `pickle` module to ensure data persistence.

## Features
- **Create New Account**: Allows users to create a new bank account with an account number, name, account type (Current/Saving), and an initial deposit.
- **Deposit Amount**: Enables users to deposit money into an existing account.
- **Withdraw Amount**: Allows users to withdraw money from their account, ensuring sufficient balance.
- **Balance Enquiry**: Users can check their current account balance.
- **Display All Accounts**: Shows a list of all stored accounts with details such as account number, name, type, and balance.
- **Close an Account**: Users can delete an existing account.
- **Modify an Account**: Allows modification of account details such as name, account type, and balance.
- **Data Persistence**: The system uses file-based storage (`pickle`) to retain account data across sessions.

## Technologies Used
- Python
- Tkinter (GUI framework)
- `pickle` module for data storage

## Installation & Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/abhihaas9391/bank_management.git
   cd bank_management
   ```
2. Run the Python script:
   ```sh
   python main.py
   ```

## Requirements
- Python 3.x
- Tkinter (included with Python)

## Contributing
Feel free to submit pull requests for bug fixes or feature improvements.

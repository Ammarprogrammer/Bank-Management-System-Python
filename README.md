# 🏦 Python Bank Management System

A simple and beginner-friendly **Bank Management System in Python** using **Object-Oriented Programming (OOP)** and **File Handling** (`accounts.txt`, `transactions.txt`).  
This project supports account creation, secure login, deposits, withdrawals, and full transaction history tracking.

---

## 🚀 Features

### ✔ Create New Account
- User name input  
- 5-digit numeric password validation  
- Auto-generated 5-digit unique account number  
- Initial deposit stored in both account file & transaction history  

### ✔ Login to Existing Account  
- Password protected  
- Loads accounts from `accounts.txt`  
- Prevents login until account is saved in memory  

### ✔ Deposit & Withdraw Money
- Updates account balance  
- Saves each transaction in `transactions.txt`  
- Fully recorded with date & time  

### ✔ Check Balance
- Shows current balance instantly  

### ✔ Transaction History
- Displays all deposits & withdrawals for that specific account  
- Reads from `transactions.txt`  

### ✔ Persistent Storage
- `accounts.txt` → stores all accounts  
- `transactions.txt` → stores all transactions  

---

## 🛠 Technologies Used

- Python 3  
- OOP (Classes & Objects)  
- File Handling  
- Datetime module  

---

## 📘 How It Works

### 1️⃣ **Create Account**
User enters name → password → initial deposit  
Program generates unique 5-digit account number.

Stored in:
accounts.txt
transactions.txt

### 2️⃣ **Login**
User enters:
- Account Number  
- Password  

If matched → user menu opens.

### 3️⃣ **Deposit / Withdraw / Balance Check**
Each action updates:
- Memory (runtime)
- File storage
- Transaction record

### 4️⃣ **Transaction History**
Reads all lines from `transactions.txt` matching the account number.

---

## 📝 Sample Transaction Format
40528 | Deposit | 5000 | 2025-11-12 21:30:45.923842
40528 | Withdraw | 1000 | 2025-11-12 22:00:01.312582

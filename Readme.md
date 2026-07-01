# 🏦 Bank Management System

A simple console-based Bank Management System built with Python, demonstrating core Object-Oriented Programming (OOP) concepts including Inheritance, Encapsulation, Polymorphism, and Abstraction.

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [OOP Concepts Used](#oop-concepts-used)
- [Features](#features)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [Usage](#usage)
- [Technologies Used](#technologies-used)

---

## 📌 About the Project

This project simulates a basic banking system where users can create accounts, deposit and withdraw money, transfer funds, and apply interest — all through a simple CLI (Command Line Interface). Data is stored in memory using Python dictionaries and lists (no external database required).

---

## 🧠 OOP Concepts Used

| Concept | Where Applied |
|---|---|
| **Class & Object** | `BankAccount`, `SavingsAccount`, `CurrentAccount`, `Bank` classes |
| **Constructor (`__init__`)** | Initializes account details on object creation |
| **Encapsulation** | `_pin` is private; accessed only via `check_pin()` method |
| **Inheritance** | `SavingsAccount` and `CurrentAccount` inherit from `BankAccount` |
| **Polymorphism** | `withdraw()` and `account_type()` behave differently per class |
| **Abstraction** | `Bank` class hides internal logic from the menu/user |
| **`__str__` Method** | Custom object representation when printed |

---

## ✨ Features

- ✅ Create Savings or Current accounts
- ✅ Deposit and withdraw money
- ✅ Check account balance
- ✅ Transfer money between accounts
- ✅ Apply interest to Savings accounts (6%)
- ✅ Overdraft support for Current accounts (up to PKR 10,000)
- ✅ View all accounts in a formatted table
- ✅ PIN-protected transactions

---

## 📁 Project Structure

```
Semester_Project_BMS/
│
└── bank_management.py       # Main file containing all classes and CLI menu
```

---

## ▶️ How to Run

**Requirements:** Python 3.x

```bash
# Clone the repository
git clone https://github.com/saadalam862/Semester_Project_BMS.git

# Navigate to the folder
cd Semester_Project_BMS

# Run the program
python bank_management.py
```

---

## 💻 Usage

Once the program runs, you will see a menu:

```
------- MAIN MENU --------
1. Create New Account
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. Account Details
6. Transfer Money
7. Apply Interest (Savings)
8. Show All Accounts
0. Exit
```

Simply enter the number of your choice and follow the prompts.

---

## 🛠️ Technologies Used

- **Language:** Python 3
- **Paradigm:** Object-Oriented Programming (OOP)
- **Storage:** In-memory (Python dictionaries)
- **Interface:** Command Line Interface (CLI)

---

## 👨‍💻 Author

**Saad Alam**
- GitHub: [@saadalam862](https://github.com/saadalam862)

---

> 📚 *This project was developed as a Semester Project for the Object-Oriented Programming (OOP) course — 4th Semester.*
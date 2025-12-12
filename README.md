# Banking OOP Practice

**Version:** 0.1.0  
**Status:** Early practice / in progress  

This project is a **Python Object-Oriented Programming (OOP) Practice application**

---

## Project Goals

This project was built to:

- Learn **Python OOP fundamentals**
- learn how **classes manage state**
- work with **methods, user input, and control flow**
- practice ** semantic versioning** from the beginning of a project

Version 0.1.0 represents a functional starting point with known limitations.

---

## Features (v0.1.0)

- BankAccount class with:
  - Account owner
  - Account balance
  - Deposit method
  - Withdraw method
  - Balance display
- Two predefined accounts
- Command-line menu to:
  - Select which account to access
  - Deposit funds
  - Withdraw funds
  - View current balance

## How to run

python banking.py

## Example flow

- Program starts
- User selects an account (1 or 2)
- User chooses an action:
  - Deposit money
  - Withdraw Money
  - View Balance

All changes are applied to the account object in memory.

## Known limiations:

- No validation for negative deposits or overdrafts
- Withdrawl logic is currently incomplete
- No persisitent storage (data resets each run)
- Limited error handling
- Only supports two hardcoded accounts

## Planned improvements:

Potential future improvements include:

- Complete withdrawl/deposit logic with balance checks
- Input handling and improved error handling
- Unit tests
- File or database persistence

## What This Project Demonstrates

- Understanding of Python classes and methods
- Ability to model real-world systems using OOP
- Comfort with CLI-based applications
- Early adoption of software versioning best practices

## Final notes

This project is part of ongoing Python practice and is expected to evolve over time. Clarity and learning value are prioritezed over completeness.
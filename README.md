Expense Tracker System
A simple yet practical OOP project built in Python to record daily expenses, organize them by category, and keep track of spending in a structured way.



It combines OOP concepts with input validation and menu-driven interaction, making it a great beginner-friendly project that still feels complete and practical.

Features
Add a new expense.

Store expense title, amount, category, and date.

View all recorded expenses.

Calculate the total amount spent.

Display category-wise expense summary.

Handle invalid values safely.

Menu-driven interface for easy interaction.


OOP Concepts Used
This project demonstrates some core OOP concepts in a clean and understandable way:

Class and Object — each expense is created as an object.

Encapsulation — expense data and related methods are organized within classes.

Methods — used for adding, viewing, and summarizing expenses.

Data Management — expenses are stored and processed in a structured way.

Validation — ensures the program handles incorrect input properly.

Project Structure
python
class Expense
├── __init__()
└── display()

class ExpenseTracker
├── __init__()
├── add_expense()
├── view_expenses()
├── total_expense()
└── category_summary()
Along with these classes, helper functions are used for validating text, amount, category, and date inputs.

How it Works
The user selects an option from the menu.

If the user chooses to add an expense, the program asks for title, amount, category, and date.

All inputs are validated before being accepted.

The expense is stored inside the tracker.

The user can later view all expenses, check the total, or see a category-wise summary.


One of the most important parts of this project is that it does not blindly accept every input.

It checks for:

Empty fields.

Invalid numeric values.

Amounts less than or equal to zero.

Wrong category names.

Incorrect date format.

This makes the project more realistic, because real applications need to guide users and handle mistakes safely.


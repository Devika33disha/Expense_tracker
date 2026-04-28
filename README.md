Expense Tracker System
A simple yet practical OOP project built in Python to record daily expenses, organize them by category, and keep track of spending in a structured way.

This project is a small step toward building something that feels real, useful, and close to everyday life. Instead of creating just another logic-based program, this one focuses on a problem almost everyone can relate to — managing expenses.

Why this project?
While learning Object-Oriented Programming, it helps to build projects that are not only simple but also meaningful. The Expense Tracker System is one such project.

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

Sample Output
bash
=== Expense Tracker Menu ===
1. Add Expense
2. View Expenses
3. Show Total Expense
4. Category-wise Summary
5. Exit

Enter your choice: 1
Enter expense title: Lunch
Enter amount: ₹120

Categories: Food, Transport, Shopping, Bills, Entertainment, Other
Enter category: Food
Enter date (DD-MM-YYYY): 28-04-2026
Expense added successfully!
Input Validation
One of the most important parts of this project is that it does not blindly accept every input.

It checks for:

Empty fields.

Invalid numeric values.

Amounts less than or equal to zero.

Wrong category names.

Incorrect date format.

This makes the project more realistic, because real applications need to guide users and handle mistakes safely.

What makes this project impressive?
This project is simple in idea, but strong in execution.

It does not just store values — it organizes them, validates them, and presents them meaningfully. That makes it feel less like a basic coding exercise and more like a small real-world application.

It is also a good example of how OOP can make code cleaner, more reusable, and easier to understand.

Learning Outcome
By building this project, the following skills get stronger:

Applying OOP in a practical use case.

Designing multiple classes with clear roles.

Building menu-driven Python programs.

Validating user input properly.

Thinking beyond logic and focusing on user experience too.

Future Improvements
This project can be enhanced further by adding:

Delete expense feature.

Edit/update expense details.

Monthly expense report.

File handling to save records permanently.

Budget limit warning.

GUI or web version.

Final Note
The best beginner projects are not always the biggest ones.
Sometimes they are the ones that solve simple real-life problems in a clean way.

And this project is exactly that — small, practical, and a meaningful step in learning OOP through building.# Expense_tracker

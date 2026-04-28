class Expense:
    def __init__(self, title, amount, category, date):
        self.title = title
        self.amount = amount
        self.category = category
        self.date = date

    def display(self):
        return f"{self.title} | ₹{self.amount:.2f} | {self.category} | {self.date}"


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def view_expenses(self):
        if not self.expenses:
            print("\nNo expenses recorded yet.")
            return

        print("\n----- All Expenses -----")
        for i, expense in enumerate(self.expenses, start=1):
            print(f"{i}. {expense.display()}")

    def total_expense(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"\nTotal Expense: ₹{total:.2f}")

    def category_summary(self):
        if not self.expenses:
            print("\nNo expenses to summarize.")
            return

        summary = {}
        for expense in self.expenses:
            summary[expense.category] = summary.get(expense.category, 0) + expense.amount

        print("\n----- Category-wise Summary -----")
        for category, amount in summary.items():
            print(f"{category}: ₹{amount:.2f}")


def get_valid_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Invalid input! This field cannot be empty.")


def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: ₹"))
            if amount > 0:
                return amount
            else:
                print("Invalid input! Amount must be greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")


def get_valid_category():
    categories = ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Other"]
    print("\nCategories:", ", ".join(categories))

    while True:
        category = input("Enter category: ").strip().title()
        if category in categories:
            return category
        else:
            print("Invalid category! Please choose from the given list.")


def get_valid_date():
    while True:
        date = input("Enter date (DD-MM-YYYY): ").strip()
        parts = date.split("-")

        if len(parts) == 3 and all(part.isdigit() for part in parts):
            day, month, year = map(int, parts)
            if 1 <= day <= 31 and 1 <= month <= 12 and year > 0:
                return date

        print("Invalid date! Please enter in DD-MM-YYYY format.")


tracker = ExpenseTracker()

while True:
    print("\n=== Expense Tracker Menu ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Category-wise Summary")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        title = get_valid_text("Enter expense title: ")
        amount = get_valid_amount()
        category = get_valid_category()
        date = get_valid_date()

        expense = Expense(title, amount, category, date)
        tracker.add_expense(expense)
        print("Expense added successfully!")

    elif choice == "2":
        tracker.view_expenses()

    elif choice == "3":
        tracker.total_expense()

    elif choice == "4":
        tracker.category_summary()

    elif choice == "5":
        print("Exiting Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice! Please select from 1 to 5.")
expenses = []
total = 0.0


def show_menu():
    print("\n1. Add an expense")
    print("2. View total spent")
    print("3. View all expenses")
    print("4. Undo last expense")
    print("5. Clear all expenses")
    print("6. Exit")


def add_expense():
    global total

    description = input("What was this expense for? ").strip()
    if description == "":
        description = "Unnamed expense"

    amount = input("Enter the amount: ").strip()
    amount = amount.replace(" ", "")
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    expenses.append({"description": description, "amount": amount})
    total = total + amount
    print(f"Added {amount:.2f} for {description}.")
    print(f"Total Spent: {total:.2f}")


def view_total():
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return
    print(f"Total Spent: {total:.2f}")
    print(f"Number of expenses: {len(expenses)}")
    print(f"Average expense: {total / len(expenses):.2f}")


def view_all():
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return
    print("\n--- Expense Log ---")
    for number in range(len(expenses)):
        print(f"{number + 1}. {expenses[number]['description']:<20} {expenses[number]['amount']:.2f}")
    print("--------------------")
    print(f"{'TOTAL':<20} {total:.2f}")


def undo_last():
    global total

    if len(expenses) == 0:
        print("Nothing to undo.")
        return
    last = expenses.pop()
    total = total - last["amount"]
    print(f"Removed: {last['description']} ({last['amount']:.2f})")
    print(f"Total Spent: {total:.2f}")


def clear_expenses():
    global total

    if len(expenses) == 0:
        print("The expense log is already empty.")
        return
    expenses.clear()
    total = 0.0
    print("All expenses cleared. Total reset to 0.00")


def main():
    print("=== Expense Tracker ===")
    while True:
        show_menu()
        option = input("Choose an option (1-6): ").strip()

        if option == "1":
            add_expense()
        elif option == "2":
            view_total()
        elif option == "3":
            view_all()
        elif option == "4":
            undo_last()
        elif option == "5":
            clear_expenses()
        elif option == "6":
            print(f"Final total spent: {total:.2f}")
            print("Goodbye.")
            break
        else:
            print("Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()

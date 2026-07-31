from collections import defaultdict

from .models import Expense, ExpenseCreate
from .storage import load_expenses, save_expenses


def add_expense(expense: ExpenseCreate) -> Expense:
    """
    Create and store a new expense.
    """
    expenses = load_expenses()

    new_expense = Expense(**expense.model_dump())

    expenses.append(new_expense.model_dump(mode="json"))

    save_expenses(expenses)

    return new_expense


def get_all_expenses(category: str | None = None) -> list[Expense]:
    """
    Return all expenses.
    Optionally filter by category.
    """
    expenses = load_expenses()

    if category:
        expenses = [
            expense
            for expense in expenses
            if expense["category"].lower() == category.lower()
        ]

    return [Expense(**expense) for expense in expenses]


def get_summary() -> dict:
    """
    Calculate total expenses
    and totals grouped by category.
    """
    expenses = load_expenses()

    total = 0.0

    by_category = defaultdict(float)

    for expense in expenses:

        total += expense["amount"]

        by_category[expense["category"]] += expense["amount"]

    return {
        "total": total,
        "by_category": dict(by_category),
    }


def delete_expense(expense_id: str) -> bool:
    """
    Delete an expense by ID.
    """
    expenses = load_expenses()

    updated = [
        expense
        for expense in expenses
        if expense["id"] != expense_id
    ]

    if len(updated) == len(expenses):
        return False

    save_expenses(updated)

    return True
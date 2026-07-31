from collections import defaultdict
from typing import Any

from .models import Expense, ExpenseCreate
from .storage import load_expenses, save_expenses


def add_expense(expense: ExpenseCreate) -> Expense:
    """
    Create a new expense, save it to storage,
    and return the created expense.
    """
    expenses = load_expenses()

    new_expense = Expense(**expense.model_dump())

    expenses.append(
        new_expense.model_dump(
            mode="json",
            exclude_none=True,
        )
    )

    save_expenses(expenses)

    return new_expense


def get_all_expenses(category: str | None = None) -> list[Expense]:
    """
    Retrieve all expenses.

    If a category is provided, return only expenses
    that belong to that category.
    """
    expenses = load_expenses()

    if category:
        expenses = [
            expense
            for expense in expenses
            if expense["category"].lower() == category.lower()
        ]

    return [Expense(**expense) for expense in expenses]


def get_summary() -> dict[str, Any]:
    """
    Calculate the total amount spent across all expenses
    and provide a category-wise expense breakdown.
    """
    expenses = load_expenses()

    total = 0.0
    by_category = defaultdict(float)

    for expense in expenses:
        amount = expense["amount"]

        total += amount
        by_category[expense["category"]] += amount

    return {
        "total": total,
        "by_category": dict(by_category),
    }


def delete_expense(expense_id: str) -> bool:
    """
    Delete an expense by its unique ID.

    Returns:
        True if the expense was deleted.
        False if no matching expense exists.
    """
    expenses = load_expenses()

    updated_expenses = [
        expense
        for expense in expenses
        if expense["id"] != expense_id
    ]

    if len(updated_expenses) == len(expenses):
        return False

    save_expenses(updated_expenses)

    return True
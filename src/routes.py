from typing import Optional

from fastapi import APIRouter, HTTPException, Query, status

from .models import Expense, ExpenseCreate, ExpenseSummary
from .services import (
    add_expense,
    delete_expense,
    get_all_expenses,
    get_summary,
)

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"],
)


@router.post(
    "",
    response_model=Expense,
    status_code=status.HTTP_201_CREATED,
    summary="Add a new expense",
)
def create_expense(expense: ExpenseCreate) -> Expense:
    """
    Create a new expense and store it.
    """
    return add_expense(expense)


@router.get(
    "",
    response_model=list[Expense],
    summary="Get all expenses",
)
def list_expenses(
    category: Optional[str] = Query(
        default=None,
        description="Filter expenses by category",
    ),
) -> list[Expense]:
    """
    Retrieve all expenses.

    Optionally filter expenses by category.
    """
    return get_all_expenses(category)


@router.get(
    "/summary",
    response_model=ExpenseSummary,
    summary="Get expense summary",
)
def expense_summary() -> ExpenseSummary:
    """
    Calculate the total expenses and
    provide a category-wise summary.
    """
    summary = get_summary()

    return ExpenseSummary(
        total=summary["total"],
        by_category=summary["by_category"],
    )


@router.delete(
    "/{expense_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete an expense",
)
def remove_expense(expense_id: str) -> None:
    """
    Delete an expense by its unique ID.
    """
    deleted = delete_expense(expense_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expense not found",
        )

    return None
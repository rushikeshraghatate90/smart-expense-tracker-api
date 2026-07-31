import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class ExpenseCreate(BaseModel):
    """
    Request model for creating a new expense.
    """

    title: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Expense title",
    )
    amount: float = Field(
        ...,
        gt=0,
        description="Expense amount",
    )
    category: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Expense category",
    )
    date: datetime.date = Field(
        ...,
        description="Expense date",
    )


class Expense(BaseModel):
    """
    Expense model stored in the application.
    """

    id: UUID = Field(
        default_factory=uuid4,
        description="Unique expense identifier",
    )
    title: str
    amount: float
    category: str
    date: datetime.date


class ExpenseSummary(BaseModel):
    """
    Expense summary grouped by category.
    """

    total: float
    by_category: dict[str, float]
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data.json"


def initialize_storage() -> None:
    """Create the JSON file if it doesn't exist."""
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")


def load_expenses() -> list[dict]:
    """Load all expenses from the JSON file."""
    initialize_storage()

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_expenses(expenses: list[dict]) -> None:
    """Save all expenses to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)
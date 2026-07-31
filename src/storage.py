import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data.json"


def initialize_storage() -> None:
    """Create the data file if it doesn't exist."""
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")


def load_expenses() -> list[dict]:
    """
    Load all expenses from the JSON file.

    Returns an empty list if the file is empty or contains invalid JSON.
    """
    initialize_storage()

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            content = file.read().strip()

            if not content:
                return []

            return json.loads(content)

    except json.JSONDecodeError:
        return []


def save_expenses(expenses: list[dict]) -> None:
    """Save expenses to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)
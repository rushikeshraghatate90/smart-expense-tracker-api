import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

# Add the project root to the Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.main import app
import src.storage as storage

@pytest.fixture
def client(tmp_path, monkeypatch):
    """
    Create a temporary data file for each test.

    Each test uses its own JSON file so tests remain isolated
    and do not modify the application's actual data.json.
    """
    temp_data = tmp_path / "data.json"
    temp_data.write_text("[]", encoding="utf-8")

    # Redirect storage to the temporary file
    monkeypatch.setattr(storage, "DATA_FILE", temp_data)

    return TestClient(app)

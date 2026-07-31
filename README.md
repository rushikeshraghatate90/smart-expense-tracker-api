<p align="center">

# 💰 Smart Expense Tracker API

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.141-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-10%20Passing-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-E92063?style=for-the-badge)
![OpenAPI](https://img.shields.io/badge/OpenAPI-Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)
![JSON](https://img.shields.io/badge/Storage-JSON-000000?style=for-the-badge&logo=json)

</p>

<p align="center">
A lightweight REST API built with <b>FastAPI</b> for managing personal expenses.<br>
Built for the <b>Software Engineering Apprenticeship Program 2026</b> take-home assignment.
</p>

---

## 📖 Overview

The **Smart Expense Tracker API** is a RESTful backend service that lets a user record, view, filter, summarize, and delete personal expenses. It was built to cover the core requirements of the take-home assignment:

- Add an expense (`id`, `title`, `amount`, `category`, `date`)
- View all expenses
- Filter expenses by category
- Calculate total expenses (overall and by category)
- Delete an expense

Data is persisted locally to a JSON file — no external database is required, and no additional services need to be installed or running.

---

## ✨ Features

- ✅ Add a new expense
- ✅ View all expenses
- ✅ Filter expenses by category
- ✅ Calculate total expenses (overall + per-category breakdown)
- ✅ Delete an expense by ID
- ✅ Automatic UUID generation for each expense
- ✅ Request validation (required fields, positive amounts, valid dates)
- ✅ Local JSON file storage (no database setup needed)
- ✅ Interactive Swagger UI and ReDoc documentation
- ✅ Automated pytest test suite (10/10 passing)

---

## 🛠 Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.12+ | Programming language |
| FastAPI | REST API framework |
| Pydantic v2 | Request/response validation |
| Uvicorn | ASGI server |
| Pytest | Automated testing |
| JSON file | Local data storage |
| Swagger / OpenAPI | Interactive API documentation |

---

## 📂 Project Structure

```text
smart-expense-tracker-api/
├── README.md              # This file
├── AI_NOTES.md            # Notes on AI tool usage during development
├── requirements.txt       # Python dependencies
│
├── src/
│   ├── __init__.py
│   ├── main.py             # FastAPI app entry point
│   ├── routes.py           # API route definitions
│   ├── services.py         # Business logic (add/filter/summarize/delete)
│   ├── models.py           # Pydantic request/response models
│   ├── storage.py          # JSON file read/write helpers
│   └── data.json           # Local expense data store
│
└── tests/
    ├── conftest.py          # Pytest fixtures (isolated test storage)
    └── test_api.py          # API test suite
```

---

## 🏗 Architecture

The project is split into four layers, each with one responsibility:

- **`main.py`** – creates the FastAPI app and mounts the routes.
- **`routes.py`** – defines HTTP endpoints and delegates to `services.py`. No business logic lives here.
- **`services.py`** – business logic: adding, filtering, summarizing, and deleting expenses.
- **`models.py`** – Pydantic models for request/response validation.
- **`storage.py`** – reads and writes `data.json`. The only layer that touches the storage format.
- **`tests/`** – pytest suite, run against a temporary, isolated data file.

### Request Flow

```
Client
  ↓
FastAPI Route     (routes.py — validates request, calls service)
  ↓
Service Layer     (services.py — applies business logic)
  ↓
Storage Layer     (storage.py — reads/writes data.json)
  ↓
JSON File         (data.json — persisted data)
  ↓
Response
```

Example: `POST /expenses` hits the route, which calls `services.add_expense()`. That function generates a UUID, builds the record, and calls `storage.save()` to persist it. The saved record is returned as the response.

---

## ✅ Prerequisites

Before you begin, make sure you have the following installed on your PC:

- **Python 3.12 or later** — check with:
  ```bash
  python --version
  ```
- **pip** (comes bundled with Python)
- **git** (to clone the repository)

---

## 🚀 Getting Started (Step-by-Step, for a Fresh PC)

### 1. Clone the repository

```bash
git clone https://github.com/rushikeshraghatate90/smart-expense-tracker-api.git
cd smart-expense-tracker-api
```

### 2. Create and activate a virtual environment

**Windows (PowerShell / cmd):**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

You'll know it worked if your terminal prompt now shows `(.venv)` at the start of the line.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API server

```bash
uvicorn src.main:app --reload
```

You should see output similar to:

```text
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Application startup complete.
```

The API is now running locally at:

```
http://127.0.0.1:8000
```

### 5. Open the interactive API docs

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

From Swagger UI you can try every endpoint directly in your browser — no separate tool needed.

### 6. Stop the server

Press `CTRL+C` in the terminal where it's running.

---

## 🧪 Running the Test Suite

With the virtual environment still activated, run:

```bash
python -m pytest -v
```

Expected output:

```text
======================== test session starts ========================
tests/test_api.py::test_add_expense PASSED
tests/test_api.py::test_get_expenses PASSED
tests/test_api.py::test_filter_by_category PASSED
tests/test_api.py::test_expense_summary PASSED
tests/test_api.py::test_delete_expense PASSED
tests/test_api.py::test_delete_nonexistent_expense PASSED
tests/test_api.py::test_invalid_amount PASSED
tests/test_api.py::test_missing_required_field PASSED
tests/test_api.py::test_empty_expense_list PASSED
tests/test_api.py::test_empty_summary PASSED

======================== 10 passed in 0.42s =========================
```

Tests run against a temporary JSON file created by a pytest fixture, not `src/data.json`, so running the suite never modifies real application data. Each test session starts with a clean file.

---

## 📚 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/expenses` | Add a new expense |
| `GET` | `/expenses` | Get all expenses |
| `GET` | `/expenses?category=Food` | Filter expenses by category |
| `GET` | `/expenses/summary` | Get total + per-category summary |
| `DELETE` | `/expenses/{expense_id}` | Delete an expense by ID |

### Add an expense

```
POST /expenses
```

Request body:
```json
{
  "title": "Lunch",
  "amount": 250,
  "category": "Food",
  "date": "2026-07-31"
}
```

Response (`201 Created`):
```json
{
  "id": "3f6a9e2e-6f0e-4a1a-8b0d-2f9d4c1a7b10",
  "title": "Lunch",
  "amount": 250,
  "category": "Food",
  "date": "2026-07-31"
}
```

### Get all expenses

```
GET /expenses
```

Response:
```json
[
  {
    "id": "3f6a9e2e-6f0e-4a1a-8b0d-2f9d4c1a7b10",
    "title": "Lunch",
    "amount": 250,
    "category": "Food",
    "date": "2026-07-31"
  }
]
```

### Filter by category

```
GET /expenses?category=Food
```

Returns only the expenses whose `category` matches, using the same response shape as above.

### Expense summary

```
GET /expenses/summary
```

Response:
```json
{
  "total": 550,
  "by_category": {
    "Food": 250,
    "Travel": 300
  }
}
```

### Delete an expense

```
DELETE /expenses/{expense_id}
```

- `204 No Content` on success
- `404 Not Found` if the ID doesn't exist

---

## ✅ Validation Rules

- `title`, `amount`, `category`, and `date` are all required.
- `amount` must be a positive number.
- `date` must be a valid `YYYY-MM-DD` date string.
- `id` is generated automatically as a UUID rather than an incrementing integer, so it stays unique without a persisted counter.
- All validation is enforced via Pydantic models, so invalid requests return a `422 Unprocessable Entity` with details on what failed.

---

## 🧪 Test Coverage

The automated suite covers:

- Adding an expense
- Retrieving all expenses
- Filtering by category
- Calculating the summary (total + by category)
- Deleting an expense
- Deleting a non-existent expense (error case)
- Rejecting an invalid (non-positive) amount
- Rejecting a request with a missing required field
- Behavior with an empty expense list
- Behavior with an empty summary

**Result:** 10 / 10 tests passing.

---

## 💾 Data Storage

Expenses are stored locally in:

```
src/data.json
```

This file is created automatically the first time you add an expense if it doesn't already exist. No database installation or setup is required.

---

## 📌 Design Decisions

- **FastAPI** – reduces boilerplate for request parsing and validation, and provides Swagger/ReDoc docs with no extra setup.
- **JSON file storage** – no database was required for this assignment, so a flat file keeps the project dependency-free. Trade-off: not safe for concurrent writes, which is why a real database is listed under Future Improvements.
- **Layered structure (routes → services → storage)** – keeps business logic testable independently of the HTTP layer and the storage format.
- **UUIDs instead of incremental IDs** – avoids needing a persisted counter and stays unique even if entries are deleted.
- **Pytest fixtures with a temporary data file** – test runs never touch or modify `src/data.json`.

---

## 🧩 Challenges Faced

- **Missing `data.json` on first run** – storage functions check for the file and create it with an empty structure if it doesn't exist, so the app works on a fresh clone before any expense is added.
- **Status code selection** – used `201` for a successful add and `204` for a successful delete, with `404` for deleting a missing ID, instead of defaulting everything to `200`.
- **Test data isolation** – early test runs wrote to the same `data.json` used for manual testing. Fixed by adding a pytest fixture that points the app at a temporary file for the test session.
- **Business logic in routes** – filtering and summary logic initially lived in `routes.py`. Moved to `services.py` to keep it testable independently of the HTTP layer.

---

## 🔮 Future Improvements

The current implementation covers the assignment's requirements but has clear limits beyond a local, single-user demo:

- **Swap JSON storage for SQLite/PostgreSQL** – removes the concurrent-write risk of a flat file.
- **Add an "update expense" endpoint** – rounds out basic CRUD; expenses currently can only be added or deleted.
- **Add pagination for `GET /expenses`** – avoids returning the full list as the file grows.
- **Add basic authentication** – restricts access, since any client can currently read or delete any expense.
- **Add Docker support** – removes manual environment setup across machines.
- **Add CI (GitHub Actions)** – catches failing tests before they're pushed.

---

## 📊 Project Highlights

- RESTful API built with FastAPI
- Layered architecture (Routes → Services → Storage)
- Local JSON-based persistence
- Automatic UUID generation
- Pydantic request validation
- Interactive Swagger & ReDoc documentation
- Automated pytest suite with isolated test data
- 10 / 10 passing automated tests

---
## 👨‍💻 Author

**Rushikesh Raghatate**

- GitHub: [https://github.com/rushikeshraghatate90](https://github.com/rushikeshraghatate90)
- Repository: [https://github.com/rushikeshraghatate90/smart-expense-tracker-api](https://github.com/rushikeshraghatate90/smart-expense-tracker-api)

---

## 📄 Note

This project was developed as part of the Software Engineering Apprenticeship Program 2026 take-home assignment. The repository also includes `AI_NOTES.md`, which documents how AI tools were used during development, as requested in the assignment instructions.

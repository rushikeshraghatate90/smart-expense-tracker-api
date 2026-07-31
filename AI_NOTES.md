# AI_NOTES.md

# AI Usage Report – Smart Expense Tracker API

## Overview

This document explains how AI tools were used during the development of this project, what changes were made after reviewing AI-generated suggestions, and which suggestions were intentionally not included in the final implementation.

I used ChatGPT as a development assistant throughout this assignment. AI was primarily used to review code, suggest improvements, generate initial drafts for some components, explain errors during debugging, and improve documentation.

Every AI-generated suggestion was reviewed, tested, and modified where necessary before becoming part of the final project. The final implementation was assembled, integrated, tested, and verified by me.

---

# 1. Which parts were AI-assisted vs. implemented by me

## My contribution

I was responsible for the overall implementation of the project, including:

- Creating the GitHub repository and project structure.
- Setting up the FastAPI application and virtual environment.
- Organizing the project into separate modules (`routes.py`, `services.py`, `models.py`, `storage.py`, and `tests`).
- Integrating the API routes, business logic, models, and storage into a working application.
- Configuring JSON-based local storage.
- Running the application locally and manually testing every endpoint through Swagger UI.
- Debugging runtime errors and fixing issues that appeared during development.
- Running the automated test suite and resolving failures until all tests passed.
- Reviewing the final project before submission.

## AI-assisted work

AI was mainly used to assist with:

- Reviewing the project structure.
- Suggesting improvements to FastAPI endpoint implementations.
- Drafting parts of the Pydantic models and validation rules.
- Improving function documentation and type hints.
- Suggesting better HTTP status codes and API documentation.
- Generating an initial version of the pytest test cases.
- Improving JSON file handling.
- Reviewing imports and code readability.
- Assisting with the README structure and documentation.

AI suggestions were treated as recommendations rather than final solutions. I reviewed each suggestion before deciding whether to use, modify, or discard it.

---

# 2. What I validated, tested, or changed

I did not assume AI-generated code was correct.

For every significant suggestion, I followed the same process:

1. Read and understood the generated code.
2. Integrated it into the project where appropriate.
3. Ran the application locally.
4. Tested the functionality using Swagger UI.
5. Executed the automated test suite.
6. Modified or rejected the suggestion if it did not match the project requirements.

Examples of changes made after reviewing AI suggestions include:

| AI Suggestion | What I Changed | Reason |
|--------------|----------------|--------|
| Pydantic validation rules | Updated validation and fixed compatibility issues | To match the project requirements and ensure compatibility with the installed Pydantic version |
| JSON storage | Improved handling of missing or empty JSON files | Prevented runtime errors during the first execution |
| DELETE endpoint | Returned **204 No Content** and added **404 Not Found** handling | Better follows REST API conventions |
| Test fixture | Switched from the real `data.json` file to a temporary file | Prevented automated tests from modifying application data |
| Function documentation | Rewrote several docstrings | Made the documentation clearer and more specific |
| Imports | Removed unused imports and simplified modules | Improved readability and code quality |

Every accepted change was verified before being included in the final repository.

---

# 3. AI suggestions I decided not to use

During development, AI suggested several additional features that were beyond the scope of the assignment.

I intentionally chose not to include them because I wanted the project to remain focused on the required functionality.

These included:

- Database integration (SQLite or PostgreSQL)
- User authentication
- Expense update endpoint
- Search functionality
- Pagination
- Docker containerization
- ORM integration
- Advanced logging
- CI/CD configuration
- Caching

Although these features could improve a larger application, they would add unnecessary complexity to an assignment that explicitly allows local JSON storage and is intended to be completed within a limited time.

---

# 4. Testing performed

The project was tested using both manual and automated testing.

## Manual Testing

I verified every endpoint using the FastAPI Swagger interface.

The following functionality was tested manually:

- Adding an expense
- Retrieving all expenses
- Filtering expenses by category
- Expense summary calculation
- Deleting an expense
- Validation for invalid requests

## Automated Testing

The project includes a pytest test suite covering:

- Add expense
- Retrieve all expenses
- Filter by category
- Expense summary
- Delete expense
- Delete non-existent expense
- Invalid amount validation
- Missing required field validation
- Empty expense list
- Empty summary

The test suite was executed using:

```bash
python -m pytest -v
```

Final Result:

- **10 automated tests**
- **10 tests passed**

---

# 5. Reflection

AI helped speed up development by providing implementation suggestions, improving documentation, generating initial test cases, and assisting during debugging.

However, AI was used as a development assistant rather than a replacement for implementation. Every suggestion was reviewed, tested, and modified where necessary before being included in the project.

Working this way helped me better understand the implementation while improving the overall quality, readability, and reliability of the final solution.
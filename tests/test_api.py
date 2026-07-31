from uuid import UUID


def test_add_expense(client):
    response = client.post(
        "/expenses",
        json={
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-07-31",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Lunch"
    assert data["amount"] == 250
    assert data["category"] == "Food"

    UUID(data["id"])


def test_get_all_expenses(client):
    client.post(
        "/expenses",
        json={
            "title": "Coffee",
            "amount": 100,
            "category": "Food",
            "date": "2026-07-31",
        },
    )

    response = client.get("/expenses")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_filter_expenses_by_category(client):
    client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 300,
            "category": "Food",
            "date": "2026-07-31",
        },
    )

    client.post(
        "/expenses",
        json={
            "title": "Movie",
            "amount": 500,
            "category": "Entertainment",
            "date": "2026-07-31",
        },
    )

    response = client.get("/expenses?category=Food")

    assert response.status_code == 200

    expenses = response.json()

    assert len(expenses) == 1
    assert expenses[0]["category"] == "Food"


def test_expense_summary(client):
    client.post(
        "/expenses",
        json={
            "title": "Burger",
            "amount": 200,
            "category": "Food",
            "date": "2026-07-31",
        },
    )

    client.post(
        "/expenses",
        json={
            "title": "Taxi",
            "amount": 300,
            "category": "Travel",
            "date": "2026-07-31",
        },
    )

    response = client.get("/expenses/summary")

    assert response.status_code == 200

    summary = response.json()

    assert summary["total"] == 500
    assert summary["by_category"]["Food"] == 200
    assert summary["by_category"]["Travel"] == 300


def test_delete_expense(client):
    response = client.post(
        "/expenses",
        json={
            "title": "Book",
            "amount": 450,
            "category": "Education",
            "date": "2026-07-31",
        },
    )

    expense_id = response.json()["id"]

    delete_response = client.delete(f"/expenses/{expense_id}")

    assert delete_response.status_code == 204

    response = client.get("/expenses")

    assert response.json() == []


def test_delete_nonexistent_expense(client):
    response = client.delete(
        "/expenses/00000000-0000-0000-0000-000000000000"
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Expense not found"


def test_invalid_amount(client):
    response = client.post(
        "/expenses",
        json={
            "title": "Coffee",
            "amount": -50,
            "category": "Food",
            "date": "2026-07-31",
        },
    )

    assert response.status_code == 422


def test_missing_required_field(client):
    response = client.post(
        "/expenses",
        json={
            "amount": 100,
            "category": "Food",
            "date": "2026-07-31",
        },
    )

    assert response.status_code == 422


def test_empty_expense_list(client):
    response = client.get("/expenses")

    assert response.status_code == 200
    assert response.json() == []


def test_empty_summary(client):
    response = client.get("/expenses/summary")

    assert response.status_code == 200

    summary = response.json()

    assert summary["total"] == 0
    assert summary["by_category"] == {}
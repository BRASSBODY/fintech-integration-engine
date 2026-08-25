# tests/test_db_verification.py
def test_user_status_in_db(db_connection):
    """Verifies that user record exists and is active in database."""
    user = next(u for u in db_connection["users"] if u["username"] == "standard_user")
    assert user["status"] == "active"
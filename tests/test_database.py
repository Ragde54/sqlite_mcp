import pytest


@pytest.mark.asyncio
async def test_database_fixture_loads_data(db):
    """
    Test that the database fixture correctly loads the schema and the seed data.
    """
    result = await db.run_query("SELECT COUNT(*) as count FROM categories;")

    assert "error" not in result
    assert result["rows"][0][0] == 3  # As per seed.sql: health, learning, work

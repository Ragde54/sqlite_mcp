import pytest
import sqlite3
import tempfile
import os
from pathlib import Path
from habit_tracker_mcp.database import Database

# Paths to your SQL files
ROOT_DIR = Path(__file__).parent.parent
SCHEMA_FILE = ROOT_DIR / "data" / "seed.sql"
TEST_DATA_FILE = ROOT_DIR / "tests" / "fixtures" / "seed.sql"


@pytest.fixture
def db_path():
    # Create a temporary file for the database
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)

    # Connect synchronously to set up schema and data
    conn = sqlite3.connect(path)

    # 1. Read and apply the main schema to create tables
    with open(SCHEMA_FILE, "r") as f:
        conn.executescript(f.read())

    # 2. Read and apply the test data into the newly created tables
    with open(TEST_DATA_FILE, "r") as f:
        conn.executescript(f.read())

    conn.close()

    yield path

    # Clean up the temporary file after tests run
    os.unlink(path)


@pytest.fixture
def db(db_path):
    # Return a Database instance pointed at the temporary file
    return Database(db_path)

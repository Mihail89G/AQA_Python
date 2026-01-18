import pytest
from sqlalchemy import text
from db import get_engine

@pytest.fixture(scope="module")
def engine():
    return get_engine()

@pytest.fixture(autouse=True)
def cleanup(engine):
    with engine.connect() as conn:
        conn.execute(text("IF OBJECT_ID('dbo.users', 'U') IS NOT NULL DROP TABLE dbo.users;"))
        conn.commit()
    yield
    with engine.connect() as conn:
        conn.execute(text("IF OBJECT_ID('dbo.users', 'U') IS NOT NULL DROP TABLE dbo.users;"))
        conn.commit()

def test_connection(engine):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        assert result.scalar() == 1

def test_create_table(engine):
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE dbo.users (
                id INT IDENTITY(1,1) PRIMARY KEY,
                name NVARCHAR(50)
            );
        """))
        conn.commit()

        result = conn.execute(text("""
            SELECT COUNT(*) 
            FROM INFORMATION_SCHEMA.TABLES 
            WHERE TABLE_NAME='users';
        """))
        assert result.scalar() == 1

def test_insert_select(engine):
    with engine.connect() as conn:
        conn.execute(text("INSERT INTO dbo.users (name) VALUES (N'Петро');"))
        conn.execute(text("INSERT INTO dbo.users (name) VALUES (N'Оля');"))
        conn.commit()

        result = conn.execute(text("SELECT COUNT(*) FROM dbo.users;"))
        assert result.scalar() == 2

def test_update(engine):
    with engine.connect() as conn:
        conn.execute(text("UPDATE dbo.users SET name = N'Олексій' WHERE name = N'Петро';"))
        conn.commit()

        result = conn.execute(text("SELECT name FROM dbo.users WHERE name = N'Олексій';"))
        assert result.scalar() == 'Олексій'

def test_delete(engine):
    with engine.connect() as conn:
        conn.execute(text("DELETE FROM dbo.users WHERE name = N'Оля';"))
        conn.commit()

        result = conn.execute(text("SELECT COUNT(*) FROM dbo.users;"))
        assert result.scalar() == 1

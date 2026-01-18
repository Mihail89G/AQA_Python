from sqlalchemy import text
from db import get_engine

def save_user(name: str):
    engine = get_engine()
    with engine.connect() as conn:
        conn.execute(text("INSERT INTO users (name) VALUES (:name)"), {"name": name})
        conn.commit()

if __name__ == "__main__":
    save_user("TestUser")
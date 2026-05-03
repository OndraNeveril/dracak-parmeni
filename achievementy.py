import sqlite3
from pathlib import Path

DB_PATH = "data/app.db"

def rebuild_db():
    Path("data").mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    with open("seed.sql") as f:
        conn.executescript(f.read())

    conn.commit()
    conn.close()


def get_all():
    with sqlite3.connect(DB_PATH) as conn:
        return conn.execute("SELECT * FROM items").fetchall()


def update_value(item_id, new_value):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "UPDATE items SET value = ? WHERE id = ?",
            (new_value, item_id)
        )
        conn.commit()

if not Path(DB_PATH).exists():
    rebuild_db()
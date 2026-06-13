from fastmcp import FastMCP
import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), 'expenses.db')

mcp = FastMCP("Expense Tracker")

def init_db():
    with sqlite3.connect(DB_PATH) as c:
        c.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                subcategory TEXT DEFAULT '',
                note TEXT DEFAULT ''
            )
        """)
        # Backward-compatible migration [safe upgrade for existing databases]
        existing_columns = [row[1] for row in c.execute("PRAGMA table_info(expenses)")]
        if "subcategory" not in existing_columns:
            c.execute("ALTER TABLE expenses ADD COLUMN subcategory TEXT DEFAULT ''")

init_db()

@mcp.tool()
def add_expenses(date, amount, category, subcategory="", note=""):
    """Add new expense to the Tracker"""
    with sqlite3.connect(DB_PATH) as c:
        cur = c.execute(
            "INSERT INTO expenses (date, amount, category, subcategory, note) VALUES (?,?,?,?,?)",
            (date, amount, category, subcategory, note)
        )
        return {"status": "success", "id": cur.lastrowid}

@mcp.tool()
def get_summary():
    """Get the summary of expenses from my DB"""
    with sqlite3.connect(DB_PATH) as c:
        cur = c.execute(
            "SELECT id, date, amount, category, subcategory, note FROM expenses ORDER BY id ASC"
        )
        cols = [d[0] for d in cur.description]
        return [dict(zip(cols, rows)) for rows in cur.fetchall()]

if __name__ == "__main__":
    mcp.run()
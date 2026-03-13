import sqlite3
import aiosqlite


class Database:
    def __init__(self, db_path: str):
        self.db_path = db_path

    async def run_query(self, sql: str) -> dict:
        async with aiosqlite.connect(self.db_path) as db:
            try:
                cursor = await db.execute(sql)
                await db.commit()

                if cursor.description is not None:
                    columns = [desc[0] for desc in cursor.description]
                    rows = await cursor.fetchall()
                    return {"columns": columns, "rows": [list(r) for r in rows]}
                else:
                    return {"columns": [], "rows": [], "rowcount": cursor.rowcount}

            except sqlite3.DatabaseError as e:
                return {"error": str(e), "columns": [], "rows": []}
        
        
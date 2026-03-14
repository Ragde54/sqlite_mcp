from typing import Any

from mcp.server.fastmcp import FastMCP
from sqlalchemy import text

from .database import engine

server = FastMCP("habit-tracker-mcp")


@server.tool()
def run_query(sql: str) -> dict[str, Any]:
    """Execute a SQL query against the database."""
    with engine.connect() as conn:
        try:
            result = conn.execute(text(sql))
            conn.commit()

            if result.returns_rows:
                columns = list(result.keys())
                rows = [list(row) for row in result.fetchall()]
                return {"columns": columns, "rows": rows}
            else:
                return {"columns": [], "rows": [], "rowcount": result.rowcount}
        except Exception as e:
            return {"error": str(e), "columns": [], "rows": []}

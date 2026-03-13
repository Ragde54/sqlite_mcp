from mcp.server.fastmcp import FastMCP
from .database import Database
from .config import settings

server = FastMCP(settings.server_name)
db = Database(settings.database_path)


@server.tool()
async def run_query(sql: str) -> dict:
    """Execute a SQL query against the database."""
    return await db.run_query(sql)

import asyncio
from importlib.metadata import version
from typing import Any, cast

from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import ServerCapabilities, TextContent, Tool, ToolsCapability

from habit_tracker_mcp.tools import (
    add_habit,
    add_todo,
    archive_habit,
    complete_habit,
    complete_todo,
    run_query,
)

app = Server("habit-tracker")

_TOOL_MODULES = [add_habit, add_todo, archive_habit, complete_habit, complete_todo, run_query]
_TOOL_MAP = {module.tool_definition.name: module for module in _TOOL_MODULES}


@app.list_tools()  # type: ignore[no-untyped-call, untyped-decorator]
async def list_tools() -> list[Tool]:
    return [m.tool_definition for m in _TOOL_MODULES]


@app.call_tool()  # type: ignore[untyped-decorator]
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    if name not in _TOOL_MAP:
        raise ValueError(f"Tool not found: {name}")
    return cast(list[TextContent], _TOOL_MAP[name].run(arguments))


async def main() -> None:
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="habit-tracker",
                server_version=version("habit-tracker-mcp"),
                capabilities=ServerCapabilities(tools=ToolsCapability()),
            ),
        )


if __name__ == "__main__":
    asyncio.run(main())

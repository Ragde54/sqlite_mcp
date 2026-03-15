from typing import Any

from mcp.types import TextContent, Tool
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from habit_tracker_mcp.database import engine
from habit_tracker_mcp.models.inputs import AddTodoInput

tool_definition = Tool(
    name="add_todo",
    description="Add a new todo item.",
    inputSchema={
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "notes": {"type": "string"},
            "priority": {"type": "string", "enum": ["low", "medium", "high"]},
            "due_date": {"type": "string", "description": "ISO 8601 date string"},
            "category_id": {"type": "integer"},
            "habit_id": {"type": "integer"},
        },
        "required": ["title"],
    },
)


def run(arguments: dict[str, Any]) -> list[TextContent]:
    """Add a new todo to the tracker."""
    params = AddTodoInput(**arguments)

    try:
        with engine.begin() as conn:
            result = conn.execute(
                text("""
                    INSERT INTO todos (title, notes, priority, due_date, category_id, habit_id)
                    VALUES (:title, :notes, :priority, :due_date, :category_id, :habit_id)
                """),
                {
                    "title": params.title,
                    "notes": params.notes,
                    "priority": params.priority,
                    "due_date": params.due_date,
                    "category_id": params.category_id,
                    "habit_id": params.habit_id,
                },
            )
            return [
                TextContent(
                    type="text", text=f"Todo '{params.title}' added with id {result.lastrowid}"
                )
            ]

    except SQLAlchemyError as e:
        raise ValueError(f"Failed to add todo: {e}") from e

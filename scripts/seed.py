# scripts/seed.py
from habit_tracker_mcp.database import SessionLocal
from habit_tracker_mcp.models import Category, Habit, Todo


def seed() -> None:
    db = SessionLocal()
    try:
        health = Category(name="health", color="#FF5733", sort_order=0)
        learning = Category(name="learning", color="#33C1FF", sort_order=1)
        db.add_all([health, learning])
        db.flush()

        habit = Habit(
            category_id=health.id,
            name="Morning run",
            frequency_type="daily",
            frequency_target=1,
        )
        db.add(habit)
        db.flush()

        todo = Todo(
            category_id=learning.id,
            title="Read SQLAlchemy docs",
            priority="high",
        )
        db.add(todo)
        db.commit()
        print("Seeded successfully.")
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


if __name__ == "__main__":
    seed()

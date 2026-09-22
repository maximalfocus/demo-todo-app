"""An in-memory to-do list."""
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Task:
    id: int
    title: str
    done: bool = False
    due_date: str = None

    def __post_init__(self):
        if self.due_date is not None:
            try:
                date.fromisoformat(self.due_date)
            except (TypeError, ValueError):
                raise ValueError(
                    f"due_date must be a real date in YYYY-MM-DD format, got {self.due_date!r}"
                )


@dataclass
class TodoList:
    tasks: list = field(default_factory=list)

    def add(self, title, due_date=None):
        task = Task(id=len(self.tasks) + 1, title=title, due_date=due_date)
        self.tasks.append(task)
        return task

    def complete(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.done = True
                return task
        raise KeyError(task_id)

    def pending(self):
        return [t for t in self.tasks if not t.done]

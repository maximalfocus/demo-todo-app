"""An in-memory to-do list."""
from dataclasses import dataclass, field


@dataclass
class Task:
    id: int
    title: str
    done: bool = False


@dataclass
class TodoList:
    tasks: list = field(default_factory=list)

    def add(self, title):
        task = Task(id=len(self.tasks) + 1, title=title)
        self.tasks.append(task)
        return task

    def complete(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.done = True
                return task
        raise KeyError(task_id)

    def pending(self, page=1, page_size=10):
        if page < 1:
            raise ValueError("todo: page must be at least 1")
        if page_size < 1:
            raise ValueError("todo: page_size must be at least 1")
        pending_tasks = [t for t in self.tasks if not t.done]
        start = (page - 1) * page_size
        return pending_tasks[start:start + page_size]

"""An in-memory to-do list."""
import csv
import io
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

    def pending(self):
        return [t for t in self.tasks if not t.done]

    def export_csv(self):
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["id", "title", "done"])
        for task in self.tasks:
            writer.writerow([task.id, task.title, task.done])
        return output.getvalue()

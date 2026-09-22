# demo-todo-app

A tiny to-do list library used for demos.

## Usage

```python
from todo.store import TodoList

todos = TodoList()

# Add tasks
todos.add("Buy milk")
todos.add("Write report")

# Mark a task done (by its id)
todos.complete(1)

# List tasks that aren't done yet
for task in todos.pending():
    print(task.id, task.title)
```

`TodoList.add(title)` creates a `Task` with an auto-incrementing `id` and
returns it. `TodoList.complete(task_id)` marks the matching task done and
returns it, raising `KeyError` if no task has that id. `TodoList.pending()`
returns the list of tasks that aren't done yet.

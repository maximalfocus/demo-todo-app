import unittest

from todo.store import TodoList


class TodoListTest(unittest.TestCase):
    def test_add_and_complete(self):
        todos = TodoList()
        task = todos.add("Write demo")
        todos.complete(task.id)
        self.assertEqual(todos.pending(), [])

    def test_add_without_due_date_defaults_to_none(self):
        todos = TodoList()
        task = todos.add("Write demo")
        self.assertIsNone(task.due_date)

    def test_add_with_valid_due_date(self):
        todos = TodoList()
        task = todos.add("Write demo", due_date="2026-09-30")
        self.assertEqual(task.due_date, "2026-09-30")

    def test_add_with_invalid_due_date_raises(self):
        todos = TodoList()
        with self.assertRaises(ValueError) as ctx:
            todos.add("Write demo", due_date="not-a-date")
        self.assertTrue(str(ctx.exception).startswith("todo:"))

    def test_add_with_nonexistent_calendar_date_raises(self):
        todos = TodoList()
        with self.assertRaises(ValueError):
            todos.add("Write demo", due_date="2026-02-30")

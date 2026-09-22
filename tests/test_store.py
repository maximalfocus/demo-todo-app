import unittest

from todo.store import TodoList


class TodoListTest(unittest.TestCase):
    def test_add_and_complete(self):
        todos = TodoList()
        task = todos.add("Write demo")
        todos.complete(task.id)
        self.assertEqual(todos.pending(), [])

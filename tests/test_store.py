import unittest

from todo.store import TodoList


class TodoListTest(unittest.TestCase):
    def test_add_and_complete(self):
        todos = TodoList()
        task = todos.add("Write demo")
        todos.complete(task.id)
        self.assertEqual(todos.pending(), [])

    def test_remove(self):
        todos = TodoList()
        task = todos.add("Write demo")
        todos.remove(task.id)
        self.assertEqual(todos.tasks, [])

    def test_remove_unknown_id_raises_value_error(self):
        todos = TodoList()
        with self.assertRaises(ValueError) as ctx:
            todos.remove(999)
        self.assertTrue(str(ctx.exception).startswith("todo:"))

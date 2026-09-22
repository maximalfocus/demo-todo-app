import unittest

from todo.store import TodoList


class TodoListTest(unittest.TestCase):
    def test_add_and_complete(self):
        todos = TodoList()
        task = todos.add("Write demo")
        todos.complete(task.id)
        self.assertEqual(todos.pending(), [])

    def test_pending_paginates(self):
        todos = TodoList()
        for i in range(5):
            todos.add(f"Task {i}")

        page1 = todos.pending(page=1, page_size=2)
        page2 = todos.pending(page=2, page_size=2)
        page3 = todos.pending(page=3, page_size=2)

        self.assertEqual([t.title for t in page1], ["Task 0", "Task 1"])
        self.assertEqual([t.title for t in page2], ["Task 2", "Task 3"])
        self.assertEqual([t.title for t in page3], ["Task 4"])

    def test_pending_default_page_and_size(self):
        todos = TodoList()
        todos.add("Only task")
        self.assertEqual([t.title for t in todos.pending()], ["Only task"])

    def test_pending_page_past_end_is_empty(self):
        todos = TodoList()
        todos.add("Task")
        self.assertEqual(todos.pending(page=2, page_size=10), [])

    def test_pending_rejects_invalid_page(self):
        todos = TodoList()
        with self.assertRaises(ValueError) as ctx:
            todos.pending(page=0)
        self.assertTrue(str(ctx.exception).startswith("todo:"))

    def test_pending_rejects_invalid_page_size(self):
        todos = TodoList()
        with self.assertRaises(ValueError) as ctx:
            todos.pending(page_size=0)
        self.assertTrue(str(ctx.exception).startswith("todo:"))

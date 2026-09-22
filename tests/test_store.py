import unittest

from todo.store import TodoList


class TodoListTest(unittest.TestCase):
    def test_add_and_complete(self):
        todos = TodoList()
        task = todos.add("Write demo")
        todos.complete(task.id)
        self.assertEqual(todos.pending(), [])

    def test_export_csv(self):
        todos = TodoList()
        todos.add("Write demo")
        todos.add("Ship it")
        todos.complete(1)
        csv_text = todos.export_csv()
        self.assertEqual(
            csv_text.splitlines(),
            [
                "id,title,done",
                "1,Write demo,True",
                "2,Ship it,False",
            ],
        )

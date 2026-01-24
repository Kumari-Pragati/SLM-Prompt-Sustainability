import unittest
from mbpp_640_code import remove_parenthesis

class TestRemoveParenthesis(unittest.TestCase):
    def test_remove_parenthesis_single_item(self):
        items = ["Hello (world)"]
        result = remove_parenthesis(items)
        self.assertEqual(result[0], "Hello world")

    def test_remove_parenthesis_multiple_items(self):
        items = ["Hello (world)", "This is another item (with parenthesis)"]
        result = remove_parenthesis(items)
        self.assertEqual(result, ["Hello world", "This is another item with parenthesis"])

    def test_remove_parenthesis_no_parenthesis(self):
        items = ["No parenthesis here"]
        result = remove_parenthesis(items)
        self.assertEqual(result, ["No parenthesis here"])

    def test_remove_parenthesis_multiple_parenthesis(self):
        items = ["Hello (world) (again)"]
        result = remove_parenthesis(items)
        self.assertEqual(result[0], "Hello world again")

    def test_remove_parenthesis_empty_list(self):
        items = []
        result = remove_parenthesis(items)
        self.assertEqual(result, [])

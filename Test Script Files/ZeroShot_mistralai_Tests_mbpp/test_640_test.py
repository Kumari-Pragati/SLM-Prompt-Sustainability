import unittest
from mbpp_640_code import remove_parenthesis

class TestRemoveParenthesis(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_parenthesis(""), "")

    def test_single_item(self):
        self.assertEqual(remove_parenthesis("(item)"), "item")
        self.assertEqual(remove_parenthesis("(item) (other item)"), "item other item")

    def test_multiple_items(self):
        self.assertEqual(remove_parenthesis(["(item1)", "(item2)", "(item3)"]), ["item1", "item2", "item3"])
        self.assertEqual(remove_parenthesis(["(item1)", "(item2)", "(item3)", "(item4) (item5)"]), ["item1", "item2", "item3", "item4 item5"])

    def test_nested_parentheses(self):
        self.assertEqual(remove_parenthesis("((item1))"), "item1")
        self.assertEqual(remove_parenthesis("((item1) (item2))"), "item1 item2")
        self.assertEqual(remove_parenthesis("((item1) (item2) (item3))"), "item1 item2 item3")

    def test_mixed_content(self):
        self.assertEqual(remove_parenthesis("(item1, item2, item3)"), "item1, item2, item3")
        self.assertEqual(remove_parenthesis("(item1, item2, (item3))"), "item1, item2, item3")
        self.assertEqual(remove_parenthesis("(item1, (item2), item3)"), "item1, item2, item3")

import unittest
from mbpp_771_code import check_expression

class TestCheckExpression(unittest.TestCase):

    def test_valid_expression(self):
        self.assertTrue(check_expression("({[]})"))

    def test_invalid_expression(self):
        self.assertFalse(check_expression("({[)]}"))

    def test_empty_expression(self):
        self.assertTrue(check_expression(""))

    def test_single_opening_bracket(self):
        self.assertFalse(check_expression("("))

    def test_single_closing_bracket(self):
        self.assertFalse(check_expression(")"))

    def test_balanced_expression(self):
        self.assertTrue(check_expression("({[()]})"))

    def test_unbalanced_expression(self):
        self.assertFalse(check_expression("({[()]")))

    def test_nested_expression(self):
        self.assertTrue(check_expression("({([{}]))}"))

    def test_unbalanced_nested_expression(self):
        self.assertFalse(check_expression("({([{}")))

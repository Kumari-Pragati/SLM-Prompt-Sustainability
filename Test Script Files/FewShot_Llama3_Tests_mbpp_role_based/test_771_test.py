import unittest
from mbpp_771_code import check_expression

class TestCheckExpression(unittest.TestCase):
    def test_valid_expression(self):
        self.assertTrue(check_expression("((()))"))

    def test_invalid_expression(self):
        self.assertFalse(check_expression("((())"))

    def test_empty_expression(self):
        self.assertTrue(check_expression(""))

    def test_single_character_expression(self):
        self.assertTrue(check_expression("("))

    def test_nested_expression(self):
        self.assertTrue(check_expression("((()))"))

    def test_unbalanced_expression(self):
        self.assertFalse(check_expression("((())"))

    def test_expression_with_spaces(self):
        self.assertTrue(check_expression("( ( ) )"))

    def test_expression_with_newlines(self):
        self.assertTrue(check_expression("( \n )"))

    def test_expression_with_mixed_brackets(self):
        self.assertTrue(check_expression("({[()]}"))

    def test_expression_with_mixed_brackets_and_spaces(self):
        self.assertTrue(check_expression("({ [ ( ) ] })"))

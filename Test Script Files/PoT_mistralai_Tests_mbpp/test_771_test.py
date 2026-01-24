import unittest
from mbpp_771_code import check_expression

class TestCheckExpression(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(check_expression(''))

    def test_single_bracket(self):
        self.assertFalse(check_expression('('))
        self.assertFalse(check_expression(')'))
        self.assertFalse(check_expression('['))
        self.assertFalse(check_expression(']'))
        self.assertFalse(check_expression('{'))
        self.assertFalse(check_expression('}'))

    def test_single_bracket_pair(self):
        self.assertTrue(check_expression('()'))
        self.assertTrue(check_expression('[]'))
        self.assertTrue(check_expression('{}'))

    def test_multiple_bracket_pairs(self):
        self.assertTrue(check_expression('()()'))
        self.assertTrue(check_expression('[][]'))
        self.assertTrue(check_expression('{}{}'))
        self.assertTrue(check_expression('()[]{}'))

    def test_mixed_bracket_pairs(self):
        self.assertFalse(check_expression('()[]'))
        self.assertFalse(check_expression('(){}'))
        self.assertFalse(check_expression('[]{}'))
        self.assertFalse(check_expression('(){}[]'))
        self.assertFalse(check_expression('()[]{}'))
        self.assertFalse(check_expression('{}()[]'))

    def test_brackets_with_numbers(self):
        self.assertTrue(check_expression('(1)'))
        self.assertTrue(check_expression('[1, 2, 3]'))
        self.assertTrue(check_expression('{key1: value1, key2: value2}'))

    def test_brackets_with_operators(self):
        self.assertFalse(check_expression('(1 + 2)'))
        self.assertFalse(check_expression('[1, 2 + 3]'))
        self.assertFalse(check_expression('{key1: value1 + value2}'))

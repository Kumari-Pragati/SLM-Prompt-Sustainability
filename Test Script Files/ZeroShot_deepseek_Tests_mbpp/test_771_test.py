import unittest
from mbpp_771_code import deque
from mbpp_771_code import check_expression

class TestCheckExpression(unittest.TestCase):

    def test_even_length_expression(self):
        self.assertTrue(check_expression('()'))
        self.assertTrue(check_expression('{}'))
        self.assertTrue(check_expression('[]'))
        self.assertTrue(check_expression('{}[]'))
        self.assertTrue(check_expression('([{}])'))

    def test_odd_length_expression(self):
        self.assertFalse(check_expression('('))
        self.assertFalse(check_expression(')'))
        self.assertFalse(check_expression('}{'))
        self.assertFalse(check_expression('['))
        self.assertFalse(check_expression(']'))
        self.assertFalse(check_expression('([)]'))

    def test_mismatched_brackets(self):
        self.assertFalse(check_expression('({[]})'))
        self.assertFalse(check_expression('({})[]]'))
        self.assertFalse(check_expression('([)]'))
        self.assertFalse(check_expression('[(])'))

    def test_empty_expression(self):
        self.assertTrue(check_expression(''))

import unittest
from mbpp_771_code import check_expression

class TestCheckExpression(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(check_expression('()'))
        self.assertTrue(check_expression('{}'))
        self.assertTrue(check_expression('[]'))
        self.assertTrue(check_expression('([])'))
        self.assertTrue(check_expression('([{}])'))
        self.assertTrue(check_expression('((((()))))'))

    def test_edge_cases(self):
        self.assertFalse(check_expression('('))
        self.assertFalse(check_expression(')'))
        self.assertFalse(check_expression(''))
        self.assertFalse(check_expression('([]'))
        self.assertFalse(check_expression('([)]'))
        self.assertFalse(check_expression('([}{]))'))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_expression(123)
        with self.assertRaises(TypeError):
            check_expression(None)
        with self.assertRaises(TypeError):
            check_expression(['(', ')'])

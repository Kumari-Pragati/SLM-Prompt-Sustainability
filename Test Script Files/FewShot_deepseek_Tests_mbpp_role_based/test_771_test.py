import unittest
from mbpp_771_code import check_expression

class TestCheckExpression(unittest.TestCase):
    def test_typical_use_cases(self):
        self.assertTrue(check_expression("()"))
        self.assertTrue(check_expression("[]"))
        self.assertTrue(check_expression("{}"))
        self.assertTrue(check_expression("([])"))
        self.assertTrue(check_expression("{[]}"))
        self.assertTrue(check_expression("([{}])"))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(check_expression("("))
        self.assertFalse(check_expression(")"))
        self.assertFalse(check_expression("]["))
        self.assertFalse(check_expression("}{"))
        self.assertFalse(check_expression("({[]})"))
        self.assertFalse(check_expression("({[]})("))

    def test_invalid_inputs(self):
        self.assertFalse(check_expression(""))
        self.assertFalse(check_expression("("))
        self.assertFalse(check_expression(")"))
        self.assertFalse(check_expression("]["))
        self.assertFalse(check_expression("}{"))
        self.assertFalse(check_expression("({[]})"))
        self.assertFalse(check_expression("({[]})("))

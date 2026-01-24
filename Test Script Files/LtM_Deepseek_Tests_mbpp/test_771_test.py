import unittest
from mbpp_771_code import check_expression

class TestCheckExpression(unittest.TestCase):

    # Test for simple / typical inputs
    def test_simple_expressions(self):
        self.assertTrue(check_expression("()"))
        self.assertTrue(check_expression("[]"))
        self.assertTrue(check_expression("{}"))
        self.assertTrue(check_expression("()[]{}"))

    # Test for edge and boundary conditions
    def test_empty_expression(self):
        self.assertTrue(check_expression(""))

    def test_single_bracket_expression(self):
        self.assertFalse(check_expression("("))
        self.assertFalse(check_expression(")"))
        self.assertFalse(check_expression("{"))
        self.assertFalse(check_expression("}"))
        self.assertFalse(check_expression("["))
        self.assertFalse(check_expression("]"))

    # Test for more complex or corner cases
    def test_complex_expressions(self):
        self.assertFalse(check_expression("({[]})"))
        self.assertFalse(check_expression("({})[]]"))
        self.assertFalse(check_expression("({})[}]"))
        self.assertFalse(check_expression("({})[})"))

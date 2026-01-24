import unittest
from mbpp_771_code import check_expression

class TestCheckExpression(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(check_expression(""))

    def test_single_bracket(self):
        self.assertFalse(check_expression("("))
        self.assertFalse(check_expression(")"))
        self.assertFalse(check_expression("{"))
        self.assertFalse(check_expression("}"))
        self.assertFalse(check_expression("["))
        self.assertFalse(check_expression("]"))

    def test_valid_expressions(self):
        self.assertTrue(check_expression("()"))
        self.assertTrue(check_expression("{}"))
        self.assertTrue(check_expression("[]"))
        self.assertTrue(check_expression("(){}[]"))
        self.assertTrue(check_expression("((()))"))
        self.assertTrue(check_expression("{{}}"))
        self.assertTrue(check_expression("[][]"))

    def test_invalid_expressions(self):
        self.assertFalse(check_expression("())"))
        self.assertFalse(check_expression("{}}"))
        self.assertFalse(check_expression("[]]"))
        self.assertFalse(check_expression("(){}]"))
        self.assertFalse(check_expression("(())"))
        self.assertFalse(check_expression("{{}}("))
        self.assertFalse(check_expression("[][]("))

    def test_mixed_expressions(self):
        self.assertFalse(check_expression("(){}[])"))
        self.assertFalse(check_expression("{}([])"))
        self.assertFalse(check_expression("[](())"))

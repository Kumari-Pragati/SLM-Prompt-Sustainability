import unittest
from mbpp_771_code import check_expression

class TestCheckExpression(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(check_expression(""))

    def test_single_char_bracket(self):
        self.assertFalse(check_expression("("))
        self.assertFalse(check_expression(")"))
        self.assertFalse(check_expression("{"))
        self.assertFalse(check_expression("}"))
        self.assertFalse(check_expression("["))
        self.assertFalse(check_expression("]"))

    def test_single_char_parenthesis(self):
        self.assertTrue(check_expression("("))
        self.assertTrue(check_expression(")"))

    def test_single_char_curly_braces(self):
        self.assertTrue(check_expression("{"))
        self.assertTrue(check_expression("}"))

    def test_single_char_square_brackets(self):
        self.assertTrue(check_expression("["))
        self.assertTrue(check_expression("]"))

    def test_simple_expression(self):
        self.assertTrue(check_expression("()"))
        self.assertTrue(check_expression("{}"))
        self.assertTrue(check_expression("[]"))

    def test_complex_expression(self):
        self.assertTrue(check_expression("(){}[]"))
        self.assertTrue(check_expression("(())"))
        self.assertTrue(check_expression("({})"))
        self.assertTrue(check_expression("([[]])"))

    def test_mixed_expression(self):
        self.assertFalse(check_expression("(}"))
        self.assertFalse(check_expression("([)"))
        self.assertFalse(check_expression("({[]})"))
        self.assertFalse(check_expression("(){}[]("))

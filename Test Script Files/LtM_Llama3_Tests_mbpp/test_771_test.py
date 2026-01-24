import unittest
from mbpp_771_code import check_expression

class TestCheckExpression(unittest.TestCase):
    def test_simple_valid(self):
        self.assertTrue(check_expression("()"))
        self.assertTrue(check_expression("[]"))
        self.assertTrue(check_expression("{{}}"))

    def test_simple_invalid(self):
        self.assertFalse(check_expression(")"))
        self.assertFalse(check_expression("]"))
        self.assertFalse(check_expression("}"))

    def test_empty_input(self):
        self.assertFalse(check_expression(""))

    def test_single_char_input(self):
        self.assertFalse(check_expression("("))
        self.assertFalse(check_expression("["))
        self.assertFalse(check_expression("{"))

    def test_nested_valid(self):
        self.assertTrue(check_expression("()()"))
        self.assertTrue(check_expression("({}[{}])"))

    def test_nested_invalid(self):
        self.assertFalse(check_expression("(()"))
        self.assertFalse(check_expression("({[}")))

    def test_mixed_valid(self):
        self.assertTrue(check_expression("({[]})"))
        self.assertTrue(check_expression("({[()]}"))

    def test_mixed_invalid(self):
        self.assertFalse(check_expression("({[}"))
        self.assertFalse(check_expression("({[})"))

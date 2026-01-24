import unittest
from mbpp_771_code import check_expression

class TestCheckExpression(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(check_expression("()"))
        self.assertTrue(check_expression("({[]})"))
        self.assertTrue(check_expression("({[()]})"))

    def test_edge_cases(self):
        self.assertFalse(check_expression("()("))
        self.assertFalse(check_expression("({[()]})("))
        self.assertFalse(check_expression("({[()]})"))


    def test_invalid_inputs(self):
        self.assertFalse(check_expression("a"))
        self.assertFalse(check_expression("({[()]})a"))
        self.assertFalse(check_expression("({[()]})a("))

    def test_empty_input(self):
        self.assertTrue(check_expression(""))

    def test_single_character_input(self):
        self.assertTrue(check_expression("("))
        self.assertTrue(check_expression(")"))
        self.assertTrue(check_expression("("))
        self.assertTrue(check_expression("]"))
        self.assertTrue(check_expression("["))

    def test_multiple_inputs(self):
        self.assertTrue(check_expression("({[()]})"))
        self.assertTrue(check_expression("({[()]})("))
        self.assertFalse(check_expression("({[()]})("))

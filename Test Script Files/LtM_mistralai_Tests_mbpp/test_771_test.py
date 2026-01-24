import unittest
from mbpp_771_code import check_expression

class TestCheckExpression(unittest.TestCase):

    def test_simple_valid_inputs(self):
        self.assertTrue(check_expression("()"))
        self.assertTrue(check_expression("[]"))
        self.assertTrue(check_expression("{}"))
        self.assertTrue(check_expression("(())"))
        self.assertTrue(check_expression("[][]"))
        self.assertTrue(check_expression("{}{}"))

    def test_edge_and_boundary_conditions(self):
        self.assertTrue(check_expression("(())("))
        self.assertTrue(check_expression("[][][]"))
        self.assertTrue(check_expression("{}{}{}"))
        self.assertTrue(check_expression("(())[]{}"))
        self.assertTrue(check_expression("()[]{}"))
        self.assertTrue(check_expression("(){}[]"))
        self.assertTrue(check_expression("[](){}"))
        self.assertTrue(check_expression("{}()[]"))

    def test_complex_and_corner_cases(self):
        self.assertFalse(check_expression("(]"))
        self.assertFalse(check_expression("[(])"))
        self.assertFalse(check_expression("{[()]}"))
        self.assertFalse(check_expression("(())(()))"))
        self.assertFalse(check_expression("[][][][]"))
        self.assertFalse(check_expression("{}{}{}{}"))
        self.assertFalse(check_expression("(())[]{}()"))
        self.assertFalse(check_expression("()[]{}()[]"))
        self.assertFalse(check_expression("(){}[]()"))
        self.assertFalse(check_expression("[](){}()"))
        self.assertFalse(check_expression("{}()[]()"))

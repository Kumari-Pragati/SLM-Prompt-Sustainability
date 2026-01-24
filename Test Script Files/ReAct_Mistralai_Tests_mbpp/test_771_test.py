import unittest
from mbpp_771_code import check_expression

class TestCheckExpression(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(check_expression(""))

    def test_single_bracket(self):
        for bracket in "([{])":
            self.assertFalse(check_expression(bracket))
            self.assertFalse(check_expression(f"{bracket} "))
            self.assertFalse(check_expression(f" {bracket}"))
            self.assertFalse(check_expression(f" {bracket} "))

    def test_single_bracket_pair(self):
        for bracket in "((()))", "([{}])", "([[]])":
            self.assertTrue(check_expression(bracket))

    def test_mixed_brackets(self):
        for brackets in (
            "([{}])([{}])",
            "([{}])([[]])",
            "([{}])([()])",
            "([()])([{}])",
            "([()])([[]])",
            "([[]])([{}])",
            "([[]])([()])",
        ):
            self.assertFalse(check_expression(brackets))

    def test_nested_brackets(self):
        for brackets in (
            "((()))",
            "([{}])",
            "([[[]]])",
            "([()])",
            "([{}])([()])",
            "([[[]]])([()])",
            "([()])([{}])",
            "([[[]]])([{}])",
            "([()])([[[]]])",
            "([{}])([()])",
            "([{}])([[[]])",
            "([[[]]])([()])",
            "([[[]]])([{}])",
        ):
            self.assertTrue(check_expression(brackets))

    def test_empty_brackets(self):
        for brackets in (
            "()",
            "{}",
            "[]",
        ):
            self.assertTrue(check_expression(brackets))

    def test_mixed_empty_brackets(self):
        for brackets in (
            "(){}",
            "()[]",
            "{}[]",
            "()[]{}",
            "{}[]()",
        ):
            self.assertFalse(check_expression(brackets))

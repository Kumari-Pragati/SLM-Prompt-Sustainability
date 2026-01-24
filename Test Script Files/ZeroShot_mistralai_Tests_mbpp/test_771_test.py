import unittest
from mbpp_771_code import deque

def check_expression(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}') or (top == '[' and ch != ']'):
                return False
    return not stack

class TestCheckExpression(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(check_expression(""))

    def test_single_char(self):
        self.assertFalse(check_expression("("))
        self.assertFalse(check_expression(")"))
        self.assertFalse(check_expression("{"))
        self.assertFalse(check_expression("}"))
        self.assertFalse(check_expression("["))
        self.assertFalse(check_expression("]"))

    def test_simple_expressions(self):
        self.assertTrue(check_expression("()"))
        self.assertTrue(check_expression("{}"))
        self.assertTrue(check_expression("[]"))
        self.assertFalse(check_expression("(}"))
        self.assertFalse(check_expression("{)"))
        self.assertFalse(check_expression("]["))
        self.assertFalse(check_expression("()]"))
        self.assertFalse(check_expression("{[]}"))

    def test_complex_expressions(self):
        self.assertTrue(check_expression("((()))"))
        self.assertTrue(check_expression("{{}}"))
        self.assertTrue(check_expression("[[[]]]"))
        self.assertFalse(check_expression("(()"))
        self.assertFalse(check_expression("{{}})"))
        self.assertFalse(check_expression("[[[]]]}"))
        self.assertFalse(check_expression("((()))]"))
        self.assertFalse(check_expression("{{}}[]"))

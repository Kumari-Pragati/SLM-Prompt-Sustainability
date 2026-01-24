import unittest
from mbpp_864_code import palindrome_lambda

class TestPalindromeLambda(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(palindrome_lambda(["radar", "level", "python"]), ["radar", "level"])

    def test_edge_conditions(self):
        self.assertEqual(palindrome_lambda(["a"]), ["a"])
        self.assertEqual(palindrome_lambda([]), [])

    def test_complex_cases(self):
        self.assertEqual(palindrome_lambda(["racecar", "deed", "python", "deified"]), ["racecar", "deed", "deified"])
        self.assertEqual(palindrome_lambda(["12321", "123321"]), ["12321", "123321"])

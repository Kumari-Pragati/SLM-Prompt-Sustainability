import unittest
from mbpp_864_code import palindrome_lambda

class TestPalindromeLambda(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertListEqual(palindrome_lambda(["racecar", "level", "madam"]), ["racecar", "level"])
        self.assertListEqual(palindrome_lambda(["radar", "rotor", "deified"]), ["radar", "rotor"])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(palindrome_lambda([""]), [])
        self.assertListEqual(palindrome_lambda(["a"]), [])
        self.assertListEqual(palindrome_lambda(["aa"]), ["aa"])
        self.assertListEqual(palindrome_lambda(["ab"]), [])
        self.assertListEqual(palindrome_lambda(["abba"]), ["abba"])
        self.assertListEqual(palindrome_lambda(["A", "B", "C", "A"]), [])
        self.assertListEqual(palindrome_lambda(["A", "B", "C", "A", "B"]), ["A", "B", "A", "B"])

    def test_special_cases(self):
        self.assertListEqual(palindrome_lambda(["12321"]), [])
        self.assertListEqual(palindrome_lambda(["A man, a plan, a canal: Panama"]), [])
        self.assertListEqual(palindrome_lambda(["Never odd or even"]), [])

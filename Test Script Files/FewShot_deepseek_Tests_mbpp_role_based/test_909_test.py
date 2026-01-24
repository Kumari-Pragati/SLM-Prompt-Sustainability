import unittest
from mbpp_909_code import previous_palindrome

class TestPreviousPalindrome(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(previous_palindrome(12321), 12211)

    def test_edge_condition(self):
        self.assertEqual(previous_palindrome(12344321), 1233321)

    def test_boundary_condition(self):
        self.assertEqual(previous_palindrome(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000), 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            previous_palindrome('12321')

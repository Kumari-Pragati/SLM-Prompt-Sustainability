import unittest
from mbpp_909_code import previous_palindrome

class TestPreviousPalindrome(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(previous_palindrome(10), 9)

    def test_edge_case(self):
        self.assertEqual(previous_palindrome(1), None)

    def test_edge_case2(self):
        self.assertEqual(previous_palindrome(0), None)

    def test_edge_case3(self):
        self.assertEqual(previous_palindrome(-1), None)

    def test_edge_case4(self):
        self.assertEqual(previous_palindrome(-10), None)

    def test_edge_case5(self):
        self.assertEqual(previous_palindrome(11), 10)

    def test_edge_case6(self):
        self.assertEqual(previous_palindrome(12), 11)

    def test_edge_case7(self):
        self.assertEqual(previous_palindrome(13), 12)

    def test_edge_case8(self):
        self.assertEqual(previous_palindrome(14), 13)

    def test_edge_case9(self):
        self.assertEqual(previous_palindrome(15), 14)

    def test_edge_case10(self):
        self.assertEqual(previous_palindrome(16), 15)

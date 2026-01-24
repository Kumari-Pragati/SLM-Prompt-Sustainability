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
        self.assertEqual(previous_palindrome(100), 99)

    def test_edge_case7(self):
        self.assertEqual(previous_palindrome(101), 100)

    def test_edge_case8(self):
        self.assertEqual(previous_palindrome(1000), 999)

    def test_edge_case9(self):
        self.assertEqual(previous_palindrome(1001), 1000)

    def test_edge_case10(self):
        self.assertEqual(previous_palindrome(10000), 9999)

    def test_edge_case11(self):
        self.assertEqual(previous_palindrome(10001), 10000)

    def test_edge_case12(self):
        self.assertEqual(previous_palindrome(100000), 99999)

    def test_edge_case13(self):
        self.assertEqual(previous_palindrome(100001), 100000)

    def test_edge_case14(self):
        self.assertEqual(previous_palindrome(1000000), 999999)

    def test_edge_case15(self):
        self.assertEqual(previous_palindrome(1000001), 1000000)

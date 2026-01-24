import unittest
from mbpp_100_code import next_smallest_palindrome

class TestNextSmallestPalindrome(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(next_smallest_palindrome(123), 121)

    def test_edge_case(self):
        self.assertEqual(next_smallest_palindrome(12321), 12321)

    def test_edge_case2(self):
        self.assertEqual(next_smallest_palindrome(123456), 12321)

    def test_edge_case3(self):
        self.assertEqual(next_smallest_palindrome(sys.maxsize - 1), sys.maxsize)

    def test_edge_case4(self):
        self.assertEqual(next_smallest_palindrome(sys.maxsize), sys.maxsize)

    def test_edge_case5(self):
        self.assertEqual(next_smallest_palindrome(0), 0)

    def test_edge_case6(self):
        self.assertEqual(next_smallest_palindrome(1), 1)

    def test_edge_case7(self):
        self.assertEqual(next_smallest_palindrome(2), 2)

    def test_edge_case8(self):
        self.assertEqual(next_smallest_palindrome(3), 3)

    def test_edge_case9(self):
        self.assertEqual(next_smallest_palindrome(4), 4)

    def test_edge_case10(self):
        self.assertEqual(next_smallest_palindrome(5), 5)

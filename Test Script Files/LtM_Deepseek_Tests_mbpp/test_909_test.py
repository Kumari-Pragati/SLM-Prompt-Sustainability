import unittest
from mbpp_909_code import previous_palindrome

class TestPreviousPalindrome(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(previous_palindrome(12321), 1221)
        self.assertEqual(previous_palindrome(121), 111)
        self.assertEqual(previous_palindrome(12344321), 123321)

    def test_edge_conditions(self):
        self.assertEqual(previous_palindrome(100), 99)
        self.assertEqual(previous_palindrome(1000), 999)
        self.assertEqual(previous_palindrome(123456789), 1234554321)

    def test_boundary_conditions(self):
        self.assertEqual(previous_palindrome(10), 9)
        self.assertEqual(previous_palindrome(10000), 9999)
        self.assertEqual(previous_palindrome(1234567890), 1234554321)

    def test_complex_cases(self):
        self.assertEqual(previous_palindrome(1234567890987654321), 12345678908908907654321)
        self.assertEqual(previous_palindrome(12345678909876543210), 12345678909876543209)

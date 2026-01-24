import unittest
from mbpp_502_code import find

class TestFindFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find(10, 3), 1)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            find(10, 0)

    def test_negative_numbers(self):
        self.assertEqual(find(-10, 3), -1)
        self.assertEqual(find(10, -3), 1)
        self.assertEqual(find(-10, -3), -1)

    def test_large_numbers(self):
        self.assertEqual(find(10**10, 10**9), 10**10 % 10**9)

    def test_equal_numbers(self):
        self.assertEqual(find(10, 10), 0)

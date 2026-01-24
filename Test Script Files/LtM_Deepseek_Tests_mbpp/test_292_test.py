import unittest
from mbpp_292_code import find

class TestFindFunction(unittest.TestCase):

    def test_simple_division(self):
        self.assertEqual(find(10, 2), 5)
        self.assertEqual(find(15, 3), 5)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            find(10, 0)

    def test_negative_numbers(self):
        self.assertEqual(find(-10, -2), 5)
        self.assertEqual(find(-15, -3), 5)

    def test_division_with_decimal(self):
        self.assertEqual(find(10, 3), 3)

    def test_large_numbers(self):
        self.assertEqual(find(10**10, 10**9), 10)

    def test_division_with_one(self):
        self.assertEqual(find(10, 1), 10)

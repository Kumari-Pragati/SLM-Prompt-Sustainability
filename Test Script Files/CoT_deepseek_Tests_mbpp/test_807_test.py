import unittest
from mbpp_807_code import first_odd

class TestFirstOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_odd([2, 4, 6, 8, 10]), -1)
        self.assertEqual(first_odd([2, 4, 6, 8, 11]), 11)

    def test_empty_list(self):
        self.assertEqual(first_odd([]), -1)

    def test_all_even(self):
        self.assertEqual(first_odd([2, 4, 6, 8]), -1)

    def test_all_odd(self):
        self.assertEqual(first_odd([1, 3, 5, 7]), 1)

    def test_mixed_numbers(self):
        self.assertEqual(first_odd([2, 4, 6, 8, 11, 13]), 11)

    def test_negative_numbers(self):
        self.assertEqual(first_odd([-2, -4, -6, -8, -10]), -1)
        self.assertEqual(first_odd([-2, -4, -6, -8, -11]), -11)

    def test_large_numbers(self):
        self.assertEqual(first_odd([1000000000000000000, 2000000000000000000]), -1)
        self.assertEqual(first_odd([1000000000000000001, 2000000000000000000]), 1000000000000000001)

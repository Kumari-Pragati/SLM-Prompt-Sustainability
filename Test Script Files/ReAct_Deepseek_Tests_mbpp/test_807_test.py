import unittest
from mbpp_807_code import first_odd

class TestFirstOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_odd([2, 4, 6, 8, 10]), -1)
        self.assertEqual(first_odd([2, 4, 6, 9, 10]), 9)

    def test_empty_list(self):
        self.assertEqual(first_odd([]), -1)

    def test_all_even(self):
        self.assertEqual(first_odd([2, 4, 6, 8]), -1)

    def test_all_odd(self):
        self.assertEqual(first_odd([3, 5, 7, 9]), 3)

    def test_negative_numbers(self):
        self.assertEqual(first_odd([-2, -4, -6, -8, -10]), -1)
        self.assertEqual(first_odd([-2, -4, -6, -9, -10]), -9)

    def test_mixed_numbers(self):
        self.assertEqual(first_odd([2, -4, 6, -8, 10]), -1)
        self.assertEqual(first_odd([2, -4, 6, -9, 10]), -9)

import unittest
from mbpp_807_code import first_odd

class TestFirstOdd(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(first_odd([]), -1)

    def test_all_even(self):
        self.assertEqual(first_odd([2, 4, 6]), -1)

    def test_single_odd(self):
        self.assertEqual(first_odd([1, 2, 3]), 1)

    def test_single_even(self):
        self.assertEqual(first_odd([2]), -1)

    def test_mixed_odd_even(self):
        self.assertEqual(first_odd([1, 2, 3, 4, 5]), 1)

    def test_negative_numbers(self):
        self.assertEqual(first_odd([-1, -3, 5]), 5)

    def test_zero(self):
        self.assertEqual(first_odd([0]), -1)

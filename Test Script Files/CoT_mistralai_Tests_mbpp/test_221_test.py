import unittest
from mbpp_221_code import first_even

class TestFirstEven(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(first_even([]), -1)

    def test_single_odd_number(self):
        self.assertEqual(first_even([1]), -1)

    def test_single_even_number(self):
        self.assertEqual(first_even([2]), 2)

    def test_multiple_even_numbers(self):
        self.assertEqual(first_even([2, 4, 6]), 2)

    def test_multiple_odd_numbers(self):
        self.assertEqual(first_even([1, 3, 5]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(first_even([1, 2, 3, 4, 5, 6]), 2)

    def test_negative_numbers(self):
        self.assertEqual(first_even([-2, -4, -6]), -2)

    def test_zero(self):
        self.assertEqual(first_even([0]), -1)

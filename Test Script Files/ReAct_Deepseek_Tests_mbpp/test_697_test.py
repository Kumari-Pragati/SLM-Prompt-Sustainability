import unittest
from mbpp_697_code import count_even

class TestCountEven(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_even([1, 2, 3, 4, 5]), 2)

    def test_empty_list(self):
        self.assertEqual(count_even([]), 0)

    def test_all_even_numbers(self):
        self.assertEqual(count_even([2, 4, 6, 8]), 4)

    def test_all_odd_numbers(self):
        self.assertEqual(count_even([1, 3, 5, 7]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(count_even([1, 2, 3, 4]), 2)

    def test_large_numbers(self):
        self.assertEqual(count_even(list(range(1, 10001))), 5000)

    def test_negative_numbers(self):
        self.assertEqual(count_even([-1, -2, -3, -4]), 2)

    def test_negative_and_positive_numbers(self):
        self.assertEqual(count_even([-1, 2, -3, 4]), 2)

    def test_single_even_number(self):
        self.assertEqual(count_even([2]), 1)

    def test_single_odd_number(self):
        self.assertEqual(count_even([1]), 0)

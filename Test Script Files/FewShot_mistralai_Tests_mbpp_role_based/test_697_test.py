import unittest
from mbpp_697_code import count_even

class TestCountEven(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_even([]), 0)

    def test_single_even_number(self):
        self.assertEqual(count_even([2]), 1)

    def test_single_odd_number(self):
        self.assertEqual(count_even([3]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(count_even([1, 2, 3, 4, 5]), 2)

    def test_all_even_numbers(self):
        self.assertEqual(count_even([2, 4, 6]), 3)

    def test_negative_numbers(self):
        self.assertEqual(count_even([-2, -4, -6]), 3)

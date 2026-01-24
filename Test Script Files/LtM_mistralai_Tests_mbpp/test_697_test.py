import unittest
from mbpp_697_code import count_even

class TestCountEven(unittest.TestCase):

    def test_simple_even(self):
        self.assertEqual(count_even([0, 2, 4, 6]), 4)

    def test_simple_odd(self):
        self.assertEqual(count_even([1, 3, 5, 7]), 0)

    def test_empty_list(self):
        self.assertEqual(count_even([]), 0)

    def test_single_number(self):
        self.assertEqual(count_even([0]), 1)
        self.assertEqual(count_even([1]), 0)

    def test_min_max_values(self):
        self.assertEqual(count_even(range(0, 1000000, 2)), 500000)
        self.assertEqual(count_even(range(1, 1000000, 2)), 0)

    def test_negative_numbers(self):
        self.assertEqual(count_even([-2, -4, -6]), 3)

    def test_mixed_numbers(self):
        self.assertEqual(count_even([0, 1, 2, 3, 4, 5, 6]), 4)

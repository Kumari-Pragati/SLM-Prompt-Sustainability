import unittest
from mbpp_221_code import first_even

class TestFirstEven(unittest.TestCase):

    def test_simple_even(self):
        self.assertEqual(first_even([2, 4, 6, 8]), 2)

    def test_simple_odd(self):
        self.assertEqual(first_even([1, 3, 5, 7]), -1)

    def test_single_even(self):
        self.assertEqual(first_even([2]), 2)

    def test_single_odd(self):
        self.assertEqual(first_even([1]), -1)

    def test_empty_list(self):
        self.assertEqual(first_even([]), -1)

    def test_all_even(self):
        self.assertEqual(first_even([0, 2, 4, 6, 8]), 0)

    def test_all_odd(self):
        self.assertEqual(first_even([1, 3, 5, 7, 9]), -1)

    def test_min_max_values(self):
        self.assertEqual(first_even([-2147483648, -1, 0, 1, 2147483647]), -1)

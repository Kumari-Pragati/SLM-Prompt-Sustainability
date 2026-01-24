import unittest
from mbpp_697_code import count_even

class TestCountEven(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(count_even([]), 0)

    def test_all_even(self):
        self.assertEqual(count_even([2, 4, 6, 8]), 4)

    def test_all_odd(self):
        self.assertEqual(count_even([1, 3, 5, 7]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(count_even([1, 2, 3, 4, 5, 6]), 3)

    def test_single_even(self):
        self.assertEqual(count_even([1, 2, 3, 4]), 1)

    def test_single_odd(self):
        self.assertEqual(count_even([1, 3, 5, 7]), 0)

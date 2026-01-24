import unittest
from mbpp_697_code import count_even

class TestCountEven(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(count_even([]), 0)

    def test_single_even(self):
        self.assertEqual(count_even([2]), 1)

    def test_single_odd(self):
        self.assertEqual(count_even([3]), 0)

    def test_multiple_even(self):
        self.assertEqual(count_even([2, 4, 6]), 3)

    def test_multiple_odd(self):
        self.assertEqual(count_even([1, 3, 5]), 0)

    def test_mixed_even_odd(self):
        self.assertEqual(count_even([2, 3, 4, 5]), 2)

    def test_negative_numbers(self):
        self.assertEqual(count_even([-2, -4, 2, 3]), 2)

    def test_zero(self):
        self.assertEqual(count_even([0, 1, 2, 3]), 2)

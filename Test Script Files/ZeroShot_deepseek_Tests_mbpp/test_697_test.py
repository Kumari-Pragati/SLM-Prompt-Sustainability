import unittest
from mbpp_697_code import count_even

class TestCountEven(unittest.TestCase):

    def test_count_even_positive(self):
        self.assertEqual(count_even([1, 2, 3, 4, 5]), 2)

    def test_count_even_negative(self):
        self.assertEqual(count_even([1, 3, 5, 7, 9]), 0)

    def test_count_even_mixed(self):
        self.assertEqual(count_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5)

    def test_count_even_empty(self):
        self.assertEqual(count_even([]), 0)

    def test_count_even_single_even(self):
        self.assertEqual(count_even([2]), 1)

    def test_count_even_single_odd(self):
        self.assertEqual(count_even([1]), 0)

import unittest
from mbpp_807_code import first_odd

class TestFirstOdd(unittest.TestCase):

    def test_simple_odd_numbers(self):
        self.assertEqual(first_odd([1, 3, 5, 7, 9]), 1)
        self.assertEqual(first_odd([3, 5, 7]), 3)
        self.assertEqual(first_odd([1, 3]), 1)
        self.assertEqual(first_odd([3]), 3)

    def test_simple_even_numbers(self):
        self.assertEqual(first_odd([2, 4, 6]), -1)
        self.assertEqual(first_odd([2, 4]), -1)
        self.assertEqual(first_odd([2]), -1)

    def test_empty_list(self):
        self.assertEqual(first_odd([]), -1)

    def test_single_zero(self):
        self.assertEqual(first_odd([0]), -1)

    def test_negative_numbers(self):
        self.assertEqual(first_odd([-1, -3, -5]), -1)
        self.assertEqual(first_odd([-1, -3]), -1)
        self.assertEqual(first_odd([-1]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(first_odd([1, 2, 3, 4, 5, -1, -3, -5]), 1)

import unittest
from mbpp_881_code import sum_even_odd

class TestSumEvenOdd(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_even_odd([]), -1)

    def test_single_even(self):
        self.assertEqual(sum_even_odd([2]), 2)

    def test_single_odd(self):
        self.assertEqual(sum_even_odd([3]), -1)

    def test_single_even_and_odd(self):
        self.assertEqual(sum_even_odd([2, 3]), 5)

    def test_multiple_even(self):
        self.assertEqual(sum_even_odd([2, 4, 6]), 12)

    def test_multiple_odd(self):
        self.assertEqual(sum_even_odd([1, 3, 5]), -1)

    def test_multiple_even_and_odd(self):
        self.assertEqual(sum_even_odd([2, 4, 6, 1, 3, 5]), 12)

    def test_list_with_duplicates(self):
        self.assertEqual(sum_even_odd([2, 2, 4, 4, 6, 6]), 18)

    def test_list_with_negative_numbers(self):
        self.assertEqual(sum_even_odd([-2, -4, 2, 4]), 4)

    def test_list_with_zero(self):
        self.assertEqual(sum_even_odd([0, 1, 2]), 3)

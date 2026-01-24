import unittest
from mbpp_881_code import sum_even_odd

class TestSumEvenOdd(unittest.TestCase):
    def test_sum_even_odd_empty_list(self):
        self.assertEqual(sum_even_odd([]), -1)

    def test_sum_even_odd_single_even(self):
        self.assertEqual(sum_even_odd([2]), 2)

    def test_sum_even_odd_single_odd(self):
        self.assertEqual(sum_even_odd([3]), -1)

    def test_sum_even_odd_multiple_even(self):
        self.assertEqual(sum_even_odd([2, 4, 6]), 2 + 4)

    def test_sum_even_odd_multiple_odd(self):
        self.assertEqual(sum_even_odd([1, 3, 5]), -1)

    def test_sum_even_odd_mixed(self):
        self.assertEqual(sum_even_odd([2, 3, 4]), 2 + 3)

    def test_sum_even_odd_list_with_duplicates(self):
        self.assertEqual(sum_even_odd([2, 4, 2, 6]), 2 + 4)

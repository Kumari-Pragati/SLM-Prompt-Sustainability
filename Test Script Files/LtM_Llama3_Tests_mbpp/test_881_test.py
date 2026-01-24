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
        self.assertEqual(sum_even_odd([2, 3]), 2)

    def test_multiple_even(self):
        self.assertEqual(sum_even_odd([2, 4, 6]), 2)

    def test_multiple_odd(self):
        self.assertEqual(sum_even_odd([3, 5, 7]), -1)

    def test_mixed_even_and_odd(self):
        self.assertEqual(sum_even_odd([2, 3, 4, 5, 6]), 2)

    def test_list_with_duplicates(self):
        self.assertEqual(sum_even_odd([2, 2, 4, 4, 6]), 2)

    def test_list_with_duplicates_and_odd(self):
        self.assertEqual(sum_even_odd([2, 2, 3, 4, 4, 5, 6]), 2)

import unittest
from mbpp_881_code import sum_even_odd

class TestSumEvenOdd(unittest.TestCase):

    def test_empty_list(self):
        self.assertIs(sum_even_odd([]), -1)

    def test_single_even_number(self):
        self.assertEqual(sum_even_odd([2]), 2)

    def test_single_odd_number(self):
        self.assertEqual(sum_even_odd([1]), 1)

    def test_mixed_list(self):
        self.assertEqual(sum_even_odd([1, 2, 3, 4, 5]), 3)

    def test_list_with_only_even_numbers(self):
        self.assertEqual(sum_even_odd([2, 4, 6]), 12)

    def test_list_with_only_odd_numbers(self):
        self.assertEqual(sum_even_odd([1, 3, 5, 7]), 16)

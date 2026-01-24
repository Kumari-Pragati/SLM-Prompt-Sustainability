import unittest
from mbpp_881_code import sum_even_odd

class TestSumEvenOdd(unittest.TestCase):
    def test_single_even(self):
        self.assertEqual(sum_even_odd([2, 3, 4]), 6)

    def test_single_odd(self):
        self.assertEqual(sum_even_odd([1, 2, 3]), 2)

    def test_multiple_even(self):
        self.assertEqual(sum_even_odd([2, 4, 6, 8]), 20)

    def test_multiple_odd(self):
        self.assertEqual(sum_even_odd([1, 3, 5, 7]), 12)

    def test_empty_list(self):
        self.assertEqual(sum_even_odd([]), -1)

    def test_list_with_no_even(self):
        self.assertEqual(sum_even_odd([1, 3, 5, 7, 9]), -1)

    def test_list_with_no_odd(self):
        self.assertEqual(sum_even_odd([2, 4, 6, 8, 10]), -1)

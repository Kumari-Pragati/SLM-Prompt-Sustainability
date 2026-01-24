import unittest
from mbpp_594_code import diff_even_odd

class TestDiffEvenOdd(unittest.TestCase):
    def test_positive_even_odd_numbers(self):
        self.assertEqual(diff_even_odd([2, 4, 6, 8, 10, 1, 3, 5]), 1)

    def test_empty_list(self):
        self.assertIs(diff_even_odd([]), -1)

    def test_single_even_number(self):
        self.assertEqual(diff_even_odd([2]), -1)

    def test_single_odd_number(self):
        self.assertEqual(diff_even_odd([3]), -1)

    def test_all_even_numbers(self):
        self.assertEqual(diff_even_odd([2, 4, 6, 8]), -1)

    def test_all_odd_numbers(self):
        self.assertEqual(diff_even_odd([1, 3, 5, 7]), -1)

    def test_mixed_even_odd_numbers(self):
        self.assertEqual(diff_even_odd([2, 4, 6, 1, 3, 5]), 1)

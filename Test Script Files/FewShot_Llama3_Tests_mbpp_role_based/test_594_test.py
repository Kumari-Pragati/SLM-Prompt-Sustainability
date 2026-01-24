import unittest
from mbpp_594_code import diff_even_odd

class TestDiffEvenOdd(unittest.TestCase):
    def test_even_numbers(self):
        self.assertEqual(diff_even_odd([2, 4, 6, 8]), 4)

    def test_odd_numbers(self):
        self.assertEqual(diff_even_odd([1, 3, 5, 7]), -4)

    def test_mixed_numbers(self):
        self.assertEqual(diff_even_odd([2, 4, 1, 3]), 1)

    def test_empty_list(self):
        self.assertEqual(diff_even_odd([]), -1)

    def test_list_with_one_element(self):
        self.assertEqual(diff_even_odd([2]), 2)

    def test_list_with_no_even_numbers(self):
        self.assertEqual(diff_even_odd([1, 3, 5, 7]), -4)

    def test_list_with_no_odd_numbers(self):
        self.assertEqual(diff_even_odd([2, 4, 6, 8]), 4)

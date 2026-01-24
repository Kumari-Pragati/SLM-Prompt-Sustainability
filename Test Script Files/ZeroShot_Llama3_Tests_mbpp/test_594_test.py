import unittest
from mbpp_594_code import diff_even_odd

class TestDiffEvenOdd(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(diff_even_odd([]), 0)

    def test_single_element_list(self):
        self.assertEqual(diff_even_odd([5]), 0)

    def test_even_odd_list(self):
        self.assertEqual(diff_even_odd([2, 4, 6, 8, 10]), 0)

    def test_odd_even_list(self):
        self.assertEqual(diff_even_odd([1, 3, 5, 7, 9]), 0)

    def test_mixed_list(self):
        self.assertEqual(diff_even_odd([2, 4, 6, 8, 10, 1, 3, 5, 7, 9]), 0)

    def test_list_with_negative_numbers(self):
        self.assertEqual(diff_even_odd([-2, -4, -6, -8, -10, 1, 3, 5, 7, 9]), 0)

    def test_list_with_zero(self):
        self.assertEqual(diff_even_odd([0, 2, 4, 6, 8, 10, 1, 3, 5, 7, 9]), 0)

    def test_list_with_duplicates(self):
        self.assertEqual(diff_even_odd([2, 4, 4, 6, 8, 8, 10, 1, 3, 5, 7, 9]), 0)

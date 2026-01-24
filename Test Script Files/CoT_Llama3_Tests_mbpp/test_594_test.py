import unittest
from mbpp_594_code import diff_even_odd

class TestDiffEvenOdd(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(diff_even_odd([]), 0)

    def test_single_element_list(self):
        self.assertEqual(diff_even_odd([5]), 0)

    def test_even_odd_list(self):
        self.assertEqual(diff_even_odd([2, 3, 4, 5]), 2 - 3)

    def test_all_even_list(self):
        self.assertEqual(diff_even_odd([2, 4, 6, 8]), 0)

    def test_all_odd_list(self):
        self.assertEqual(diff_even_odd([1, 3, 5, 7]), 0)

    def test_mixed_list(self):
        self.assertEqual(diff_even_odd([2, 1, 4, 3, 6, 5]), 2 - 3)

    def test_list_with_negative_numbers(self):
        self.assertEqual(diff_even_odd([-2, -3, -4, -5]), -2 - (-3))

    def test_list_with_zero(self):
        self.assertEqual(diff_even_odd([0, 1, 2, 3]), 0)

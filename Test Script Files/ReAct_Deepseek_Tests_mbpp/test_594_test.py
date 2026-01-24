import unittest
from mbpp_594_code import diff_even_odd

class TestDiffEvenOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(diff_even_odd([1, 2, 3, 4]), 2)

    def test_typical_case_with_negative_numbers(self):
        self.assertEqual(diff_even_odd([-1, -2, -3, -4]), -2)

    def test_typical_case_with_mixed_numbers(self):
        self.assertEqual(diff_even_odd([1, -2, 3, -4]), 1)

    def test_typical_case_with_zero(self):
        self.assertEqual(diff_even_odd([0, 2, 4]), 0)

    def test_edge_case_with_no_even_numbers(self):
        self.assertEqual(diff_even_odd([1, 3, 5, 7]), -1)

    def test_edge_case_with_no_odd_numbers(self):
        self.assertEqual(diff_even_odd([2, 4, 6, 8]), -1)

    def test_edge_case_with_empty_list(self):
        self.assertEqual(diff_even_odd([]), -1)

    def test_edge_case_with_single_element(self):
        self.assertEqual(diff_even_odd([5]), -1)

    def test_edge_case_with_all_same_numbers(self):
        self.assertEqual(diff_even_odd([2, 2, 2, 2]), -1)

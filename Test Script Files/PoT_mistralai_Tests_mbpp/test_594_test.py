import unittest
from mbpp_594_code import diff_even_odd

class TestDiffEvenOdd(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(diff_even_odd([1, 2, 3, 4, 5]), 2)
        self.assertEqual(diff_even_odd([2, 2, 2, 3, 4]), 0)
        self.assertEqual(diff_even_odd([4, 3, 2, 1]), -3)

    def test_edge_case_empty_list(self):
        self.assertEqual(diff_even_odd([]), -1)

    def test_edge_case_single_element(self):
        self.assertEqual(diff_even_odd([1]), 0)
        self.assertEqual(diff_even_odd([2]), 0)

    def test_corner_case_all_even(self):
        self.assertEqual(diff_even_odd([2, 2, 2, 2]), 0)

    def test_corner_case_all_odd(self):
        self.assertEqual(diff_even_odd([1, 3, 5, 7]), 4)

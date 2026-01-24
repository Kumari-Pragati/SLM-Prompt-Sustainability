import unittest
from mbpp_881_code import sum_even_odd

class TestSumEvenOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_even_odd([1, 2, 3, 4]), 6)

    def test_edge_case_empty_list(self):
        self.assertEqual(sum_even_odd([]), -2)

    def test_boundary_case_single_element(self):
        self.assertEqual(sum_even_odd([1]), -1)
        self.assertEqual(sum_even_odd([2]), 2)

    def test_corner_case_all_elements_even(self):
        self.assertEqual(sum_even_odd([2, 4, 6]), 8)

    def test_corner_case_all_elements_odd(self):
        self.assertEqual(sum_even_odd([1, 3, 5]), 0)

    def test_exceptional_case_no_even_no_odd(self):
        self.assertEqual(sum_even_odd([3, 5, 7]), -1)

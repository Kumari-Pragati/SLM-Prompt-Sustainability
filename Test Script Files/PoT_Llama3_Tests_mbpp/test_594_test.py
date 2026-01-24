import unittest
from mbpp_594_code import diff_even_odd

class TestDiffEvenOdd(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(diff_even_odd([2, 4, 6, 8]), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(diff_even_odd([]), -1)

    def test_edge_case_single_element_list(self):
        self.assertEqual(diff_even_odd([2]), -1)

    def test_edge_case_single_element_odd_list(self):
        self.assertEqual(diff_even_odd([3]), -1)

    def test_edge_case_single_element_even_list(self):
        self.assertEqual(diff_even_odd([2]), 0)

    def test_edge_case_single_element_list_with_zero(self):
        self.assertEqual(diff_even_odd([0]), -1)

    def test_edge_case_single_element_list_with_negative(self):
        self.assertEqual(diff_even_odd([-2]), 0)

    def test_edge_case_multiple_elements_list(self):
        self.assertEqual(diff_even_odd([2, 4, 6, 8, 10]), 0)

    def test_edge_case_multiple_elements_list_with_odd(self):
        self.assertEqual(diff_even_odd([2, 4, 6, 8, 3]), -3)

    def test_edge_case_multiple_elements_list_with_even(self):
        self.assertEqual(diff_even_odd([2, 4, 6, 8, 10, 12]), 0)

    def test_edge_case_multiple_elements_list_with_mixed(self):
        self.assertEqual(diff_even_odd([2, 4, 6, 8, 3, 10]), -3)

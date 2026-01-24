import unittest
from mbpp_881_code import sum_even_odd

class TestSumEvenOdd(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_even_odd([2, 3, 4, 5]), 6)

    def test_edge_case_empty_list(self):
        self.assertEqual(sum_even_odd([]), -1)

    def test_edge_case_single_element_list(self):
        self.assertEqual(sum_even_odd([2]), 2)

    def test_edge_case_single_element_odd_list(self):
        self.assertEqual(sum_even_odd([3]), -1)

    def test_edge_case_single_element_even_list(self):
        self.assertEqual(sum_even_odd([2]), 2)

    def test_edge_case_multiple_even_elements_list(self):
        self.assertEqual(sum_even_odd([2, 4, 6]), 6)

    def test_edge_case_multiple_odd_elements_list(self):
        self.assertEqual(sum_even_odd([1, 3, 5]), -1)

    def test_edge_case_mixed_elements_list(self):
        self.assertEqual(sum_even_odd([2, 3, 4, 5]), 6)

    def test_edge_case_mixed_elements_list_with_duplicates(self):
        self.assertEqual(sum_even_odd([2, 2, 3, 4, 5]), 6)

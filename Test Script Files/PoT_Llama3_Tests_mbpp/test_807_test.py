import unittest
from mbpp_807_code import first_odd

class TestFirstOdd(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(first_odd([1, 2, 3, 4, 5]), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(first_odd([]), -1)

    def test_edge_case_single_element(self):
        self.assertEqual(first_odd([1]), 1)

    def test_edge_case_single_even_element(self):
        self.assertEqual(first_odd([2]), -1)

    def test_edge_case_single_odd_element(self):
        self.assertEqual(first_odd([1]), 1)

    def test_edge_case_multiple_odd_elements(self):
        self.assertEqual(first_odd([1, 3, 5]), 1)

    def test_edge_case_multiple_even_elements(self):
        self.assertEqual(first_odd([2, 4, 6]), -1)

    def test_edge_case_mixed_elements(self):
        self.assertEqual(first_odd([1, 2, 3, 4, 5, 6]), 1)

    def test_edge_case_mixed_elements_with_first_odd_at_start(self):
        self.assertEqual(first_odd([1, 2, 3, 4, 5, 6, 7]), 1)

    def test_edge_case_mixed_elements_with_first_odd_at_end(self):
        self.assertEqual(first_odd([2, 3, 4, 5, 6, 7, 1]), 1)

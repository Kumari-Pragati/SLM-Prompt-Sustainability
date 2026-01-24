import unittest
from mbpp_221_code import first_even

class TestFirstEven(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(first_even([2, 4, 6, 8]), 2)

    def test_edge_case_empty_list(self):
        self.assertEqual(first_even([]), -1)

    def test_edge_case_single_element_list(self):
        self.assertEqual(first_even([2]), 2)

    def test_edge_case_single_odd_element_list(self):
        self.assertEqual(first_even([1]), -1)

    def test_edge_case_multiple_odd_element_list(self):
        self.assertEqual(first_even([1, 3, 5]), -1)

    def test_edge_case_multiple_even_element_list(self):
        self.assertEqual(first_even([2, 4, 6]), 2)

    def test_edge_case_mixed_element_list(self):
        self.assertEqual(first_even([1, 2, 3, 4]), 2)

    def test_edge_case_mixed_element_list_with_first_even_at_end(self):
        self.assertEqual(first_even([1, 3, 5, 2]), 2)

    def test_edge_case_mixed_element_list_with_first_even_at_start(self):
        self.assertEqual(first_even([2, 1, 3, 4]), 2)

    def test_edge_case_mixed_element_list_with_first_even_in_middle(self):
        self.assertEqual(first_even([1, 3, 2, 4]), 2)

import unittest
from mbpp_221_code import first_even

class TestFirstEven(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(first_even([1, 2, 3, 4, 5]), 2)

    def test_edge_case_empty_list(self):
        self.assertEqual(first_even([]), -1)

    def test_edge_case_single_element_list(self):
        self.assertEqual(first_even([1]), -1)

    def test_edge_case_single_even_element_list(self):
        self.assertEqual(first_even([2]), 2)

    def test_edge_case_multiple_even_elements_list(self):
        self.assertEqual(first_even([2, 4, 6]), 2)

    def test_edge_case_multiple_odd_elements_list(self):
        self.assertEqual(first_even([1, 3, 5]), -1)

    def test_edge_case_mixed_elements_list(self):
        self.assertEqual(first_even([1, 2, 3, 4, 5, 6]), 2)

    def test_edge_case_negative_numbers_list(self):
        self.assertEqual(first_even([-1, -2, -3, -4, -5]), -2)

    def test_edge_case_zero_list(self):
        self.assertEqual(first_even([0]), 0)

    def test_edge_case_negative_zero_list(self):
        self.assertEqual(first_even([-1, 0]), 0)

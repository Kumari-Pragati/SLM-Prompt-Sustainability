import unittest
from mbpp_168_code import frequency

class TestFrequency(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(frequency([1, 2, 2, 3, 4, 2, 5], 2), 3)

    def test_edge_case_empty_list(self):
        self.assertEqual(frequency([], 1), 0)

    def test_edge_case_single_element_list(self):
        self.assertEqual(frequency([1], 1), 1)

    def test_edge_case_single_element_list_nonexistent(self):
        self.assertEqual(frequency([1], 2), 0)

    def test_edge_case_single_element_list_nonexistent_negative(self):
        self.assertEqual(frequency([1], -2), 0)

    def test_edge_case_single_element_list_nonexistent_zero(self):
        self.assertEqual(frequency([1], 0), 0)

    def test_edge_case_single_element_list_nonexistent_positive(self):
        self.assertEqual(frequency([1], 1), 1)

    def test_edge_case_single_element_list_nonexistent_large(self):
        self.assertEqual(frequency([1], 1000), 0)

    def test_edge_case_single_element_list_nonexistent_negative_large(self):
        self.assertEqual(frequency([1], -1000), 0)

    def test_edge_case_single_element_list_nonexistent_zero_large(self):
        self.assertEqual(frequency([1], 0), 0)

    def test_edge_case_single_element_list_nonexistent_positive_large(self):
        self.assertEqual(frequency([1], 1000), 0)

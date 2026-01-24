import unittest
from mbpp_426_code import filter_oddnumbers

class TestFilterOddnumbers(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(filter_oddnumbers([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_edge_case_empty_list(self):
        self.assertEqual(filter_oddnumbers([]), [])

    def test_edge_case_single_element(self):
        self.assertEqual(filter_oddnumbers([2]), [])

    def test_edge_case_single_odd_element(self):
        self.assertEqual(filter_oddnumbers([1]), [1])

    def test_edge_case_multiple_odd_elements(self):
        self.assertEqual(filter_oddnumbers([1, 3, 5]), [1, 3, 5])

    def test_edge_case_multiple_even_elements(self):
        self.assertEqual(filter_oddnumbers([2, 4, 6]), [])

    def test_edge_case_mixed_elements(self):
        self.assertEqual(filter_oddnumbers([1, 2, 3, 4, 5, 6]), [1, 3, 5])

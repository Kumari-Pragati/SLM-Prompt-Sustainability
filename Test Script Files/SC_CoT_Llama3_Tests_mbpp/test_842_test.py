import unittest
from mbpp_842_code import get_odd_occurence

class TestGetOddOccurrence(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(get_odd_occurrence([1, 2, 3, 4, 5], 5), 5)

    def test_edge_case_single_element(self):
        self.assertEqual(get_odd_occurrence([1], 1), 1)

    def test_edge_case_empty_array(self):
        self.assertEqual(get_odd_occurrence([], 0), -1)

    def test_edge_case_single_element_array(self):
        self.assertEqual(get_odd_occurrence([1, 1], 2), 1)

    def test_edge_case_all_duplicates(self):
        self.assertEqual(get_odd_occurrence([1, 1, 1, 1, 1], 5), 1)

    def test_edge_case_all_unique(self):
        self.assertEqual(get_odd_occurrence([1, 2, 3, 4, 5], 5), 5)

    def test_edge_case_duplicates_and_unique(self):
        self.assertEqual(get_odd_occurrence([1, 1, 2, 3, 4], 5), 1)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            get_odd_occurence(123, 5)

    def test_invalid_input_non_integer_size(self):
        with self.assertRaises(TypeError):
            get_odd_occurence([1, 2, 3, 4, 5], 'five')

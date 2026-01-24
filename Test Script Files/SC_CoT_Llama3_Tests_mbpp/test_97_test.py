import unittest
from mbpp_97_code import frequency_lists

class TestFrequencyLists(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(frequency_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5]]), {1: 1, 2: 2, 3: 3, 4: 2, 5: 1})

    def test_edge_case_empty_list(self):
        self.assertEqual(frequency_lists([]), {})

    def test_edge_case_single_element_list(self):
        self.assertEqual(frequency_lists([[1]]), {1: 1})

    def test_edge_case_single_element_list_with_duplicates(self):
        self.assertEqual(frequency_lists([[1, 1, 1]]), {1: 3})

    def test_edge_case_single_element_list_with_duplicates_and_zeros(self):
        self.assertEqual(frequency_lists([[0, 0, 0]]), {0: 3})

    def test_edge_case_single_element_list_with_duplicates_and_negative_numbers(self):
        self.assertEqual(frequency_lists([[-1, -1, -1]]), {-1: 3})

    def test_edge_case_single_element_list_with_duplicates_and_negative_numbers_and_zeros(self):
        self.assertEqual(frequency_lists([[0, -1, -1]]), {0: 1, -1: 2})

    def test_edge_case_single_element_list_with_duplicates_and_negative_numbers_and_zeros_and_duplicates(self):
        self.assertEqual(frequency_lists([[0, 0, -1, -1]]), {0: 2, -1: 2})

    def test_edge_case_single_element_list_with_duplicates_and_negative_numbers_and_zeros_and_duplicates_and_duplicates(self):
        self.assertEqual(frequency_lists([[0, 0, -1, -1, -1]]), {0: 2, -1: 3})

    def test_edge_case_single_element_list_with_duplicates_and_negative_numbers_and_zeros_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(frequency_lists([[0, 0, -1, -1, -1, -1]]), {0: 2, -1: 4})

    def test_edge_case_single_element_list_with_duplicates_and_negative_numbers_and_zeros_and_duplicates_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(frequency_lists([[0, 0, -1, -1, -1, -1, -1]]), {0: 2, -1: 5})

    def test_edge_case_single_element_list_with_duplicates_and_negative_numbers_and_zeros_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(frequency_lists([[0, 0, -1, -1, -1, -1, -1, -1]]), {0: 2, -1: 6})

    def test_edge_case_single_element_list_with_duplicates_and_negative_numbers_and_zeros_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(frequency_lists([[0, 0, -1, -1, -1, -1, -1, -1, -1]]), {0: 2, -1: 7})

    def test_edge_case_single_element_list_with_duplicates_and_negative_numbers_and_zeros_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(frequency_lists([[0, 0, -1, -1, -1, -1, -1, -1, -1, -1]]), {0: 2, -1: 8})

    def test_edge_case_single_element_list_with_duplicates_and_negative_numbers_and_zeros_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(frequency_lists([[0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1]]), {0: 2, -1: 9})

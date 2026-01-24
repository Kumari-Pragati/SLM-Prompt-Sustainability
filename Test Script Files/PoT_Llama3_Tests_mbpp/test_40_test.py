import unittest
from mbpp_40_code import freq_element

class TestFreqElement(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(freq_element([[1, 2, 3], [4, 5, 6]]), {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})

    def test_edge_case_empty_list(self):
        self.assertEqual(freq_element([]), {})

    def test_edge_case_single_list(self):
        self.assertEqual(freq_element([[1, 2, 3]]), {1: 1, 2: 1, 3: 1})

    def test_edge_case_single_element(self):
        self.assertEqual(freq_element([[1]]), {1: 1})

    def test_edge_case_single_element_list(self):
        self.assertEqual(freq_element([[1]]), {1: 1})

    def test_edge_case_empty_list_of_lists(self):
        self.assertEqual(freq_element([]), {})

    def test_edge_case_single_list_of_lists(self):
        self.assertEqual(freq_element([[]]), {})

    def test_edge_case_single_element_list_of_lists(self):
        self.assertEqual(freq_element([[]]), {})

    def test_edge_case_multiple_lists(self):
        self.assertEqual(freq_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1})

    def test_edge_case_multiple_lists_with_duplicates(self):
        self.assertEqual(freq_element([[1, 2, 2, 3], [4, 5, 5, 6], [7, 8, 8, 9]]), {1: 1, 2: 2, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 2, 9: 1})

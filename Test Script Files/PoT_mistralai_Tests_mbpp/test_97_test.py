import unittest
from mbpp_97_code import frequency_lists

class TestFrequencyLists(unittest.TestCase):

    def test_typical_case(self):
        self.assertDictEqual(frequency_lists([[1, 2, 3], [4, 5, 6], [1, 2, 3]]), {'1': 3, '2': 3, '3': 3, '4': 1, '5': 1, '6': 1})

    def test_edge_case_empty_list(self):
        self.assertDictEqual(frequency_lists([]), {})

    def test_edge_case_single_element(self):
        self.assertDictEqual(frequency_lists([[1]]), {'1': 1})

    def test_edge_case_single_element_list(self):
        self.assertDictEqual(frequency_lists([[1]]), {'1': 1})

    def test_edge_case_single_element_list_duplicate(self):
        self.assertDictEqual(frequency_lists([[1, 1]]), {'1': 2})

    def test_corner_case_negative_numbers(self):
        self.assertDictEqual(frequency_lists([[-1, 2, -3], [4, 5, 6], [-1, 2, -3]]), {'-1': 3, '2': 3, '3': 1, '4': 1, '5': 1, '6': 1})

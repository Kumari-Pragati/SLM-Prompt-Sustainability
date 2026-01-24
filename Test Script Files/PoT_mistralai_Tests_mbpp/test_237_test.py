import unittest
from mbpp_237_code import check_occurences

class TestCheckOccurences(unittest.TestCase):
    def test_typical_case(self):
        self.assertDictEqual(check_occurences([[1, 2], [2, 1], [1, 3], [3, 1]]), {'(1, 2)': 2, '(1, 3)': 1, '(3, 1)': 1})

    def test_edge_case_empty_list(self):
        self.assertDictEqual(check_occurences([]), {})

    def test_edge_case_single_element(self):
        self.assertDictEqual(check_occurences([[1, 1]]), {'(1, 1)': 1})

    def test_edge_case_duplicate_elements(self):
        self.assertDictEqual(check_occurences([[1, 2], [1, 2], [1, 2]]), {'(1, 2)': 3})

    def test_corner_case_unsorted_list(self):
        self.assertDictEqual(check_occurences([[2, 1], [1, 2]]), {'(1, 2)': 1, '(2, 1)': 1})

import unittest
from mbpp_237_code import check_occurences

class TestCheckOccurences(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(check_occurences([[1, 2, 3], [3, 2, 1], [1, 2, 3]]), {(1, 2, 3): 2})

    def test_edge_case_empty_list(self):
        self.assertEqual(check_occurences([]), {})

    def test_edge_case_single_element_list(self):
        self.assertEqual(check_occurences([[1, 2, 3]]), {(1, 2, 3): 1})

    def test_edge_case_duplicates(self):
        self.assertEqual(check_occurences([[1, 2, 3], [1, 2, 3], [1, 2, 3]]), {(1, 2, 3): 3})

    def test_edge_case_sorted_duplicates(self):
        self.assertEqual(check_occurences([[1, 2, 3], [1, 2, 3], [3, 2, 1]]), {(1, 2, 3): 2})

    def test_edge_case_empty_list_duplicates(self):
        self.assertEqual(check_occurences([[], [], []]), {})

    def test_edge_case_single_element_list_duplicates(self):
        self.assertEqual(check_occurences([[1, 2, 3], [1, 2, 3]]), {(1, 2, 3): 2})

    def test_edge_case_duplicates_sorted(self):
        self.assertEqual(check_occurences([[1, 2, 3], [1, 2, 3], [1, 2, 3]]), {(1, 2, 3): 3})

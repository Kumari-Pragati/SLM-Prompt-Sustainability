import unittest
from mbpp_612_code import merge

class TestMerge(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(merge([[1, 2], [3, 4], [5, 6]]), [[1, 3, 5], [2, 4, 6]])

    def test_edge_case_empty_list(self):
        self.assertEqual(merge([]), [])

    def test_edge_case_single_list(self):
        self.assertEqual(merge([[1, 2, 3]]), [[1], [2], [3]])

    def test_edge_case_single_element_list(self):
        self.assertEqual(merge([[1]]), [[1]])

    def test_edge_case_single_element_list_with_duplicates(self):
        self.assertEqual(merge([[1, 1]]), [[1], [1]])

    def test_edge_case_multiple_lists_with_duplicates(self):
        self.assertEqual(merge([[1, 1], [2, 2], [3, 3]]), [[1, 2, 3], [1, 2, 3]])

    def test_edge_case_multiple_lists_with_duplicates_and_empty(self):
        self.assertEqual(merge([[1, 1], [2, 2], [], [3, 3]]), [[1, 2], [1, 2], [], [3, 3]])

    def test_edge_case_multiple_lists_with_duplicates_and_empty_and_single(self):
        self.assertEqual(merge([[1, 1], [2, 2], [], [3, 3], [4]]), [[1, 2], [1, 2], [], [3, 3], [4]])

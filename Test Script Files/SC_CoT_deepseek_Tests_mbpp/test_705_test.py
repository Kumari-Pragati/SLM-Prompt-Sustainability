import unittest
from mbpp_705_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_sublists([[1, 2, 3], [4, 5], [6], [7, 8, 9, 10]]),
                         [[1, 2, 3], [4, 5], [6], [7, 8, 9, 10]])

    def test_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_single_element_list(self):
        self.assertEqual(sort_sublists([[1]]), [[1]])

    def test_same_length_sublists(self):
        self.assertEqual(sort_sublists([[1, 2], [3, 4], [5, 6]]),
                         [[1, 2], [3, 4], [5, 6]])

    def test_mixed_length_sublists(self):
        self.assertEqual(sort_sublists([[1, 2, 3], [4], [5, 6]]),
                         [[4], [1, 2, 3], [5, 6]])

    def test_sorting_by_length(self):
        self.assertEqual(sort_sublists([[1, 2, 3], [4, 5, 6, 7], [8]]),
                         [[8], [1, 2, 3], [4, 5, 6, 7]])

    def test_empty_sublists(self):
        self.assertEqual(sort_sublists([[], [], []]), [])

    def test_single_element_sublists(self):
        self.assertEqual(sort_sublists([[1], [2], [3]]), [[1], [2], [3]])

    def test_sorting_with_same_elements(self):
        self.assertEqual(sort_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3]]),
                         [[1, 2, 3], [1, 2, 3], [1, 2, 3]])

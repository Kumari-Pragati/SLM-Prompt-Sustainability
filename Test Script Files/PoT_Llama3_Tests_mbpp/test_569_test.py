import unittest
from mbpp_569_code import sort_sublists

class TestSortSublists(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sort_sublists([[1, 2, 3], [4, 5, 6]]), [[1, 2, 3], [4, 5, 6]])

    def test_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_single_element_list(self):
        self.assertEqual(sort_sublists([[1]]), [[1]])

    def test_single_element_sublist(self):
        self.assertEqual(sort_sublists([[1, 2, 3], [1]]), [[1, 2, 3], [1]])

    def test_sublist_with_duplicates(self):
        self.assertEqual(sort_sublists([[1, 2, 2, 3], [4, 5, 5, 6]]), [[1, 2, 2, 3], [4, 5, 5, 6]])

    def test_sublist_with_duplicates_and_empty(self):
        self.assertEqual(sort_sublists([[1, 2, 2, 3], [4, 5, 5, 6, []]]), [[1, 2, 2, 3], [4, 5, 5, 6, []]])

    def test_sublist_with_empty(self):
        self.assertEqual(sort_sublists([[1, 2, 3], [], [4, 5, 6]]), [[1, 2, 3], [], [4, 5, 6]])

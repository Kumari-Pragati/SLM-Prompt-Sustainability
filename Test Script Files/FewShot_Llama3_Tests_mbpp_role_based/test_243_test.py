import unittest
from mbpp_243_code import sort_on_occurence

class TestSortOnOccurence(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sort_on_occurence([]), [])

    def test_single_element_list(self):
        self.assertEqual(sort_on_occurence([(1, [1, 2, 3])]), [(1, 1, 1, 3)])

    def test_multiple_elements_list(self):
        self.assertEqual(sort_on_occurence([(1, [1, 2, 3]), (2, [4, 5, 6]), (1, [7, 8, 9])]),
                        [(1, 1, 1, 3), (1, 1, 2, 9), (2, 1, 1, 6)])

    def test_duplicates(self):
        self.assertEqual(sort_on_occurence([(1, [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]))],
                        [(1, 1, 1, 3), (1, 1, 2, 9), (2, 1, 1, 6), (3, 1, 1, 9), (4, 1, 1, 9), (5, 1, 1, 9), (6, 1, 1, 9), (7, 1, 1, 9), (8, 1, 1, 9), (9, 1, 1, 9)])

import unittest
from mbpp_243_code import sort_on_occurence

class TestSortOnOccurence(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sort_on_occurence([]), [])

    def test_single_element_list(self):
        self.assertEqual(sort_on_occurence([(1, [1, 2, 3])]), [(1, 1, 1, 3)])

    def test_multiple_elements_list(self):
        self.assertEqual(sort_on_occurence([(1, [1, 2, 3]), (2, [4, 5, 6]), (3, [7, 8, 9])]),
                         [(1, 1, 1, 3), (2, 4, 1, 3), (3, 7, 1, 3)])

    def test_duplicates(self):
        self.assertEqual(sort_on_occurence([(1, [1, 1, 1]), (2, [2, 2, 2])]),
                         [(1, 1, 1, 3), (2, 2, 1, 3)])

    def test_empty_sublist(self):
        self.assertEqual(sort_on_occurence([(1, [1, 2, 3]), (2, [])]), [(1, 1, 1, 3), (2, None, 0, 0)])

    def test_sublist_with_duplicates(self):
        self.assertEqual(sort_on_occurence([(1, [1, 1, 1]), (2, [2, 2, 2])]),
                         [(1, 1, 1, 3), (2, 2, 1, 3)])

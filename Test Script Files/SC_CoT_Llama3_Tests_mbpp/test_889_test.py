import unittest
from mbpp_889_code import reverse_list_lists

class TestReverseListLists(unittest.TestCase):

    def test_typical_input(self):
        lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = reverse_list_lists(lists)
        self.assertEqual(result, [[9, 8, 7], [6, 5, 4], [3, 2, 1]])

    def test_empty_list(self):
        lists = []
        result = reverse_list_lists(lists)
        self.assertEqual(result, [])

    def test_single_list(self):
        lists = [[1, 2, 3]]
        result = reverse_list_lists(lists)
        self.assertEqual(result, [[3, 2, 1]])

    def test_list_of_single_elements(self):
        lists = [[1], [2], [3]]
        result = reverse_list_lists(lists)
        self.assertEqual(result, [[3], [2], [1]])

    def test_list_of_lists_with_duplicates(self):
        lists = [[1, 2, 2], [3, 4, 4], [5, 6, 6]]
        result = reverse_list_lists(lists)
        self.assertEqual(result, [[6, 6, 2], [4, 4, 3], [2, 2, 1]])

    def test_list_of_lists_with_empty_sublist(self):
        lists = [[1, 2, 3], [4, 5, 6], [], [7, 8, 9]]
        result = reverse_list_lists(lists)
        self.assertEqual(result, [[9, 8, 7], [6, 5, 4], [], [3, 2, 1]])

    def test_list_of_lists_with_sublist_of_duplicates(self):
        lists = [[1, 2, 2], [3, 4, 4, 4], [5, 6, 6, 6]]
        result = reverse_list_lists(lists)
        self.assertEqual(result, [[6, 6, 6], [4, 4, 4, 3], [2, 2, 1]])

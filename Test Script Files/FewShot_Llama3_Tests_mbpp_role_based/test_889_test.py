import unittest
from mbpp_889_code import reverse_list_lists

class TestReverseListLists(unittest.TestCase):
    def test_single_list(self):
        lists = [[1, 2, 3]]
        result = reverse_list_lists(lists)
        self.assertEqual(result, [[3, 2, 1]])

    def test_multiple_lists(self):
        lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = reverse_list_lists(lists)
        self.assertEqual(result, [[9, 8, 7], [6, 5, 4], [3, 2, 1]])

    def test_empty_list(self):
        lists = []
        result = reverse_list_lists(lists)
        self.assertEqual(result, [])

    def test_list_with_single_element(self):
        lists = [[1]]
        result = reverse_list_lists(lists)
        self.assertEqual(result, [[1]])

    def test_list_with_empty_sublist(self):
        lists = [[1, 2, []], [3, 4, 5]]
        result = reverse_list_lists(lists)
        self.assertEqual(result, [[[], 2, 1], [5, 4, 3]])

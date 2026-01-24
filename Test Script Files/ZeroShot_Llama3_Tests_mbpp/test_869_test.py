import unittest
from mbpp_869_code import remove_list_range

class TestRemoveListRange(unittest.TestCase):

    def test_remove_list_range(self):
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 7), [3, 4, 5, 6, 7])
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 9), [5, 6, 7, 8, 9])
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 1), [])
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 11), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11, 0), [])

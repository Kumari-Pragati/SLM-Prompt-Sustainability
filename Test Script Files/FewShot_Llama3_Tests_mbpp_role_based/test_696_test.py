import unittest
from mbpp_696_code import zip_list

class TestZipList(unittest.TestCase):
    def test_typical_use_case(self):
        list1 = [[1, 2], [3, 4]]
        list2 = [[5, 6], [7, 8]]
        self.assertEqual(zip_list(list1, list2), [[1, 2, 5, 6], [3, 4, 7, 8]])

    def test_empty_list(self):
        list1 = []
        list2 = [[1, 2], [3, 4]]
        self.assertEqual(zip_list(list1, list2), [])

    def test_single_element_list(self):
        list1 = [[1, 2]]
        list2 = [[3, 4], [5, 6]]
        self.assertEqual(zip_list(list1, list2), [[1, 2, 3, 4], [1, 2, 5, 6]])

    def test_lists_of_different_lengths(self):
        list1 = [[1, 2], [3, 4]]
        list2 = [[5, 6]]
        self.assertEqual(zip_list(list1, list2), [[1, 2, 5, 6], [3, 4]])

    def test_lists_of_zero_length(self):
        list1 = []
        list2 = []
        self.assertEqual(zip_list(list1, list2), [])

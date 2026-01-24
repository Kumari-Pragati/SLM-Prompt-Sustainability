import unittest
from mbpp_550_code import find_Max

class TestFindMax(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(find_Max([], 0, 0))

    def test_single_element_list(self):
        for num in range(10):
            self.assertEqual(find_Max([num], 0, 0), num)

    def test_multiple_elements_list(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(find_Max(test_list, 0, len(test_list) - 1), max(test_list))

    def test_list_with_duplicates(self):
        test_list = [1, 1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 8, 9]
        self.assertEqual(find_Max(test_list, 0, len(test_list) - 1), max(test_list))

    def test_list_with_negative_numbers(self):
        test_list = [-1, -2, -3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(find_Max(test_list, 0, len(test_list) - 1), max(test_list))

    def test_list_with_zero(self):
        test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(find_Max(test_list, 0, len(test_list) - 1), max(test_list))

    def test_list_with_out_of_bounds_index(self):
        test_list = [1, 2, 3, 4, 5]
        with self.assertRaises(IndexError):
            find_Max(test_list, -1, len(test_list))

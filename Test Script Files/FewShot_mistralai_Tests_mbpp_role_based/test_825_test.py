import unittest
from mbpp_825_code import access_elements

class TestAccessElements(unittest.TestCase):
    def test_valid_list_and_index(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [1, 3]
        result = [2, 4]
        self.assertEqual(access_elements(nums, list_index), result)

    def test_empty_list(self):
        nums = []
        list_index = [0, 1]
        self.assertListEqual(access_elements(nums, list_index), [])

    def test_negative_index(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [-1, -2]
        self.assertListEqual(access_elements(nums, list_index), [])

    def test_index_out_of_range(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [6, 7]
        self.assertRaises(IndexError, access_elements, nums, list_index)

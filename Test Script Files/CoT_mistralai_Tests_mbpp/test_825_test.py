import unittest
from mbpp_825_code import access_elements

class TestAccessElements(unittest.TestCase):

    def test_typical_input(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [1, 3]
        expected_output = [2, 4]
        self.assertListEqual(access_elements(nums, list_index), expected_output)

    def test_empty_list(self):
        nums = []
        list_index = [0]
        self.assertRaises(IndexError, access_elements, nums, list_index)

    def test_negative_index(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [-1, 0]
        self.assertRaises(IndexError, access_elements, nums, list_index)

    def test_out_of_range_index(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [5, 6]
        self.assertRaises(IndexError, access_elements, nums, list_index)

    def test_invalid_input(self):
        self.assertRaises(TypeError, access_elements, 'string', [0])
        self.assertRaises(TypeError, access_elements, [1, 2, 3], 3.14)

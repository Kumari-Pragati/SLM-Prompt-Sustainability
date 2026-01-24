import unittest
from mbpp_825_code import access_elements

class TestAccessElements(unittest.TestCase):

    def test_typical_case(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [0, 2, 4]
        result = access_elements(nums, list_index)
        self.assertEqual(result, [1, 3, 5])

    def test_empty_list(self):
        nums = []
        list_index = [0]
        result = access_elements(nums, list_index)
        self.assertEqual(result, [])

    def test_out_of_range_index(self):
        nums = [1, 2, 3]
        list_index = [0, 2, 3]
        with self.assertRaises(IndexError):
            access_elements(nums, list_index)

    def test_negative_index(self):
        nums = [1, 2, 3]
        list_index = [-1]
        result = access_elements(nums, list_index)
        self.assertEqual(result, [3])

    def test_duplicate_index(self):
        nums = [1, 2, 3]
        list_index = [0, 0]
        result = access_elements(nums, list_index)
        self.assertEqual(result, [1, 1])

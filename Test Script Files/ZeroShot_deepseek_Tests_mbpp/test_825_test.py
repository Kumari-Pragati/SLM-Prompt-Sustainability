import unittest
from mbpp_825_code import access_elements

class TestAccessElements(unittest.TestCase):

    def test_access_elements(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [0, 2, 4]
        result = access_elements(nums, list_index)
        self.assertEqual(result, [1, 3, 5])

    def test_access_elements_empty_list(self):
        nums = []
        list_index = [0, 1, 2]
        result = access_elements(nums, list_index)
        self.assertEqual(result, [])

    def test_access_elements_out_of_range(self):
        nums = [1, 2, 3]
        list_index = [0, 1, 2, 3]
        result = access_elements(nums, list_index)
        self.assertEqual(result, [1, 2, 3, None])

    def test_access_elements_negative_index(self):
        nums = [1, 2, 3]
        list_index = [-1, -2]
        result = access_elements(nums, list_index)
        self.assertEqual(result, [3, 2])

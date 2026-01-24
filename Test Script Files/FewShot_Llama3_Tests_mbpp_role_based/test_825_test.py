import unittest
from mbpp_825_code import access_elements

class TestAccessElements(unittest.TestCase):
    def test_access_elements_positive_index(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [0, 1, 2]
        result = access_elements(nums, list_index)
        self.assertEqual(result, [1, 2, 3])

    def test_access_elements_negative_index(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [-1, 0, 1]
        result = access_elements(nums, list_index)
        self.assertEqual(result, [5, 1, 2])

    def test_access_elements_out_of_range_index(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [5, 6, 7]
        result = access_elements(nums, list_index)
        self.assertEqual(result, [])

    def test_access_elements_empty_list_index(self):
        nums = [1, 2, 3, 4, 5]
        list_index = []
        result = access_elements(nums, list_index)
        self.assertEqual(result, [])

    def test_access_elements_single_element_index(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [0]
        result = access_elements(nums, list_index)
        self.assertEqual(result, [1])

    def test_access_elements_multiple_elements_index(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [0, 2, 4]
        result = access_elements(nums, list_index)
        self.assertEqual(result, [1, 3, 5])

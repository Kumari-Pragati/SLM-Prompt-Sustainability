import unittest
from mbpp_825_code import access_elements

class TestAccessElements(unittest.TestCase):

    def test_access_elements_typical(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [0, 1, 3]
        self.assertEqual(access_elements(nums, list_index), [1, 2, 4])

    def test_access_elements_empty_list(self):
        nums = [1, 2, 3, 4, 5]
        list_index = []
        self.assertEqual(access_elements(nums, list_index), [])

    def test_access_elements_single_element(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [4]
        self.assertEqual(access_elements(nums, list_index), [5])

    def test_access_elements_out_of_range(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [5]
        with self.assertRaises(IndexError):
            access_elements(nums, list_index)

    def test_access_elements_negative_index(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [-1]
        with self.assertRaises(IndexError):
            access_elements(nums, list_index)

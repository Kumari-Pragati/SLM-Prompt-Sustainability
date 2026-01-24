import unittest
from mbpp_825_code import access_elements

class TestAccessElements(unittest.TestCase):

    def test_typical_input(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [0, 1, 2]
        result = access_elements(nums, list_index)
        self.assertEqual(result, [1, 2, 3])

    def test_edge_case_empty_list_index(self):
        nums = [1, 2, 3, 4, 5]
        list_index = []
        result = access_elements(nums, list_index)
        self.assertEqual(result, [])

    def test_edge_case_single_element_list_index(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [0]
        result = access_elements(nums, list_index)
        self.assertEqual(result, [1])

    def test_edge_case_list_index_out_of_bounds(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [5, 6, 7]
        with self.assertRaises(IndexError):
            access_elements(nums, list_index)

    def test_edge_case_negative_list_index(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [-1, 0, 1]
        result = access_elements(nums, list_index)
        self.assertEqual(result, [2, 1, 3])

    def test_edge_case_list_index_with_duplicates(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [0, 1, 1, 2, 2]
        result = access_elements(nums, list_index)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_edge_case_list_index_with_duplicates_and_out_of_bounds(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [0, 1, 1, 2, 5]
        with self.assertRaises(IndexError):
            access_elements(nums, list_index)

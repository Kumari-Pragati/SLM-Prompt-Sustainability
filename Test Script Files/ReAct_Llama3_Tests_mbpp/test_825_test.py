import unittest
from mbpp_825_code import access_elements

class TestAccessElements(unittest.TestCase):

    def test_access_elements_typical_case(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [0, 1, 3]
        result = access_elements(nums, list_index)
        self.assertEqual(result, [1, 2, 4])

    def test_access_elements_edge_case(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [0, 4]
        result = access_elements(nums, list_index)
        self.assertEqual(result, [1, 5])

    def test_access_elements_empty_list(self):
        nums = [1, 2, 3, 4, 5]
        list_index = []
        result = access_elements(nums, list_index)
        self.assertEqual(result, [])

    def test_access_elements_single_element(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [0]
        result = access_elements(nums, list_index)
        self.assertEqual(result, [1])

    def test_access_elements_out_of_range(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [5]
        with self.assertRaises(IndexError):
            access_elements(nums, list_index)

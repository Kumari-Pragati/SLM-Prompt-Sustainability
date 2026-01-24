import unittest
from mbpp_825_code import access_elements

class TestAccessElements(unittest.TestCase):
    
    def test_typical_case(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [0, 2, 4]
        self.assertEqual(access_elements(nums, list_index), [1, 3, 5])

    def test_empty_list(self):
        nums = []
        list_index = [0]
        self.assertEqual(access_elements(nums, list_index), [])

    def test_out_of_range_index(self):
        nums = [1, 2, 3]
        list_index = [0, 2, 3]
        self.assertEqual(access_elements(nums, list_index), [1, 3])

    def test_negative_index(self):
        nums = [1, 2, 3]
        list_index = [-1, -2]
        self.assertEqual(access_elements(nums, list_index), [3, 2])

    def test_duplicate_index(self):
        nums = [1, 2, 3]
        list_index = [0, 0]
        self.assertEqual(access_elements(nums, list_index), [1, 1])

    def test_invalid_input(self):
        nums = [1, 2, 3]
        list_index = ['a', 'b']
        with self.assertRaises(TypeError):
            access_elements(nums, list_index)

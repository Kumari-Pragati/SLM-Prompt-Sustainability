import unittest
from mbpp_825_code import access_elements

class TestAccessElements(unittest.TestCase):

    def test_normal_input(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [0, 2, 4]
        expected_output = [1, 3, 5]
        self.assertEqual(access_elements(nums, list_index), expected_output)

    def test_edge_cases(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [0, len(nums) - 1]
        expected_output = [1, 5]
        self.assertEqual(access_elements(nums, list_index), expected_output)

        nums = [1, 2, 3, 4, 5]
        list_index = [-1, 0, len(nums)]
        expected_output = []
        self.assertEqual(access_elements(nums, list_index), expected_output)

    def test_boundary_cases(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [0, len(nums)]
        expected_output = [1]
        self.assertEqual(access_elements(nums, list_index), expected_output)

        nums = [1, 2, 3, 4, 5]
        list_index = [len(nums), 0]
        expected_output = []
        self.assertEqual(access_elements(nums, list_index), expected_output)

    def test_invalid_input(self):
        nums = [1, 2, 3, 4, 5]
        list_index = [-1, -2]
        with self.assertRaises(IndexError):
            access_elements(nums, list_index)

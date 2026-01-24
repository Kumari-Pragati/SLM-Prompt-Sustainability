import unittest
from mbpp_154_code import specified_element

class TestSpecifiedElement(unittest.TestCase):

    def test_typical_case(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 1
        self.assertEqual(specified_element(nums, N), [2, 5, 8])

    def test_single_element_list(self):
        nums = [[1]]
        N = 0
        self.assertEqual(specified_element(nums, N), [1])

    def test_empty_list(self):
        nums = []
        N = 0
        self.assertEqual(specified_element(nums, N), [])

    def test_negative_index(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = -1
        self.assertEqual(specified_element(nums, N), [3, 6, 9])

    def test_out_of_range_index(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 3
        self.assertEqual(specified_element(nums, N), [])

    def test_invalid_input_type(self):
        nums = "not a list"
        N = 0
        with self.assertRaises(TypeError):
            specified_element(nums, N)

    def test_invalid_index_type(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = "not an integer"
        with self.assertRaises(TypeError):
            specified_element(nums, N)

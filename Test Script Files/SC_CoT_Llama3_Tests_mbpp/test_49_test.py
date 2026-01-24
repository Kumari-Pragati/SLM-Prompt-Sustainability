import unittest
from mbpp_49_code import specified_element

class TestSpecifiedElement(unittest.TestCase):

    def test_typical_inputs(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 1
        result = specified_element(nums, N)
        self.assertEqual(result, [1, 4, 7])

    def test_edge_cases(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 0
        result = specified_element(nums, N)
        self.assertEqual(result, [])

    def test_edge_case_zero_length_list(self):
        nums = []
        N = 1
        result = specified_element(nums, N)
        self.assertEqual(result, [])

    def test_edge_case_zero_length_sublist(self):
        nums = [[], [1, 2, 3], [4, 5, 6]]
        N = 1
        result = specified_element(nums, N)
        self.assertEqual(result, [])

    def test_invalid_input_type(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 'a'
        with self.assertRaises(TypeError):
            specified_element(nums, N)

    def test_invalid_input_value(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = -1
        with self.assertRaises(IndexError):
            specified_element(nums, N)

import unittest
from mbpp_154_code import specified_element

class TestSpecifiedElement(unittest.TestCase):

    def test_specified_element(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 1
        expected_result = [2, 5, 8]
        self.assertEqual(specified_element(nums, N), expected_result)

    def test_specified_element_empty_list(self):
        nums = []
        N = 1
        expected_result = []
        self.assertEqual(specified_element(nums, N), expected_result)

    def test_specified_element_invalid_N(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 4
        with self.assertRaises(IndexError):
            specified_element(nums, N)

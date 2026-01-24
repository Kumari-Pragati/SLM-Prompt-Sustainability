import unittest
from mbpp_49_code import specified_element

class TestSpecifiedElement(unittest.TestCase):

    def test_specified_element(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 1
        self.assertEqual(specified_element(nums, N), [1, 5, 9])

    def test_specified_element_empty_list(self):
        nums = []
        N = 1
        self.assertEqual(specified_element(nums, N), [])

    def test_specified_element_single_element_list(self):
        nums = [[1, 2, 3]]
        N = 1
        self.assertEqual(specified_element(nums, N), [1])

    def test_specified_element_invalid_input(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 'a'
        with self.assertRaises(TypeError):
            specified_element(nums, N)

    def test_specified_element_negative_index(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = -1
        with self.assertRaises(IndexError):
            specified_element(nums, N)

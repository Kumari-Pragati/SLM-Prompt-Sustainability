import unittest
from mbpp_49_code import specified_element

class TestSpecifiedElement(unittest.TestCase):
    def test_typical_case(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 1
        expected = [1, 4, 7]
        self.assertEqual(specified_element(nums, N), expected)

    def test_edge_case(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 0
        expected = [1, 5, 9]
        self.assertEqual(specified_element(nums, N), expected)

    def test_edge_case2(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 2
        expected = [3, 6, 9]
        self.assertEqual(specified_element(nums, N), expected)

    def test_invalid_input(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 'a'
        with self.assertRaises(TypeError):
            specified_element(nums, N)

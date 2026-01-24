import unittest
from mbpp_49_code import specified_element

class TestSpecifiedElement(unittest.TestCase):
    def test_typical_use_case(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 1
        self.assertEqual(specified_element(nums, N), [2, 5, 8])

    def test_edge_condition(self):
        nums = [[1], [2], [3]]
        N = 0
        self.assertEqual(specified_element(nums, N), [1, 2, 3])

    def test_boundary_condition(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 3
        self.assertEqual(specified_element(nums, N), [3, 6, 9])

    def test_invalid_input(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 'a'
        with self.assertRaises(TypeError):
            specified_element(nums, N)

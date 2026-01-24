import unittest
from mbpp_31_code import func

class TestFunc(unittest.TestCase):
    def test_typical_use_case(self):
        nums = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        k = 2
        self.assertEqual(func(nums, k), [2, 3])

    def test_edge_condition(self):
        nums = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        k = 1
        self.assertEqual(func(nums, k), [1])

    def test_boundary_condition(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        k = 10
        self.assertEqual(func(nums, k), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_invalid_input(self):
        nums = "not a list"
        k = 2
        with self.assertRaises(TypeError):
            func(nums, k)

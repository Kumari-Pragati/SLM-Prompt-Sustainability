import unittest
from mbpp_31_code import func

class TestFunc(unittest.TestCase):

    def test_typical_case(self):
        nums = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        k = 2
        self.assertEqual(func(nums, k), [3, 4])

    def test_edge_case(self):
        nums = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        k = 0
        self.assertEqual(func(nums, k), [])

    def test_corner_case(self):
        nums = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        k = 2
        self.assertEqual(func(nums, k), [1, 2])

    def test_invalid_input(self):
        nums = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        k = -1
        with self.assertRaises(Exception):
            func(nums, k)

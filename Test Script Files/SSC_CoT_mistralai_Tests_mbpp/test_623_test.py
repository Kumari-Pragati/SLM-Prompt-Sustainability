import unittest
from mbpp_623_code import nth_nums

class TestNthNums(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(nth_nums([1, 2, 3, 4], 2), [1, 4, 9, 16])
        self.assertEqual(nth_nums([5, 6, 7, 8], 3), [125, 216, 343, 512])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(nth_nums([], 2), [])
        self.assertEqual(nth_nums([0], 2), [0])
        self.assertEqual(nth_nums([-1, -2, -3], 3), [-1, -8, -27])
        self.assertEqual(nth_nums([1.0, 2.0, 3.0], 2), [1.0, 4.0, 9.0])
        self.assertEqual(nth_nums([1, 2, 3], 0), [1, 2, 3])

    def test_invalid_input(self):
        self.assertRaises(TypeError, lambda: nth_nums('abc', 2))
        self.assertRaises(TypeError, lambda: nth_nums([1, 2], 'n'))
        self.assertRaises(ValueError, lambda: nth_nums([], 0))

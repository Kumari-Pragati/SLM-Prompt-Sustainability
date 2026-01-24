import unittest
from mbpp_817_code import div_of_nums

class TestDivOfNums(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(div_of_nums([12, 18, 20, 24], 4, 6), [12, 18, 24])
        self.assertListEqual(div_of_nums([12, 18, 20, 24], 6, 4), [12, 18, 24])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(div_of_nums([0], 0, 1), [0])
        self.assertListEqual(div_of_nums([0], 1, 0), [])
        self.assertListEqual(div_of_nums([1], 2, 1), [])
        self.assertListEqual(div_of_nums([2], 1, 2), [2])
        self.assertListEqual(div_of_nums([-1, -2], -1, 1), [])
        self.assertListEqual(div_of_nums([-1, -2], 1, -1), [-1, -2])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, div_of_nums, [1, 2, 3], 'm', 'n')
        self.assertRaises(TypeError, div_of_nums, [1, 2, 3], 1.0, 2.0)
        self.assertRaises(TypeError, div_of_nums, [1, 2, 3], [], 2)
        self.assertRaises(TypeError, div_of_nums, [1, 2, 3], 1, [])

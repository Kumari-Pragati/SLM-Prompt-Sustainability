import unittest
from mbpp_883_code import div_of_nums

class TestDivOfNums(unittest.TestCase):

    def test_typical_input(self):
        self.assertListEqual(div_of_nums([10, 15, 20, 25], 5, 5), [10, 25])
        self.assertListEqual(div_of_nums([10, 15, 20, 25], 10, 5), [10])
        self.assertListEqual(div_of_nums([10, 15, 20, 25], 10, 10), [10, 25])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(div_of_nums([0], 0, 0), [])
        self.assertListEqual(div_of_nums([], 1, 2), [])
        self.assertListEqual(div_of_nums([1], 1, 1), [1])
        self.assertListEqual(div_of_nums([1, 2, 3], 0, 2), [])
        self.assertListEqual(div_of_nums([1, 2, 3], 2, 0), [])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, div_of_nums, [1, 2, 3], "m", 2)
        self.assertRaises(TypeError, div_of_nums, [1, 2, 3], 1, "n")

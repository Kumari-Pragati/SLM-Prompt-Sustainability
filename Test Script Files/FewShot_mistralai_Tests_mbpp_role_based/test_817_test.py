import unittest
from mbpp_817_code import div_of_nums

class TestDivOfNums(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertListEqual(div_of_nums([1, 2, 3, 4, 5], 2, 3), [2, 3, 4])
        self.assertListEqual(div_of_nums([6, 7, 8, 9, 10], 3, 4), [6, 9])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(div_of_nums([0], 2, 2), [0])
        self.assertListEqual(div_of_nums([1], 2, 2), [])
        self.assertListEqual(div_of_nums([1, 2, 3], 0, 2), [])
        self.assertListEqual(div_of_nums([1, 2, 3], 2, 0), [])
        self.assertListEqual(div_of_nums([], 2, 3), [])

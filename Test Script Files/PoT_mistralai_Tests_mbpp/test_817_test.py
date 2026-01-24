import unittest
from mbpp_817_code import div_of_nums

class TestDivOfNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(div_of_nums([12, 18, 24, 36], 4, 6), [12, 18, 24, 36])
        self.assertListEqual(div_of_nums([1, 2, 3, 4, 5], 2, 3), [1, 2, 3])
        self.assertListEqual(div_of_nums([10, 20, 30], 5, 10), [10, 20, 30])

    def test_edge_case_zero(self):
        self.assertListEqual(div_of_nums([], 2, 3), [])
        self.assertListEqual(div_of_nums([0], 2, 3), [])

    def test_edge_case_one(self):
        self.assertListEqual(div_of_nums([1], 2, 3), [1])

    def test_edge_case_negative(self):
        self.assertListEqual(div_of_nums([-1, -2, -3], 2, 3), [])

    def test_boundary_case_one(self):
        self.assertListEqual(div_of_nums([1], 2, 2), [])

    def test_boundary_case_zero(self):
        self.assertListEqual(div_of_nums([0], 0, 0), [])

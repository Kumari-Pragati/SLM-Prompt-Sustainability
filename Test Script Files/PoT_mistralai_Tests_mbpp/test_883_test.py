import unittest
from mbpp_883_code import div_of_nums

class TestDivOfNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(div_of_nums([12, 18, 24, 36], 3, 4), [12, 36])
        self.assertListEqual(div_of_nums([12, 18, 24, 36], 4, 3), [12])
        self.assertListEqual(div_of_nums([12, 18, 24, 36], 2, 9), [])

    def test_edge_case_zero(self):
        self.assertListEqual(div_of_nums([], 3, 4), [])
        self.assertListEqual(div_of_nums([0], 3, 4), [])

    def test_edge_case_one(self):
        self.assertListEqual(div_of_nums([1], 3, 4), [])
        self.assertListEqual(div_of_nums([1], 4, 3), [])

    def test_edge_case_negative(self):
        self.assertListEqual(div_of_nums([-12, -18, -24, -36], 3, 4), [])
        self.assertListEqual(div_of_nums([-12, -18, -24, -36], 4, 3), [])

    def test_corner_case_m_n_equal(self):
        self.assertListEqual(div_of_nums([12, 18, 24, 36], 3, 3), [12, 18, 24, 36])
        self.assertListEqual(div_of_nums([12, 18, 24, 36], 4, 4), [12, 18, 24, 36])

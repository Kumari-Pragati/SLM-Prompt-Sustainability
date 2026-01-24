import unittest
from mbpp_907_code import lucky_num

class TestLuckyNum(unittest.TestCase):

    def test_typical_input(self):
        self.assertListEqual(lucky_num(3), [1, 3, 5])
        self.assertListEqual(lucky_num(5), [1, 3, 5, 7])
        self.assertListEqual(lucky_num(7), [1, 3, 5, 7, 9])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(lucky_num(0), [])
        self.assertListEqual(lucky_num(1), [1])
        self.assertListEqual(lucky_num(2), [1])
        self.assertListEqual(lucky_num(4), [1, 3])
        self.assertListEqual(lucky_num(6), [1, 3, 5])
        self.assertListEqual(lucky_num(8), [1, 3, 5, 7])
        self.assertListEqual(lucky_num(9), [1, 3, 5, 7, 9])

    def test_special_cases(self):
        self.assertListEqual(lucky_num(10), [1, 3, 5, 7, 9, 11])
        self.assertListEqual(lucky_num(11), [1, 3, 5, 7, 9, 11, 13])
        self.assertListEqual(lucky_num(13), [1, 3, 5, 7, 9, 11, 13, 15])
        self.assertListEqual(lucky_num(15), [1, 3, 5, 7, 9, 11, 13, 15, 17])
        self.assertListEqual(lucky_num(17), [1, 3, 5, 7, 9, 11, 13, 15, 17, 19])

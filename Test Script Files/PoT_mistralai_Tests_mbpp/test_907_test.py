import unittest
from mbpp_907_code import lucky_num

class TestLuckyNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(lucky_num(3), [1, 3, 5, 7])
        self.assertListEqual(lucky_num(4), [1, 3, 5, 7, 9, 13])
        self.assertListEqual(lucky_num(5), [1, 3, 5, 7, 9, 13, 15])

    def test_edge_case(self):
        self.assertListEqual(lucky_num(0), [])
        self.assertListEqual(lucky_num(1), [1])
        self.assertListEqual(lucky_num(2), [1, 3])
        self.assertListEqual(lucky_num(6), [1, 3, 5, 7, 9, 13, 15, 17])

    def test_boundary_case(self):
        self.assertListEqual(lucky_num(1000), [1, 3, 5, 7, 9, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97])
        self.assertListEqual(lucky_num(-1), [])
        self.assertListEqual(lucky_num(-2), [])

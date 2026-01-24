import unittest
from mbpp_907_code import lucky_num

class TestLuckyNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(lucky_num(5), [0, 2, 4, 6, 8])

    def test_edge_case(self):
        self.assertEqual(lucky_num(1), [0])
        self.assertEqual(lucky_num(2), [0, 2])
        self.assertEqual(lucky_num(3), [0, 2, 4])
        self.assertEqual(lucky_num(4), [0, 2, 4, 6])
        self.assertEqual(lucky_num(9), [0, 2, 4, 6, 8])

    def test_boundary_case(self):
        self.assertEqual(lucky_num(0), [])
        self.assertEqual(lucky_num(10), [0, 2, 4, 6, 8, 10])

    def test_corner_case(self):
        self.assertEqual(lucky_num(-1), [])
        self.assertEqual(lucky_num(-2), [])

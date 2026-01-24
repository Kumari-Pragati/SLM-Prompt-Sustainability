import unittest
from mbpp_907_code import lucky_num

class TestLuckyNum(unittest.TestCase):

    def test_lucky_num(self):
        self.assertEqual(lucky_num(1), [0])
        self.assertEqual(lucky_num(2), [0, 2])
        self.assertEqual(lucky_num(3), [0, 2, 4])
        self.assertEqual(lucky_num(4), [0, 2, 4, 6])
        self.assertEqual(lucky_num(5), [0, 2, 4, 6, 8])
        self.assertEqual(lucky_num(6), [0, 2, 4, 6, 8, 10])
        self.assertEqual(lucky_num(7), [0, 2, 4, 6, 8, 10, 12])
        self.assertEqual(lucky_num(8), [0, 2, 4, 6, 8, 10, 12, 14])
        self.assertEqual(lucky_num(9), [0, 2, 4, 6, 8, 10, 12, 14, 16])
        self.assertEqual(lucky_num(10), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

    def test_lucky_num_edge_cases(self):
        self.assertEqual(lucky_num(0), [])
        self.assertEqual(lucky_num(-1), [])

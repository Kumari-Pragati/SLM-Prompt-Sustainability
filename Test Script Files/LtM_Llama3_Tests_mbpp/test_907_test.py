import unittest
from mbpp_907_code import lucky_num

class TestLuckyNum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(lucky_num(1), [0])
        self.assertEqual(lucky_num(2), [0, 2])
        self.assertEqual(lucky_num(3), [0, 2, 4])
        self.assertEqual(lucky_num(4), [0, 2, 4, 6])
        self.assertEqual(lucky_num(5), [0, 2, 4, 6, 8])

    def test_edge(self):
        self.assertEqual(lucky_num(0), [0])
        self.assertEqual(lucky_num(1), [0])
        self.assertEqual(lucky_num(-1), [-1, 1])
        self.assertEqual(lucky_num(9), [0, 2, 4, 6, 8])

    def test_complex(self):
        self.assertEqual(lucky_num(10), [0, 2, 4, 6, 8, 10])
        self.assertEqual(lucky_num(20), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
        self.assertEqual(lucky_num(-10), [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8])
        self.assertEqual(lucky_num(25), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])

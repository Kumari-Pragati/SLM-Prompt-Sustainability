import unittest
from mbpp_907_code import lucky_num

class TestLuckyNum(unittest.TestCase):

    def test_lucky_num_positive_numbers(self):
        self.assertEqual(lucky_num(1), [2])
        self.assertEqual(lucky_num(2), [4, 6])
        self.assertEqual(lucky_num(3), [8, 12, 16])
        self.assertEqual(lucky_num(4), [16, 24, 32, 40])

    def test_lucky_num_negative_numbers(self):
        self.assertEqual(lucky_num(-1), [])
        self.assertEqual(lucky_num(-2), [])

    def test_lucky_num_zero(self):
        self.assertEqual(lucky_num(0), [])

    def test_lucky_num_large_numbers(self):
        self.assertEqual(lucky_num(10), [128, 192, 256, 320, 384, 448, 512, 576, 640, 704])

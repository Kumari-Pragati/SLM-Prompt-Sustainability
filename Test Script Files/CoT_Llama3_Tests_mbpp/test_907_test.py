import unittest
from mbpp_907_code import lucky_num

class TestLuckyNum(unittest.TestCase):
    def test_lucky_num_positive(self):
        self.assertEqual(lucky_num(5), [0, 2, 4, 6, 8])

    def test_lucky_num_negative(self):
        self.assertEqual(lucky_num(-1), [])

    def test_lucky_num_zero(self):
        self.assertEqual(lucky_num(0), [])

    def test_lucky_num_one(self):
        self.assertEqual(lucky_num(1), [0])

    def test_lucky_num_large(self):
        self.assertEqual(lucky_num(10), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

    def test_lucky_num_invalid_input(self):
        with self.assertRaises(TypeError):
            lucky_num('a')

import unittest
from mbpp_907_code import lucky_num

class TestLuckyNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(lucky_num(5), [2, 4, 6, 8, 10])

    def test_small_number(self):
        self.assertEqual(lucky_num(1), [2])

    def test_large_number(self):
        self.assertEqual(lucky_num(10), [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    def test_negative_number(self):
        self.assertEqual(lucky_num(-1), [])

    def test_zero(self):
        self.assertEqual(lucky_num(0), [])

    def test_edge_case(self):
        self.assertEqual(lucky_num(2), [2, 4])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            lucky_num('5')

        with self.assertRaises(TypeError):
            lucky_num(None)

        with self.assertRaises(TypeError):
            lucky_num([])

        with self.assertRaises(TypeError):
            lucky_num({})

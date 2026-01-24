import unittest
from mbpp_907_code import lucky_num

class TestLuckyNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(lucky_num(5), [1, 3, 5, 7, 9])

    def test_edge_case_small_number(self):
        self.assertEqual(lucky_num(1), [1])

    def test_edge_case_large_number(self):
        self.assertEqual(lucky_num(10), [1, 3, 5, 7, 9, 11, 13, 15, 17, 19])

    def test_edge_case_zero(self):
        self.assertEqual(lucky_num(0), [])

    def test_negative_number(self):
        with self.assertRaises(IndexError):
            lucky_num(-1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            lucky_num(2.5)

    def test_large_number(self):
        with self.assertRaises(RecursionError):
            lucky_num(1000)

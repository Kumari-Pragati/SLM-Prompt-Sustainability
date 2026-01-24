import unittest
from mbpp_907_code import lucky_num

class TestLuckyNum(unittest.TestCase):
    def test_lucky_num_positive_integer(self):
        self.assertEqual(lucky_num(5), [1, 3, 5, 7, 9])

    def test_lucky_num_zero(self):
        self.assertEqual(lucky_num(0), [])

    def test_lucky_num_negative_integer(self):
        self.assertEqual(lucky_num(-1), [])

    def test_lucky_num_non_integer(self):
        with self.assertRaises(TypeError):
            lucky_num('a')

    def test_lucky_num_edge_case(self):
        self.assertEqual(lucky_num(1), [1])

    def test_lucky_num_edge_case_2(self):
        self.assertEqual(lucky_num(2), [1, 3])

    def test_lucky_num_edge_case_3(self):
        self.assertEqual(lucky_num(3), [1, 3, 5])

import unittest
from mbpp_211_code import count_Num

class TestCountNum(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(count_Num(1), 1)

    def test_positive_numbers(self):
        self.assertEqual(count_Num(2), 1)
        self.assertEqual(count_Num(3), 2)
        self.assertEqual(count_Num(4), 2)
        self.assertEqual(count_Num(5), 4)
        self.assertEqual(count_Num(6), 4)
        self.assertEqual(count_Num(7), 8)
        self.assertEqual(count_Num(8), 8)

    def test_zero(self):
        self.assertEqual(count_Num(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(count_Num(-1), 0)
        self.assertEqual(count_Num(-2), 0)
        self.assertEqual(count_Num(-3), 0)

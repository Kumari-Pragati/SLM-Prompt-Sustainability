import unittest
from mbpp_211_code import count_Num

class TestCountNum(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(count_Num(1), 1)

    def test_positive_numbers(self):
        for n in range(2, 10):
            self.assertEqual(count_Num(n), pow(2, n - 2))

    def test_large_number(self):
        self.assertEqual(count_Num(100), pow(2, 98))

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            count_Num(-1)

    def test_zero(self):
        with self.assertRaises(ValueError):
            count_Num(0)

    def test_fraction(self):
        with self.assertRaises(TypeError):
            count_Num(3.14)

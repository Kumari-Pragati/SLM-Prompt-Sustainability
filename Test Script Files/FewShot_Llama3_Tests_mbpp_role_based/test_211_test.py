import unittest
from mbpp_211_code import count_Num

class TestCount_Num(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(count_Num(1), 1)
        self.assertEqual(count_Num(2), 2)
        self.assertEqual(count_Num(3), 4)
        self.assertEqual(count_Num(4), 8)
        self.assertEqual(count_Num(5), 16)

    def test_negative_integer(self):
        with self.assertRaises(TypeError):
            count_Num(-1)

    def test_zero(self):
        with self.assertRaises(TypeError):
            count_Num(0)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            count_Num('a')

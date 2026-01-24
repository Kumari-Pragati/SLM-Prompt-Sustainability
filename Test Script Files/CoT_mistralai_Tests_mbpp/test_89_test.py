import unittest
from mbpp_89_code import MagicMock
from 89_code import closest_num

class TestClosestNum(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(closest_num(5), 4)

    def test_zero(self):
        self.assertEqual(closest_num(0), -1)

    def test_negative_integer(self):
        self.assertEqual(closest_num(-5), -6)

    def test_float(self):
        self.assertEqual(closest_num(3.14), 2)

    def test_string(self):
        with self.assertRaises(TypeError):
            closest_num('hello')

    def test_list(self):
        with self.assertRaises(TypeError):
            closest_num([1, 2, 3])

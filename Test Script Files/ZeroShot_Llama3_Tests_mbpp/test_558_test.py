import unittest
from mbpp_558_code import digit_distance_nums

class TestDigitDistanceNums(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(digit_distance_nums(123, 456), 9)

    def test_negative_numbers(self):
        self.assertEqual(digit_distance_nums(-123, 456), 9)

    def test_zero(self):
        self.assertEqual(digit_distance_nums(0, 0), 0)

    def test_negative_zero(self):
        self.assertEqual(digit_distance_nums(-0, 0), 0)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            digit_distance_nums(123.45, 456)

    def test_non_numeric(self):
        with self.assertRaises(TypeError):
            digit_distance_nums('123', 456)

    def test_non_integer_negative(self):
        with self.assertRaises(TypeError):
            digit_distance_nums(-123.45, 456)

    def test_non_numeric_negative(self):
        with self.assertRaises(TypeError):
            digit_distance_nums('-123', 456)

import unittest
from mbpp_558_code import digit_distance_nums

class TestDigitDistanceNums(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(digit_distance_nums(10, 20), 2)

    def test_negative_numbers(self):
        self.assertEqual(digit_distance_nums(-10, -20), 2)

    def test_positive_and_negative_numbers(self):
        self.assertEqual(digit_distance_nums(10, -20), 3)

    def test_zero(self):
        self.assertEqual(digit_distance_nums(0, 0), 0)

    def test_zero_and_non_zero(self):
        self.assertEqual(digit_distance_nums(0, 10), 1)

    def test_non_zero_and_zero(self):
        self.assertEqual(digit_distance_nums(10, 0), 1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            digit_distance_nums(10.5, 20)

    def test_non_integer2(self):
        with self.assertRaises(TypeError):
            digit_distance_nums("10", 20)

    def test_non_integer3(self):
        with self.assertRaises(TypeError):
            digit_distance_nums(10, "20")

    def test_non_integer4(self):
        with self.assertRaises(TypeError):
            digit_distance_nums("10", "20")

import unittest
from mbpp_558_code import digit_distance_nums

class TestDigitDistanceNums(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(digit_distance_nums(10, 20), 2)

    def test_negative_numbers(self):
        self.assertEqual(digit_distance_nums(-10, -20), 2)

    def test_zero(self):
        self.assertEqual(digit_distance_nums(0, 0), 0)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            digit_distance_nums('10', 20)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            digit_distance_nums('ten', 20)

    def test_large_numbers(self):
        self.assertEqual(digit_distance_nums(1000, 2000), 4)

    def test_small_numbers(self):
        self.assertEqual(digit_distance_nums(1, 2), 1)

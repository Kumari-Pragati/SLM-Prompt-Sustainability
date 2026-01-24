import unittest
from mbpp_558_code import digit_distance_nums

class TestDigitDistanceNums(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(digit_distance_nums(123, 456), 7)
        self.assertEqual(digit_distance_nums(987, 654), 5)
        self.assertEqual(digit_distance_nums(1024, 2048), 4)

    def test_negative_numbers(self):
        self.assertEqual(digit_distance_nums(-123, -456), 7)
        self.assertEqual(digit_distance_nums(-987, -654), 5)
        self.assertEqual(digit_distance_nums(-1024, -2048), 4)

    def test_zero(self):
        self.assertEqual(digit_distance_nums(0, 123), 3)
        self.assertEqual(digit_distance_nums(123, 0), 3)
        self.assertEqual(digit_distance_nums(0, 0), 0)

    def test_same_numbers(self):
        self.assertEqual(digit_distance_nums(123, 123), 0)

    def test_large_numbers(self):
        self.assertEqual(digit_distance_nums(1000000, 2000000), 3)
        self.assertEqual(digit_distance_nums(1000000000, 2000000000), 10)

    def test_negative_large_numbers(self):
        self.assertEqual(digit_distance_nums(-1000000, -2000000), 3)
        self.assertEqual(digit_distance_nums(-1000000000, -2000000000), 10)

    def test_error_cases(self):
        self.assertRaises(TypeError, digit_distance_nums, 'a', 'b')
        self.assertRaises(TypeError, digit_distance_nums, 1.23, 4)

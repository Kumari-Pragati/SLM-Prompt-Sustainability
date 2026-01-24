import unittest
from mbpp_558_code import digit_distance_nums

class TestDigitDistanceNums(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(digit_distance_nums(12, 34), 2)
        self.assertEqual(digit_distance_nums(987, 123), 8)
        self.assertEqual(digit_distance_nums(55, 56), 1)

    def test_negative_numbers(self):
        self.assertEqual(digit_distance_nums(-12, -34), 2)
        self.assertEqual(digit_distance_nums(-987, -123), 8)
        self.assertEqual(digit_distance_nums(-55, -56), 1)

    def test_zero(self):
        self.assertEqual(digit_distance_nums(0, 12), 1)
        self.assertEqual(digit_distance_nums(12, 0), 1)
        self.assertEqual(digit_distance_nums(0, 0), 0)

    def test_same_numbers(self):
        self.assertEqual(digit_distance_nums(12, 12), 0)

    def test_large_numbers(self):
        self.assertEqual(digit_distance_nums(1234567890, 9876543210), 10)

    def test_small_numbers(self):
        self.assertEqual(digit_distance_nums(1, 2), 1)
        self.assertEqual(digit_distance_nums(2, 1), 1)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, digit_distance_nums, 'a', 'b')
        self.assertRaises(TypeError, digit_distance_nums, 1.23, 4.56)

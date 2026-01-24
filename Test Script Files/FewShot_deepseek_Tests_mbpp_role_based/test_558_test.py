import unittest
from mbpp_558_code import digit_distance_nums

class TestDigitDistanceNums(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(digit_distance_nums(123, 456), 6)

    def test_boundary_conditions(self):
        self.assertEqual(digit_distance_nums(0, 0), 0)
        self.assertEqual(digit_distance_nums(999, 1000), 1)
        self.assertEqual(digit_distance_nums(1000, 999), 1)

    def test_negative_numbers(self):
        self.assertEqual(digit_distance_nums(-123, 456), 10)
        self.assertEqual(digit_distance_nums(123, -456), 10)
        self.assertEqual(digit_distance_nums(-123, -456), 10)

    def test_large_numbers(self):
        self.assertEqual(digit_distance_nums(1000000, 999999), 9)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            digit_distance_nums("123", 456)
        with self.assertRaises(TypeError):
            digit_distance_nums(123, "456")
        with self.assertRaises(TypeError):
            digit_distance_nums("123", "456")

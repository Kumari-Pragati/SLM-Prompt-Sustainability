import unittest
from mbpp_558_code import digit_distance_nums

class TestDigitDistanceNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(digit_distance_nums(123, 456), 5)

    def test_boundary_case_same_numbers(self):
        self.assertEqual(digit_distance_nums(111, 111), 0)

    def test_boundary_case_negative_numbers(self):
        self.assertEqual(digit_distance_nums(-123, 456), 10)

    def test_boundary_case_max_min_int(self):
        self.assertEqual(digit_distance_nums(int(1e9), int(-1e9)), 19)

    def test_error_case_non_integer_input(self):
        with self.assertRaises(TypeError):
            digit_distance_nums(123, 456.5)

    def test_error_case_string_input(self):
        with self.assertRaises(TypeError):
            digit_distance_nums("123", 456)

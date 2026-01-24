import unittest
from mbpp_558_code import digit_distance_nums

class TestDigitDistanceNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(digit_distance_nums(123, 456), 3)

    def test_edge_case_zero(self):
        self.assertEqual(digit_distance_nums(0, 0), 0)

    def test_edge_case_negative(self):
        self.assertEqual(digit_distance_nums(-123, 456), 3)

    def test_edge_case_large(self):
        self.assertEqual(digit_distance_nums(123456, 123456), 0)

    def test_edge_case_large_negative(self):
        self.assertEqual(digit_distance_nums(-123456, 123456), 9)

    def test_edge_case_large_positive(self):
        self.assertEqual(digit_distance_nums(123456, -123456), 9)

    def test_edge_case_large_negative_positive(self):
        self.assertEqual(digit_distance_nums(-123456, 123456), 9)

    def test_edge_case_large_negative_negative(self):
        self.assertEqual(digit_distance_nums(-123456, -123456), 0)

    def test_edge_case_large_positive_positive(self):
        self.assertEqual(digit_distance_nums(123456, 123456), 0)

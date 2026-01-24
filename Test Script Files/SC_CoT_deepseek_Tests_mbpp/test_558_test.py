import unittest
from mbpp_558_code import digit_distance_nums

class TestDigitDistanceNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(digit_distance_nums(123, 456), 6)

    def test_boundary_case(self):
        self.assertEqual(digit_distance_nums(0, 0), 0)

    def test_edge_case(self):
        self.assertEqual(digit_distance_nums(999999, 100000), 16)
        self.assertEqual(digit_distance_nums(100000, 999999), 16)

    def test_negative_numbers(self):
        self.assertEqual(digit_distance_nums(-123, 456), 12)
        self.assertEqual(digit_distance_nums(123, -456), 12)
        self.assertEqual(digit_distance_nums(-123, -456), 12)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            digit_distance_nums('123', 456)
        with self.assertRaises(TypeError):
            digit_distance_nums(123, '456')
        with self.assertRaises(TypeError):
            digit_distance_nums('123', '456')

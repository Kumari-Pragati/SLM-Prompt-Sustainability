import unittest
from mbpp_558_code import digit_distance_nums

class TestDigitDistanceNums(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(digit_distance_nums(123, 456), 5)
        self.assertEqual(digit_distance_nums(987, 654), 6)
        self.assertEqual(digit_distance_nums(100, 200), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(digit_distance_nums(0, 0), 0)
        self.assertEqual(digit_distance_nums(999, 0), 9)
        self.assertEqual(digit_distance_nums(1000, 999), 2)

    def test_corner_cases(self):
        self.assertEqual(digit_distance_nums(10000, 9999), 4)
        self.assertEqual(digit_distance_nums(99999, 100000), 5)
        self.assertEqual(digit_distance_nums(123456, 654321), 15)

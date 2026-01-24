import unittest
from mbpp_558_code import digit_distance_nums

class TestDigitDistanceNums(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(digit_distance_nums(123, 456), 7)
        self.assertEqual(digit_distance_nums(987, 654), 6)
        self.assertEqual(digit_distance_nums(1010, 1011), 1)

    def test_edge_cases(self):
        self.assertEqual(digit_distance_nums(0, 1), 1)
        self.assertEqual(digit_distance_nums(1, 0), 1)
        self.assertEqual(digit_distance_nums(-1, 1), 2)
        self.assertEqual(digit_distance_nums(1, -1), 2)

    def test_boundary_cases(self):
        self.assertEqual(digit_distance_nums(999999, 100000), 1)
        self.assertEqual(digit_distance_nums(100000, 999999), 1)
        self.assertEqual(digit_distance_nums(999999999, 1000000000), 9)
        self.assertEqual(digit_distance_nums(1000000000, 999999999), 9)

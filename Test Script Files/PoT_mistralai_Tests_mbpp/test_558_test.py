import unittest
from mbpp_558_code import digit_distance_nums

class TestDigitDistanceNums(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(digit_distance_nums(12, 21), 3)
        self.assertEqual(digit_distance_nums(100, 99), 1)
        self.assertEqual(digit_distance_nums(1000, 999), 1)
        self.assertEqual(digit_distance_nums(123456, 654321), 10)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(digit_distance_nums(0, 1), 1)
        self.assertEqual(digit_distance_nums(1, 0), 1)
        self.assertEqual(digit_distance_nums(-1, 1), 2)
        self.assertEqual(digit_distance_nums(1, -1), 2)
        self.assertEqual(digit_distance_nums(10**10, 10**10 + 1), 1)
        self.assertEqual(digit_distance_nums(10**10 + 1, 10**10), 1)

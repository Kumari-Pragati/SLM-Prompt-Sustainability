import unittest
from mbpp_558_code import digit_distance_nums

class TestDigitDistanceNums(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(digit_distance_nums(123, 456), 5)
        self.assertEqual(digit_distance_nums(987, 654), 6)

    def test_edge_conditions(self):
        self.assertEqual(digit_distance_nums(0, 0), 0)
        self.assertEqual(digit_distance_nums(1000, 999), 4)
        self.assertEqual(digit_distance_nums(-123, 123), 6)

    def test_boundary_conditions(self):
        self.assertEqual(digit_distance_nums(10**9, 0), 9)
        self.assertEqual(digit_distance_nums(0, 10**9), 9)
        self.assertEqual(digit_distance_nums(10**9, 10**9), 0)

    def test_complex_cases(self):
        self.assertEqual(digit_distance_nums(314159, 265358), 10)
        self.assertEqual(digit_distance_nums(123456789, 987654321), 18)

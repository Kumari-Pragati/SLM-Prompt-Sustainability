import unittest
from mbpp_558_code import digit_distance_nums

class TestDigitDistanceNums(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(digit_distance_nums(1, 2), 1)
        self.assertEqual(digit_distance_nums(10, 15), 5)
        self.assertEqual(digit_distance_nums(100, 101), 1)
        self.assertEqual(digit_distance_nums(1000, 1001), 1)

    def test_edge_and_boundary(self):
        self.assertEqual(digit_distance_nums(-1, 1), 2)
        self.assertEqual(digit_distance_nums(0, 1), 1)
        self.assertEqual(digit_distance_nums(1, 0), 1)
        self.assertEqual(digit_distance_nums(10**6, 10**6 + 1), 1)
        self.assertEqual(digit_distance_nums(10**6, 10**6 - 1), 10)

    def test_complex(self):
        self.assertEqual(digit_distance_nums(12345, 654321), 108)
        self.assertEqual(digit_distance_nums(123456789, 987654321), 111)
        self.assertEqual(digit_distance_nums(1234567890, 9876543210), 20)

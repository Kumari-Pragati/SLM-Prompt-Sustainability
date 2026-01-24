import unittest
from mbpp_566_code import sum_digits

class TestSumDigits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(sum_digits(123), 6)
        self.assertEqual(sum_digits(456), 15)
        self.assertEqual(sum_digits(789), 24)

    def test_edge_cases(self):
        self.assertEqual(sum_digits(0), 0)
        self.assertEqual(sum_digits(10), 1)
        self.assertEqual(sum_digits(100), 1)

    def test_boundary_cases(self):
        self.assertEqual(sum_digits(1000), 1)
        self.assertEqual(sum_digits(9999), 36)

    def test_corner_cases(self):
        self.assertEqual(sum_digits(10000), 1)
        self.assertEqual(sum_digits(99999), 36)

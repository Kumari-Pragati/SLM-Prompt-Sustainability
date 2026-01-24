import unittest
from mbpp_543_code import count_digits

class TestCountDigits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_digits(123, 456), 6)
        self.assertEqual(count_digits(0, 0), 1)
        self.assertEqual(count_digits(1000, 999), 4)

    def test_edge_cases(self):
        self.assertEqual(count_digits(0, 123), 3)
        self.assertEqual(count_digits(123, 0), 3)
        self.assertEqual(count_digits(-123, 456), 6)
        self.assertEqual(count_digits(123, -456), 6)

    def test_boundary_cases(self):
        self.assertEqual(count_digits(0, 1), 1)
        self.assertEqual(count_digits(1, 0), 1)
        self.assertEqual(count_digits(1, 1), 1)
        self.assertEqual(count_digits(sys.maxsize, 1), len(str(sys.maxsize)) + 1)
        self.assertEqual(count_digits(1, sys.maxsize), len(str(sys.maxsize)) + 1)

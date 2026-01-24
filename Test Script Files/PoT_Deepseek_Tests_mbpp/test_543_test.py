import unittest
from mbpp_543_code import count_digits

class TestCountDigits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_digits(123, 456), 3)
        self.assertEqual(count_digits(98765, 4321), 5)
        self.assertEqual(count_digits(0, 0), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_digits(0, 99999), 5)
        self.assertEqual(count_digits(99999, 0), 5)
        self.assertEqual(count_digits(10000, 9999), 5)
        self.assertEqual(count_digits(9999, 10000), 5)

    def test_corner_cases(self):
        self.assertEqual(count_digits(1000000000, 1000000000), 10)
        self.assertEqual(count_digits(9999999999, 0), 10)
        self.assertEqual(count_digits(0, 9999999999), 10)

import unittest
from mbpp_566_code import sum_digits

class TestSumDigits(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(sum_digits(12345), 15)
        self.assertEqual(sum_digits(98765), 21)
        self.assertEqual(sum_digits(10203040), 1 + 2 + 0 + 3 + 0 + 4 + 0 + 5)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_digits(0), 0)
        self.assertEqual(sum_digits(9), 9)
        self.assertEqual(sum_digits(100), 1 + 0 + 0)
        self.assertEqual(sum_digits(999), 9 + 9 + 9)
        self.assertEqual(sum_digits(123000), 1 + 2 + 3 + 0 + 0 + 0)
        self.assertEqual(sum_digits(999999), 9 + 9 + 9 + 9 + 9 + 9)

    def test_negative_numbers(self):
        self.assertEqual(sum_digits(-123), 1 + 2 + 3)
        self.assertEqual(sum_digits(-987), 9 + 8 + 7)
        self.assertEqual(sum_digits(-100), 1 + 0 + 0)
        self.assertEqual(sum_digits(-999), 9 + 9 + 9)

    def test_floats(self):
        self.assertEqual(round(sum_digits(123.456), 2), 1 + 2 + 3 + 4 + 5)
        self.assertEqual(round(sum_digits(-123.456), 2), 1 + 2 + 3)

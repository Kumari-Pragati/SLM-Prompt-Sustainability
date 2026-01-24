import unittest
from mbpp_657_code import first_Digit

class TestFirstDigit(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_Digit(123), 1)

    def test_edge_case_zero(self):
        self.assertEqual(first_Digit(0), 0)

    def test_edge_case_one(self):
        self.assertEqual(first_Digit(1), 1)

    def test_edge_case_negative(self):
        with self.assertRaises(ValueError):
            first_Digit(-1)

    def test_edge_case_large(self):
        self.assertEqual(first_Digit(1000000), 1)

    def test_edge_case_small(self):
        self.assertEqual(first_Digit(10), 1)

    def test_edge_case_single_digit(self):
        self.assertEqual(first_Digit(5), 5)

    def test_edge_case_multiple_digits(self):
        self.assertEqual(first_Digit(12345), 1)

    def test_edge_case_factorial(self):
        self.assertEqual(first_Digit(math.factorial(5)), 1)

    def test_edge_case_factorial_large(self):
        self.assertEqual(first_Digit(math.factorial(100)), 1)

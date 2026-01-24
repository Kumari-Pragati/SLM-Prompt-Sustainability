import unittest
from mbpp_365_code import count_Digit

class TestCountDigit(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(count_Digit(123), 3)
        self.assertEqual(count_Digit(0), 0)
        self.assertEqual(count_Digit(10), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Digit(-123), 3)
        self.assertEqual(count_Digit(999_999_999), 10)
        self.assertEqual(count_Digit(0.123), 1)
        self.assertEqual(count_Digit(1e100), 100)

    def test_complex_cases(self):
        self.assertEqual(count_Digit(1234567890), 10)
        self.assertEqual(count_Digit(123000), 4)
        self.assertEqual(count_Digit(123_000_000), 7)
        self.assertEqual(count_Digit(123_456_789_012), 15)

import unittest
from mbpp_365_code import count_Digit

class TestCountDigit(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(count_Digit(123), 3)
        self.assertEqual(count_Digit(0), 0)
        self.assertEqual(count_Digit(1000), 3)
        self.assertEqual(count_Digit(987654321), 10)

    def test_edge_cases(self):
        self.assertEqual(count_Digit(-123), 3)
        self.assertEqual(count_Digit(0.123), 1)
        self.assertEqual(count_Digit(1e100), 100)

    def test_corner_cases(self):
        self.assertEqual(count_Digit(10 ** 18), 18)
        self.assertEqual(count_Digit(10 ** 365), 365)

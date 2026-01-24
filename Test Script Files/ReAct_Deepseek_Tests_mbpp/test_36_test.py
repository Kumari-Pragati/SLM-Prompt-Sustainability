import unittest
from mbpp_36_code import find_Nth_Digit

class TestFindNthDigit(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Nth_Digit(10, 3, 1), 3)

    def test_zero_N(self):
        self.assertEqual(find_Nth_Digit(10, 3, 0), 10)

    def test_large_N(self):
        self.assertEqual(find_Nth_Digit(10, 3, 10), 0)

    def test_negative_N(self):
        self.assertEqual(find_Nth_Digit(10, 3, -1), 10)

    def test_zero_p(self):
        self.assertEqual(find_Nth_Digit(0, 3, 1), 0)

    def test_zero_q(self):
        self.assertEqual(find_Nth_Digit(10, 0, 1), None)  # Assuming None is returned for division by zero

    def test_negative_values(self):
        self.assertEqual(find_Nth_Digit(-10, -3, 1), None)  # Assuming None is returned for negative values

    def test_large_values(self):
        self.assertEqual(find_Nth_Digit(10**10, 3, 1), 3)

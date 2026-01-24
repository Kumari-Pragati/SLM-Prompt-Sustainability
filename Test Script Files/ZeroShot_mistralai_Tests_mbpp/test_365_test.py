import unittest
from mbpp_365_code import count_Digit

class TestCountDigit(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(count_Digit(0), 0)

    def test_positive_numbers(self):
        for num in [1, 10, 123, 12345, 1234567]:
            self.assertEqual(count_Digit(num), len(str(num)))

    def test_negative_numbers(self):
        for num in [-1, -10, -123, -12345, -1234567]:
            self.assertEqual(count_Digit(num), len(str(abs(num))))

import unittest
from mbpp_657_code import first_Digit

class TestFirstDigit(unittest.TestCase):

    def test_first_Digit_positive(self):
        self.assertEqual(first_Digit(5), 120)
        self.assertEqual(first_Digit(10), 3628800)
        self.assertEqual(first_Digit(15), 1307674368000)

    def test_first_Digit_zero(self):
        self.assertEqual(first_Digit(0), 1)

    def test_first_Digit_negative(self):
        self.assertEqual(first_Digit(-5), 120)

    def test_first_Digit_large_number(self):
        self.assertEqual(first_Digit(20), 2432902008176640000)

import unittest
from mbpp_657_code import first_Digit

class TestFirstDigit(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(first_Digit(0), 0)

    def test_one(self):
        self.assertEqual(first_Digit(1), 1)

    def test_two(self):
        self.assertEqual(first_Digit(2), 2)

    def test_ten(self):
        self.assertEqual(first_Digit(10), 1)

    def test_twenty(self):
        self.assertEqual(first_Digit(20), 2)

    def test_hundred(self):
        self.assertEqual(first_Digit(100), 1)

    def test_thousand(self):
        self.assertEqual(first_Digit(1000), 1)

    def test_large_number(self):
        self.assertEqual(first_Digit(123456789), 8)

    def test_negative_number(self):
        self.assertEqual(first_Digit(-123), -1)

    def test_large_negative_number(self):
        self.assertEqual(first_Digit(-123456789), 8)

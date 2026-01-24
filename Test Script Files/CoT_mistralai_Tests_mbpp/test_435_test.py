import unittest
from mbpp_435_code import last_Digit

class TestLastDigit(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(last_Digit(12345), 5)
        self.assertEqual(last_Digit(9876), 6)
        self.assertEqual(last_Digit(10), 0)
        self.assertEqual(last_Digit(100), 0)
        self.assertEqual(last_Digit(1000), 0)

    def test_negative_numbers(self):
        self.assertEqual(last_Digit(-12345), 5)
        self.assertEqual(last_Digit(-9876), 6)
        self.assertEqual(last_Digit(-10), 0)
        self.assertEqual(last_Digit(-100), 0)
        self.assertEqual(last_Digit(-1000), 0)

    def test_zero(self):
        self.assertEqual(last_Digit(0), 0)

    def test_floats(self):
        self.assertEqual(last_Digit(12.345), 5)
        self.assertEqual(last_Digit(-12.345), 5)
        self.assertEqual(last_Digit(12e3), 3)
        self.assertEqual(last_Digit(-12e3), 3)

    def test_strings(self):
        self.assertEqual(last_Digit('12345'), 5)
        self.assertEqual(last_Digit('-12345'), 5)
        self.assertEqual(last_Digit('12345abc'), 5)
        self.assertEqual(last_Digit('-12345abc'), 5)

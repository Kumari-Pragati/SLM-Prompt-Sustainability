import unittest
from mbpp_365_code import count_Digit

class TestCountDigit(unittest.TestCase):

    def test_count_digit_positive_integer(self):
        self.assertEqual(count_Digit(123), 3)
        self.assertEqual(count_Digit(987654321), 10)
        self.assertEqual(count_Digit(1000000000), 10)

    def test_count_digit_zero(self):
        self.assertEqual(count_Digit(0), 0)

    def test_count_digit_negative_integer(self):
        self.assertEqual(count_Digit(-123), 3)
        self.assertEqual(count_Digit(-987654321), 10)
        self.assertEqual(count_Digit(-1000000000), 10)

    def test_count_digit_float(self):
        self.assertEqual(count_Digit(123.456), 3)
        self.assertEqual(count_Digit(987654321.012), 10)
        self.assertEqual(count_Digit(1000000000.5), 17)

    def test_count_digit_string(self):
        self.assertEqual(count_Digit('123'), 3)
        self.assertEqual(count_Digit('987654321'), 10)
        self.assertEqual(count_Digit('1000000000'), 10)

    def test_count_digit_empty_string(self):
        self.assertEqual(count_Digit(''), 0)

    def test_count_digit_none(self):
        self.assertEqual(count_Digit(None), 0)

import unittest
from mbpp_832_code import extract_max

class TestExtractMax(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(extract_max('1'), 1)

    def test_multiple_digits(self):
        self.assertEqual(extract_max('12345'), 5)

    def test_mixed_text_numbers(self):
        self.assertEqual(extract_max('abc123def456'), 6)

    def test_no_numbers(self):
        self.assertIsNone(extract_max('abcdef'))

    def test_negative_numbers(self):
        self.assertEqual(extract_max('-123-456-789'), 9)

    def test_decimal_numbers(self):
        self.assertEqual(extract_max('1.23,4.56,7.89'), 9)

    def test_empty_string(self):
        self.assertIsNone(extract_max(''))

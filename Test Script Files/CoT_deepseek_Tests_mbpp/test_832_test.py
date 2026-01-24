import unittest
from mbpp_832_code import extract_max

class TestExtractMax(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_max('abc123def456'), 456)

    def test_single_digit(self):
        self.assertEqual(extract_max('1'), 1)

    def test_multiple_digits(self):
        self.assertEqual(extract_max('123456789'), 9)

    def test_no_digits(self):
        self.assertIsNone(extract_max('abcde'))

    def test_negative_numbers(self):
        self.assertEqual(extract_max('-123456-789'), 9)

    def test_float_numbers(self):
        self.assertEqual(extract_max('123.456'), 456)

    def test_empty_string(self):
        self.assertIsNone(extract_max(''))

    def test_special_characters(self):
        self.assertEqual(extract_max('abc123!@#456'), 456)

    def test_whitespace(self):
        self.assertEqual(extract_max('abc123  456'), 456)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            extract_max(123456)

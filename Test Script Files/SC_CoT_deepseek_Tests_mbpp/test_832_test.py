import unittest
from mbpp_832_code import extract_max

class TestExtractMax(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_max('abc123def456'), 456)

    def test_single_digit(self):
        self.assertEqual(extract_max('1'), 1)

    def test_multiple_digits(self):
        self.assertEqual(extract_max('1234567890'), 90)

    def test_no_digits(self):
        self.assertIsNone(extract_max('abcdef'))

    def test_negative_numbers(self):
        self.assertEqual(extract_max('-123456-7890'), 7890)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            extract_max(123456)

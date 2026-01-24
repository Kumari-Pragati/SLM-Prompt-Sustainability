import unittest
from mbpp_764_code import number_ctr

class TestNumberCtr(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(number_ctr(''), 0)

    def test_single_digit(self):
        self.assertEqual(number_ctr('1'), 1)

    def test_multiple_digits(self):
        self.assertEqual(number_ctr('12345'), 5)

    def test_leading_zero(self):
        self.assertEqual(number_ctr('012345'), 5)

    def test_trailing_zero(self):
        self.assertEqual(number_ctr('123450'), 5)

    def test_mixed_characters(self):
        self.assertEqual(number_ctr('A1B2C3'), 3)

    def test_negative_numbers(self):
        self.assertEqual(number_ctr('-123'), 3)

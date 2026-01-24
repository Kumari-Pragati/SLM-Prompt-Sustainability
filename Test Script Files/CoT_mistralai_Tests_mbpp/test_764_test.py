import unittest
from mbpp_764_code import number_ctr

class TestNumberCtr(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(number_ctr(''), 0)

    def test_single_digit(self):
        self.assertEqual(number_ctr('5'), 1)

    def test_multiple_digits(self):
        self.assertEqual(number_ctr('12345'), 5)

    def test_leading_zero(self):
        self.assertEqual(number_ctr('012345'), 5)

    def test_trailing_zero(self):
        self.assertEqual(number_ctr('123450'), 5)

    def test_leading_and_trailing_zero(self):
        self.assertEqual(number_ctr('0123450'), 5)

    def test_only_digits(self):
        self.assertEqual(number_ctr('123456789'), 9)

    def test_mixed_string(self):
        self.assertEqual(number_ctr('A1B2C3D4'), 4)

    def test_negative_number(self):
        self.assertEqual(number_ctr('-123'), 3)

    def test_alphabet_only(self):
        self.assertEqual(number_ctr('abcdefg'), 0)

    def test_special_characters(self):
        self.assertEqual(number_ctr('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), 0)

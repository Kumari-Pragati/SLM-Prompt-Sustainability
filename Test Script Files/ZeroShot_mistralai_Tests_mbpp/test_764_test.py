import unittest
from764_code import number_ctr

class TestNumberCtr(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(number_ctr(''), 0)

    def test_string_with_only_spaces(self):
        self.assertEqual(number_ctr('   '), 0)

    def test_string_with_only_numbers(self):
        self.assertEqual(number_ctr('123456'), 6)

    def test_string_with_numbers_and_letters(self):
        self.assertEqual(number_ctr('A1B2C3D4'), 4)

    def test_string_with_numbers_and_special_characters(self):
        self.assertEqual(number_ctr('1#$%&4@5Z'), 3)

    def test_string_with_leading_numbers(self):
        self.assertEqual(number_ctr('123abc'), 3)

    def test_string_with_trailing_numbers(self):
        self.assertEqual(number_ctr('abc123'), 2)

    def test_string_with_numbers_in_middle(self):
        self.assertEqual(number_ctr('abc123def456'), 4)

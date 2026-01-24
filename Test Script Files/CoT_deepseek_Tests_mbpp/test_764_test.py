import unittest
from mbpp_764_code import number_ctr

class TestNumberCtr(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(number_ctr('abc123def456'), 6)

    def test_no_numbers(self):
        self.assertEqual(number_ctr('abcdefghijklmnopqrstuvwxyz'), 0)

    def test_empty_string(self):
        self.assertEqual(number_ctr(''), 0)

    def test_single_number(self):
        self.assertEqual(number_ctr('1'), 1)

    def test_all_numbers(self):
        self.assertEqual(number_ctr('1234567890'), 10)

    def test_mixed_case(self):
        self.assertEqual(number_ctr('a1b2c3d4e5'), 5)

    def test_special_characters(self):
        self.assertEqual(number_ctr('abc!@#123def$%^456ghi*()'), 6)

    def test_whitespace(self):
        self.assertEqual(number_ctr('abc 123 def 456'), 6)

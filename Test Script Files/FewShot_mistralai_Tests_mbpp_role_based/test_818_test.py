import unittest
from mbpp_818_code import lower_ctr

class TestLowerCtr(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(lower_ctr(''), 0)

    def test_single_uppercase_letter(self):
        self.assertEqual(lower_ctr('A'), 0)

    def test_single_lowercase_letter(self):
        self.assertEqual(lower_ctr('a'), 1)

    def test_mixed_case_string(self):
        self.assertEqual(lower_ctr('Hello, World!'), 10)

    def test_long_string(self):
        self.assertEqual(lower_ctr('abcdefghijklmnopqrstuvwxyz'), 26)

    def test_string_with_non_alphabetic_characters(self):
        self.assertEqual(lower_ctr('Hello123World!'), 10)

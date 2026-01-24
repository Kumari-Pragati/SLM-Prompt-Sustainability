import unittest
from mbpp_967_code import check

class TestCheck(unittest.TestCase):
    def test_accepted_string(self):
        self.assertEqual(check("AEIOUaeiou"), 'accepted')

    def test_not_accepted_string(self):
        self.assertEqual(check("BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"), 'not accepted')

    def test_string_with_mixed_case(self):
        self.assertEqual(check("aEIoUaeiou"), 'accepted')

    def test_string_with_no_vowels(self):
        self.assertEqual(check("BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"), 'not accepted')

    def test_string_with_no_characters(self):
        self.assertEqual(check(""), 'not accepted')

    def test_string_with_non_alphabetic_characters(self):
        self.assertEqual(check("AEIOUaeiou123"), 'accepted')

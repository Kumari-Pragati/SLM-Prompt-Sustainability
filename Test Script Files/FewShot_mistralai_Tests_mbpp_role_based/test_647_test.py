import unittest
from mbpp_647_code import split_upperstring

class TestSplitUpperstring(unittest.TestCase):
    def test_empty_string(self):
        self.assertListEqual(split_upperstring(''), [])

    def test_single_uppercase_letter(self):
        self.assertListEqual(split_upperstring('A'), ['A'])

    def test_multiple_uppercase_letters(self):
        self.assertListEqual(split_upperstring('ABC'), ['AB', 'C'])

    def test_mixed_case_string(self):
        self.assertListEqual(split_upperstring('aBc'), ['B', 'C'])

    def test_multiple_uppercase_and_lowercase_letters(self):
        self.assertListEqual(split_upperstring('AbCdEf'), ['A', 'C', 'E'])

    def test_string_with_only_lowercase_letters(self):
        self.assertListEqual(split_upperstring('abc'), [])

    def test_string_with_numbers(self):
        self.assertListEqual(split_upperstring('AB12C'), ['AB', 'C'])

    def test_string_with_special_characters(self):
        self.assertListEqual(split_upperstring('AB!@#C'), ['AB', 'C'])

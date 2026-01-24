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
        self.assertListEqual(split_upperstring('aBcDeFg'), ['B', 'C', 'F'])

    def test_leading_uppercase_letter(self):
        self.assertListEqual(split_upperstring('AB123'), ['A', 'B123'])

    def test_trailing_uppercase_letter(self):
        self.assertListEqual(split_upperstring('abcZ'), ['abc', 'Z'])

    def test_uppercase_in_middle(self):
        self.assertListEqual(split_upperstring('abCdEf'), ['ab', 'C', 'dE', 'f'])

    def test_multiple_consecutive_uppercase_letters(self):
        self.assertListEqual(split_upperstring('AA'), ['A', 'A'])

    def test_multiple_consecutive_uppercase_letters_with_spaces(self):
        self.assertListEqual(split_upperstring(' A   AA  B  CC  DDD  E'), ['A', 'A', 'B', 'C', 'C', 'D', 'D', 'D', 'E'])

    def test_punctuation_before_uppercase(self):
        self.assertListEqual(split_upperstring('.,!?ABC'), ['.', '!', '?', 'A', 'B', 'C'])

    def test_punctuation_after_uppercase(self):
        self.assertListEqual(split_upperstring('ABC.,!? '), ['A', 'B', 'C', '. ', '!', ' '])

    def test_punctuation_in_middle(self):
        self.assertListEqual(split_upperstring('.,!?ABC.,!? '), ['.', '!', 'A', 'B', 'C', '.', '!', ' '])

    def test_multiple_consecutive_punctuation(self):
        self.assertListEqual(split_upperstring('.,!?.,!?'), ['.', '!', '.', '!', '.'])

    def test_empty_words(self):
        self.assertListEqual(split_upperstring('   AB   C   '), ['A', 'B', 'C'])

    def test_whitespace_only(self):
        self.assertListEqual(split_upperstring('   '), [])

    def test_non_alphabetic_characters(self):
        self.assertListEqual(split_upperstring('123ABC'), ['123', 'ABC'])

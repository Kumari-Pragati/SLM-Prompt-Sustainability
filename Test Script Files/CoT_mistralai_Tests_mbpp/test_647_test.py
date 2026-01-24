import unittest
from mbpp_647_code import split_upperstring

class TestSplitUpperstring(unittest.TestCase):
    def test_empty_string(self):
        self.assertListEqual(split_upperstring(''), [])

    def test_single_uppercase_letter(self):
        self.assertListEqual(split_upperstring('A'), ['A'])

    def test_multiple_uppercase_letters(self):
        self.assertListEqual(split_upperstring('ABC'), ['AB', 'C'])

    def test_uppercase_with_spaces(self):
        self.assertListEqual(split_upperstring('ABC DEF'), ['ABC', 'DEF'])

    def test_uppercase_with_numbers(self):
        self.assertListEqual(split_upperstring('ABC123'), ['ABC'])

    def test_uppercase_with_special_characters(self):
        self.assertListEqual(split_upperstring('ABC!@#$%'), ['ABC'])

    def test_uppercase_with_mixed_case(self):
        self.assertListEqual(split_upperstring('aBc'), [])
        self.assertListEqual(split_upperstring('AbC'), ['Ab'])
        self.assertListEqual(split_upperstring('AbCd'), ['Ab', 'Cd'])

    def test_uppercase_with_multiple_spaces(self):
        self.assertListEqual(split_upperstring(' A B C '), ['A', 'B', 'C'])

    def test_uppercase_with_multiple_whitespace_characters(self):
        self.assertListEqual(split_upperstring('\tABC\n\r'), ['ABC'])

    def test_invalid_input_empty_string_with_space(self):
        with self.assertRaises(ValueError):
            split_upperstring(' ')

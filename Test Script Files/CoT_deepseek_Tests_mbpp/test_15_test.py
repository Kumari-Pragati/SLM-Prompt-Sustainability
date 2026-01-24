import unittest
from mbpp_15_code import split_lowerstring

class TestSplitLowerstring(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(split_lowerstring('HelloWorld'), ['ello', 'orld'])

    def test_single_letter(self):
        self.assertEqual(split_lowerstring('a'), ['a'])

    def test_no_lowercase(self):
        self.assertEqual(split_lowerstring('HELLO'), ['HELLO'])

    def test_empty_string(self):
        self.assertEqual(split_lowerstring(''), [])

    def test_mixed_case(self):
        self.assertEqual(split_lowerstring('HelloWORLD'), ['ello', 'ORLD'])

    def test_numbers_and_symbols(self):
        self.assertEqual(split_lowerstring('Hello123World456'), ['ello', 'orld'])

    def test_special_characters(self):
        self.assertEqual(split_lowerstring('Hello@World#'), ['ello', 'orld'])

    def test_whitespace(self):
        self.assertEqual(split_lowerstring('Hello World'), ['ello', 'orld'])

    def test_lowercase_with_whitespace(self):
        self.assertEqual(split_lowerstring('Hello World'), ['ello', 'orld'])

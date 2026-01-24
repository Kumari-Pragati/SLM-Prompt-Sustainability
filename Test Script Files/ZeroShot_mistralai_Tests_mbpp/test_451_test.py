import unittest
from mbpp_451_code import remove_whitespaces

class TestRemoveWhitespaces(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_whitespaces(''), '')

    def test_single_whitespace(self):
        self.assertEqual(remove_whitespaces(' '), '')
        self.assertEqual(remove_whitespaces('\t'), '')
        self.assertEqual(remove_whitespaces('\n'), '\n')

    def test_multiple_whitespaces(self):
        self.assertEqual(remove_whitespaces('   \t\n  '), '')

    def test_single_character(self):
        self.assertEqual(remove_whitespaces('a'), 'a')
        self.assertEqual(remove_whitespaces('A'), 'A')
        self.assertEqual(remove_whitespaces('0'), '0')

    def test_multiple_characters(self):
        self.assertEqual(remove_whitespaces('abcd'), 'abcd')
        self.assertEqual(remove_whitespaces('ABCd'), 'ABCd')
        self.assertEqual(remove_whitespaces('0123'), '0123')

    def test_whitespace_at_beginning_and_end(self):
        self.assertEqual(remove_whitespaces('   abcd   '), 'abcd')
        self.assertEqual(remove_whitespaces('\tABCd\n'), 'ABCd')

    def test_whitespace_in_middle(self):
        self.assertEqual(remove_whitespaces('ab cd'), 'abcd')
        self.assertEqual(remove_whitespaces('AB CD'), 'ABCD')
        self.assertEqual(remove_whitespaces('01 23'), '0123')

import unittest
from mbpp_708_code import Convert

class TestConvert(unittest.TestCase):

    def test_convert_single_word(self):
        self.assertEqual(Convert('Hello'), ['Hello'])

    def test_convert_multiple_words(self):
        self.assertEqual(Convert('Hello World'), ['Hello', 'World'])

    def test_convert_empty_string(self):
        self.assertEqual(Convert(''), [])

    def test_convert_whitespace_only(self):
        self.assertEqual(Convert('   '), [''])

    def test_convert_numbers_and_symbols(self):
        self.assertEqual(Convert('123@#$456'), ['123@#$456'])

    def test_convert_mixed_case(self):
        self.assertEqual(Convert('Hello WoRlD'), ['Hello', 'WoRlD'])

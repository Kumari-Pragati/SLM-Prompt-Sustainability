import unittest
from mbpp_337_code import text_match_word

class TestTextMatchWord(unittest.TestCase):

    def test_match_word(self):
        self.assertEqual(text_match_word('HelloWorld'), 'Found a match!')
        self.assertEqual(text_match_word('HelloWorld123'), 'Found a match!')
        self.assertEqual(text_match_word('HelloWorld '), 'Found a match!')
        self.assertEqual(text_match_word('HelloWorld!'), 'Found a match!')
        self.assertEqual(text_match_word('HelloWorld!@#'), 'Found a match!')
        self.assertEqual(text_match_word('HelloWorld!@# '), 'Found a match!')
        self.assertEqual(text_match_word('HelloWorld!@#123'), 'Found a match!')
        self.assertEqual(text_match_word('HelloWorld!@#123 '), 'Found a match!')

    def test_no_match_word(self):
        self.assertEqual(text_match_word('HelloWorld!@#1234'), 'Not matched!')
        self.assertEqual(text_match_word('HelloWorld!@#1234 '), 'Not matched!')
        self.assertEqual(text_match_word('HelloWorld!@#12345'), 'Not matched!')
        self.assertEqual(text_match_word('HelloWorld!@#12345 '), 'Not matched!')

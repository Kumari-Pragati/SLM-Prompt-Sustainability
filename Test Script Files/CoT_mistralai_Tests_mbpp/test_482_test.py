import unittest
from mbpp_482_code import match

class TestMatchFunction(unittest.TestCase):
    def test_uppercase_and_lowercase_words(self):
        self.assertEqual(match('ABCdef'), 'Yes')
        self.assertEqual(match('abcDef'), 'Yes')
        self.assertEqual(match('AbCdEf'), 'Yes')

    def test_single_word(self):
        self.assertEqual(match('ABC'), 'Yes')
        self.assertEqual(match('abc'), 'No')
        self.assertEqual(match('AbC'), 'No')

    def test_empty_string(self):
        self.assertEqual(match(''), 'No')

    def test_special_characters(self):
        self.assertEqual(match('123ABCdef'), 'No')
        self.assertEqual(match('ABCdef_'), 'No')
        self.assertEqual(match('ABCdef.'), 'No')

    def test_numbers(self):
        self.assertEqual(match('ABC123def'), 'No')
        self.assertEqual(match('ABCdef123'), 'No')
        self.assertEqual(match('123ABCdef'), 'No')

    def test_punctuation(self):
        self.assertEqual(match('ABCdef.'), 'No')
        self.assertEqual(match('ABCdef,', 'Yes'), 'No')
        self.assertEqual(match('ABCdef!'), 'No')

    def test_whitespace(self):
        self.assertEqual(match('ABC def'), 'No')
        self.assertEqual(match('ABC   def'), 'No')
        self.assertEqual(match('   ABC def'), 'No')

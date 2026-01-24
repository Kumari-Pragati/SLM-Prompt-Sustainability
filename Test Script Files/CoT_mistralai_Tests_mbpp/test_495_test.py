import unittest
from mbpp_495_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_lowercase(''), '')

    def test_single_uppercase_letter(self):
        for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            self.assertEqual(remove_lowercase(char), char)

    def test_single_uppercase_word(self):
        for word in ['HELLO', 'WORLD', 'PYTHON']:
            self.assertEqual(remove_lowercase(word), word.upper())

    def test_multiple_uppercase_words(self):
        for word in ['HELLO WORLD', 'PYTHON IS AWESOME', 'GOODBYE UNITTEST']:
            self.assertEqual(remove_lowercase(word), word.upper().replace(' ', ''))

    def test_mixed_case_word(self):
        for word in ['HelloWorld', 'PythonIsAwesome', 'GoodbyeUnitTest']:
            self.assertEqual(remove_lowercase(word), word.upper().replace(' ', ''))

    def test_punctuation_and_numbers(self):
        for word in ['Hello123World!', 'Python456IsAwesome@', 'Goodbye789UnitTest?']:
            self.assertEqual(remove_lowercase(word), word.upper().replace(' ', '').replace(r'\d', '').replace(r'\W', ''))

    def test_multiple_spaces(self):
        self.assertEqual(remove_lowercase('  Hello   World  '), 'HELLO   WORLD')

    def test_leading_trailing_spaces(self):
        self.assertEqual(remove_lowercase('   Hello   World   '), 'HELLO   WORLD')
        self.assertEqual(remove_lowercase('Hello   World   '), 'HELLO   WORLD')
        self.assertEqual(remove_lowercase('   Hello   World  '), 'HELLO   WORLD')

    def test_empty_list(self):
        self.assertEqual(remove_lowercase([]), [])

    def test_single_empty_string(self):
        self.assertEqual(remove_lowercase(['']), [''])

    def test_single_uppercase_string(self):
        for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            self.assertEqual(remove_lowercase(['' + char]), [char])

    def test_single_mixed_case_string(self):
        for word in ['HelloWorld', 'PythonIsAwesome', 'GoodbyeUnitTest']:
            self.assertEqual(remove_lowercase([word]), [word.upper()])

    def test_multiple_strings(self):
        for words in [('HelloWorld', 'PythonIsAwesome', 'GoodbyeUnitTest'), ('HELLO', 'WORLD', 'PYTHON'), ('123', '456', '789')]:
            self.assertEqual(remove_lowercase(words), [words[0].upper(), words[1].upper(), words[2].upper()])

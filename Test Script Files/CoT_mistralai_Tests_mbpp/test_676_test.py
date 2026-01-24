import unittest
from mbpp_676_code import remove_extra_char

class TestRemoveExtraChar(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_extra_char(''), '')

    def test_single_word(self):
        self.assertEqual(remove_extra_char('word'), 'word')

    def test_multiple_words(self):
        self.assertEqual(remove_extra_char('word1 word2 word3'), 'word1word2word3')

    def test_punctuation(self):
        self.assertEqual(remove_extra_char('word,.,!'), 'word')

    def test_numbers(self):
        self.assertEqual(remove_extra_char('word123'), 'word123')

    def test_mixed_case(self):
        self.assertEqual(remove_extra_char('Word123_'), 'word123')

    def test_special_characters(self):
        self.assertEqual(remove_extra_char('word#$%^&*()_+-=[]{}|;:<>,.?/'), 'word')

    def test_multiple_extra_chars(self):
        self.assertEqual(remove_extra_char('Word_123_'), 'word123')

    def test_long_string(self):
        long_string = 'This is a very long string with extra characters like _ , . and !'
        expected_output = 'Thisisaverylongstringwithextracharacterslike'
        self.assertEqual(remove_extra_char(long_string), expected_output)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_extra_char(123)

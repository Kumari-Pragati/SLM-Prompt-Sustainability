import unittest
from mbpp_956_code import split_list

class TestSplitList(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(split_list(''), [])

    def test_single_word(self):
        self.assertEqual(split_list('Word'), ['Word', ])

    def test_multiple_words(self):
        self.assertEqual(split_list('This is a test'), ['This', 'is', 'a', 'test'])

    def test_mixed_case(self):
        self.assertEqual(split_list('ThIs Is A TeSt'), ['ThIs', 'Is', 'A', 'TeSt'])

    def test_punctuation(self):
        self.assertEqual(split_list('This, is, a, test.'), ['This', 'is', 'a', 'test'])

    def test_numbers(self):
        self.assertEqual(split_list('This123 is a test456'), ['This', '123', 'is', 'a', 'test', '456'])

    def test_special_characters(self):
        self.assertEqual(split_list('This$%^&*()_ is a test.'), ['This', '$', '%', '^', '&', '*', '(', ')', '_', 'is', 'a', 'test'])

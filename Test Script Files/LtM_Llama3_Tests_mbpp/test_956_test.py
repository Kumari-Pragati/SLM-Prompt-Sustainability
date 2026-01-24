import unittest
from mbpp_956_code import split_list

class TestSplitList(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(split_list('HelloWorld'), ['Hello', 'World'])

    def test_empty_input(self):
        self.assertEqual(split_list(''), [])

    def test_single_word(self):
        self.assertEqual(split_list('Hello'), ['Hello'])

    def test_multiple_words(self):
        self.assertEqual(split_list('HelloWorld FooBar'), ['Hello', 'World', 'Foo', 'Bar'])

    def test_punctuation(self):
        self.assertEqual(split_list('Hello,World!'), ['Hello', 'World'])

    def test_numbers(self):
        self.assertEqual(split_list('Hello123World'), ['Hello', '123', 'World'])

    def test_special_chars(self):
        self.assertEqual(split_list('Hello@World'), ['Hello', 'World'])

import unittest
from mbpp_319_code import find_long_word

class TestFindLongWord(unittest.TestCase):

    def test_find_long_word(self):
        self.assertEqual(find_long_word("Hello world"), ['world'])
        self.assertEqual(find_long_word("Hello"), [])
        self.assertEqual(find_long_word("Hello world hello"), ['world'])
        self.assertEqual(find_long_word("Hello world hello world"), ['world', 'world'])
        self.assertEqual(find_long_word("Hello world hello world hello"), ['world', 'world', 'world'])
        self.assertEqual(find_long_word("Hello world hello world hello world"), ['world', 'world', 'world', 'world'])
        self.assertEqual(find_long_word("Hello world hello world hello world hello"), ['world', 'world', 'world', 'world', 'world'])
        self.assertEqual(find_long_word("Hello world hello world hello world hello world"), ['world', 'world', 'world', 'world', 'world', 'world'])
        self.assertEqual(find_long_word("Hello world hello world hello world hello world hello"), ['world', 'world', 'world', 'world', 'world', 'world', 'world'])

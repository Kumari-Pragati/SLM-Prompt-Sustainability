import unittest
from mbpp_678_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_spaces(''), '')

    def test_single_space(self):
        self.assertEqual(remove_spaces(' '), '')

    def test_multiple_spaces(self):
        self.assertEqual(remove_spaces('   '), '')

    def test_single_word(self):
        self.assertEqual(remove_spaces('hello'), 'hello')

    def test_multiple_words(self):
        self.assertEqual(remove_spaces('hello world'), 'helloworld')

    def test_spaces_at_beginning_and_end(self):
        self.assertEqual(remove_spaces(' hello world '), 'helloworld')

    def test_spaces_in_middle(self):
        self.assertEqual(remove_spaces('hello world hello'), 'helloworldhello')

    def test_spaces_before_and_after_words(self):
        self.assertEqual(remove_spaces(' hello   world   '), 'helloworld')

    def test_spaces_before_and_after_words_with_empty_strings(self):
        self.assertEqual(remove_spaces('   hello   world   '), 'helloworld')

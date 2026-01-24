import unittest
from mbpp_678_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(remove_spaces('hello world'), 'helloworld')

    def test_empty_input(self):
        self.assertEqual(remove_spaces(''), '')

    def test_single_space(self):
        self.assertEqual(remove_spaces('hello'), 'hello')

    def test_multiple_spaces(self):
        self.assertEqual(remove_spaces('hello   world'), 'helloworld')

    def test_leading_spaces(self):
        self.assertEqual(remove_spaces('   hello world'), 'helloworld')

    def test_trailing_spaces(self):
        self.assertEqual(remove_spaces('hello world   '), 'helloworld')

    def test_multiple_spaces_between_words(self):
        self.assertEqual(remove_spaces('hello  world  again'), 'helloworldagain')

    def test_spaces_at_beginning_and_end(self):
        self.assertEqual(remove_spaces('   hello   world   '), 'helloworld')

import unittest
from mbpp_676_code import sub

def remove_extra_char(text1):
  pattern = re.compile('[\W_]+')
  return (pattern.sub('', text1))

class TestRemoveExtraChar(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_extra_char(''), '')

    def test_single_word(self):
        self.assertEqual(remove_extra_char('Hello'), 'Hello')

    def test_multiple_words(self):
        self.assertEqual(remove_extra_char('Hello World'), 'HelloWorld')

    def test_special_characters(self):
        self.assertEqual(remove_extra_char('Hello@World!'), 'HelloWorld')

    def test_numbers(self):
        self.assertEqual(remove_extra_char('Hello123World'), 'Hello123World')

    def test_whitespace_only(self):
        self.assertEqual(remove_extra_char('   '), '')

    def test_leading_trailing_whitespace(self):
        self.assertEqual(remove_extra_char(' Hello World   '), 'HelloWorld')

    def test_underscores(self):
        self.assertEqual(remove_extra_char('Hello_World'), 'HelloWorld')

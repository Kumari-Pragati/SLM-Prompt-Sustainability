import unittest
from mbpp_173_code import remove_splchar

class TestRemoveSplchar(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_splchar(''), '')

    def test_single_char(self):
        self.assertEqual(remove_splchar('a'), 'a')
        self.assertEqual(remove_splchar('A'), 'A')
        self.assertEqual(remove_splchar('0'), '0')

    def test_multiple_chars(self):
        self.assertEqual(remove_splchar('Hello, World!'), 'HelloWorld')
        self.assertEqual(remove_splchar('123-456-7890'), '1234567890')
        self.assertEqual(remove_splchar('_Test_'), 'Test')

    def test_special_characters(self):
        self.assertEqual(remove_splchar('!@#$%^&*()_+-=[]{}|;:,.<>?'), '')

    def test_whitespace(self):
        self.assertEqual(remove_splchar('   Hello   World   '), 'HelloWorld')

    def test_mixed_case(self):
        self.assertEqual(remove_splchar('HeLlO wOrLd'), 'HelloWorld')

    def test_unicode(self):
        text = 'Hello, 世界!'
        self.assertEqual(remove_splchar(text), 'Hello, 世界')

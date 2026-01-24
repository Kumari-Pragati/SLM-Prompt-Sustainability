import unittest
from mbpp_83_code import get_Char

class TestGetChar(unittest.TestCase):

    def test_get_Char_with_lowercase_letters(self):
        self.assertEqual(get_Char('abc'), 'd')
        self.assertEqual(get_Char('xyz'), 'z')
        self.assertEqual(get_Char('zzz'), 'a')

    def test_get_Char_with_uppercase_letters(self):
        self.assertEqual(get_Char('ABC'), 'D')
        self.assertEqual(get_Char('XYZ'), 'Z')
        self.assertEqual(get_Char('ZZZ'), 'A')

    def test_get_Char_with_mixed_case_letters(self):
        self.assertEqual(get_Char('AbC'), 'd')
        self.assertEqual(get_Char('XyZ'), 'z')
        self.assertEqual(get_Char('ZzZ'), 'a')

    def test_get_Char_with_special_characters(self):
        self.assertEqual(get_Char('!@#'), '!')
        self.assertEqual(get_Char('$%^'), '$')
        self.assertEqual(get_Char('&*('), '!')

    def test_get_Char_with_numbers(self):
        self.assertEqual(get_Char('123'), 'd')
        self.assertEqual(get_Char('789'), 'z')
        self.assertEqual(get_Char('456'), 'a')

import unittest
from mbpp_83_code import get_Char

class TestGetChar(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(get_Char('abc'), 'c')
        self.assertEqual(get_Char('def'), 'f')
        self.assertEqual(get_Char('ghi'), 'h')
        self.assertEqual(get_Char('jkl'), 'k')
        self.assertEqual(get_Char('mno'), 'o')
        self.assertEqual(get_Char('pqr'), 'r')
        self.assertEqual(get_Char('stu'), 't')
        self.assertEqual(get_Char('vwxyz'), 'z')

    def test_empty_string(self):
        self.assertEqual(get_Char(''), ord('a'))

    def test_single_letter(self):
        self.assertEqual(get_Char('a'), ord('b'))
        self.assertEqual(get_Char('z'), ord('a'))

    def test_multi_digit_input(self):
        self.assertEqual(get_Char('123'), ord('a'))
        self.assertEqual(get_Char('999'), ord('z'))

    def test_special_characters(self):
        self.assertRaises(TypeError, get_Char, '!@#$%^&*()_+-=')
        self.assertRaises(TypeError, get_Char, 'ABC!@#$%^&*()_+-=')

    def test_empty_list(self):
        self.assertRaises(TypeError, get_Char, [])

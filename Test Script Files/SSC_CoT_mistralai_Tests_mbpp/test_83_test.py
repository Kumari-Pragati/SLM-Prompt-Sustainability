import unittest
from mbpp_83_code import get_Char

class TestGetChar(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(get_Char('abcdefghijklmnopqrstuvwxyz'), 'z')
        self.assertEqual(get_Char('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'z')
        self.assertEqual(get_Char('aA1B2cC3dD4eE5fF6gG7hH8iI9jJ0kK11'), chr(ord('a') + 26 - 1))

    def test_edge_cases(self):
        self.assertEqual(get_Char(''), chr(ord('a') - 1))
        self.assertEqual(get_Char('z'), chr(ord('a') + 25))
        self.assertEqual(get_Char('zz'), chr(ord('a') + 52))
        self.assertEqual(get_Char('aZ'), chr(ord('a') + 51))

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, get_Char, '123')
        self.assertRaises(ValueError, get_Char, '!@#$%^&*()')
        self.assertRaises(ValueError, get_Char, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123!@#$%^&*()')

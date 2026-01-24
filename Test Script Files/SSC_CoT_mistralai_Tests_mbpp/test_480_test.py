import unittest
from mbpp_480_code import get_max_occuring_char

class TestGetMaxOccuringChar(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(get_max_occuring_char('aaabbcdd'), 'a')
        self.assertEqual(get_max_occuring_char('Hello World'), 'l')
        self.assertEqual(get_max_occuring_char('12345'), '5')

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(get_max_occuring_char(''), '')
        self.assertEqual(get_max_occuring_char(' '), ' ')
        self.assertEqual(get_max_occuring_char('A'), 'A')
        self.assertEqual(get_max_occuring_char('aabbccaaa'), 'a')
        self.assertEqual(get_max_occuring_char('a' * 1000), 'a')

    def test_special_cases(self):
        self.assertEqual(get_max_occuring_char('!@#$%^&*()_+-=[]{}|;:'\'<>,./?'), '!')
        self.assertEqual(get_max_occuring_char('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'Z')
        self.assertEqual(get_max_occuring_char('abcdefghijklmnopqrstuvwxyz'), 'z')
        self.assertEqual(get_max_occuring_char('0123456789'), '9')

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, get_max_occuring_char, 123)
        self.assertRaises(TypeError, get_max_occuring_char, [1, 2, 3])

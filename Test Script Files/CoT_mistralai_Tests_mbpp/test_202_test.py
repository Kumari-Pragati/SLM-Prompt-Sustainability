import unittest
from mbpp_202_code import remove_even

class TestRemoveEven(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_even(''), '')

    def test_single_character(self):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.assertEqual(remove_even(char), char)

    def test_even_length(self):
        for word in ['aa', 'ee', 'ii', 'oo', 'ww', 'zz']:
            self.assertEqual(remove_even(word), '')

    def test_odd_length(self):
        for word in ['ab', 'cd', 'ef', 'gh', 'ij', 'kl', 'mn', 'op', 'qr', 'st', 'uv', 'wx', 'yz']:
            self.assertEqual(remove_even(word), word[1:])

    def test_long_string(self):
        long_string = 'abcdefghijklmnopqrstuvwxyz' * 10
        self.assertEqual(remove_even(long_string), long_string[1::2])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_even(123)

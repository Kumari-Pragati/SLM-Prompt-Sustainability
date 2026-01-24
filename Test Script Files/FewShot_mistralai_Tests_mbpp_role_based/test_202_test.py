import unittest
from mbpp_202_code import remove_even

class TestRemoveEven(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_even(''), '')

    def test_single_character_string(self):
        for char in ['a', 'b', 'c']:
            self.assertEqual(remove_even(char), char)

    def test_even_length_string(self):
        for even_str in ['aa', 'abba', 'abcdefg']:
            self.assertEqual(remove_even(even_str), '')

    def test_odd_length_string(self):
        for odd_str in ['a', 'ab', 'abc', 'abcd', 'abcde']:
            self.assertEqual(remove_even(odd_str), odd_str)

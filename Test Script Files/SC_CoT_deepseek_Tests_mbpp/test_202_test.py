import unittest
from mbpp_202_code import remove_even

class TestRemoveEven(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_even('1234567890'), '13579')

    def test_empty_string(self):
        self.assertEqual(remove_even(''), '')

    def test_single_character(self):
        self.assertEqual(remove_even('a'), 'a')

    def test_even_length_string(self):
        self.assertEqual(remove_even('abcde'), 'ace')

    def test_all_even_positions(self):
        self.assertEqual(remove_even('abcdefghijklmnopqrstuvwxyz'), 'bdfhjlnprtvxz')

    def test_all_odd_positions(self):
        self.assertEqual(remove_even('abcdefghijklmnopqrstuvwxyz'), 'acegikmoqsuwy')

    def test_special_characters(self):
        self.assertEqual(remove_even('!@#$%^&*()'), '!@#%*')

    def test_numeric_string(self):
        self.assertEqual(remove_even('1234567890'), '13579')

    def test_string_with_spaces(self):
        self.assertEqual(remove_even('Hello World'), 'HloWrd')

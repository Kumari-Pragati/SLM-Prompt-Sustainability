import unittest
from mbpp_202_code import remove_even

class TestRemoveEven(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_even('abcdefg'), 'bdf')

    def test_empty_string(self):
        self.assertEqual(remove_even(''), '')

    def test_single_character(self):
        self.assertEqual(remove_even('a'), '')

    def test_even_length_string(self):
        self.assertEqual(remove_even('abcde'), 'bd')

    def test_string_with_spaces(self):
        self.assertEqual(remove_even('abc def'), 'bd')

    def test_string_with_numbers(self):
        self.assertEqual(remove_even('123456'), '35')

    def test_string_with_special_characters(self):
        self.assertEqual(remove_even('!@#$%^'), '@$')

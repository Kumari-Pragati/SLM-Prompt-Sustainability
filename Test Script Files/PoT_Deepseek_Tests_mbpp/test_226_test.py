import unittest
from mbpp_226_code import odd_values_string

class TestOddValuesString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(odd_values_string('abcdefg'), 'aceg')

    def test_empty_string(self):
        self.assertEqual(odd_values_string(''), '')

    def test_single_character_string(self):
        self.assertEqual(odd_values_string('a'), 'a')

    def test_long_string(self):
        self.assertEqual(odd_values_string('abcdefghijklmnopqrstuvwxyz'), 'acegikmou')

    def test_string_with_special_characters(self):
        self.assertEqual(odd_values_string('abc!def@ghi#jkl$'), 'ac!e@g#')

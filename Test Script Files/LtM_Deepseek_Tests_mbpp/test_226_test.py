import unittest
from mbpp_226_code import odd_values_string

class TestOddValuesString(unittest.TestCase):

    def test_simple_string(self):
        self.assertEqual(odd_values_string('abcde'), 'ace')

    def test_empty_string(self):
        self.assertEqual(odd_values_string(''), '')

    def test_single_character_string(self):
        self.assertEqual(odd_values_string('a'), 'a')

    def test_long_string(self):
        self.assertEqual(odd_values_string('abcdefghijklmnopqrstuvwxyz'), 'acegikmoqsuwy')

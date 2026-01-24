import unittest
from mbpp_226_code import odd_values_string

class TestOddValuesString(unittest.TestCase):

    def test_odd_values_string(self):
        self.assertEqual(odd_values_string('abcde'), 'ace')
        self.assertEqual(odd_values_string('1234567890'), '13579')
        self.assertEqual(odd_values_string('abcdefghijklmnopqrstuvwxyz'), 'acegikmoqsuwy')
        self.assertEqual(odd_values_string(''), '')
        self.assertEqual(odd_values_string('a'), 'a')

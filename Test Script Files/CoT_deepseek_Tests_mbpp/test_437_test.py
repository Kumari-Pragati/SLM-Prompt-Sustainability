import unittest
from mbpp_437_code import remove_odd

class TestRemoveOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_odd('abcdefg'), 'bdf')

    def test_empty_string(self):
        self.assertEqual(remove_odd(''), '')

    def test_single_character(self):
        self.assertEqual(remove_odd('a'), '')

    def test_all_odd_characters(self):
        self.assertEqual(remove_odd('bdf'), '')

    def test_all_even_characters(self):
        self.assertEqual(remove_odd('abcde'), 'abcde')

    def test_mixed_characters(self):
        self.assertEqual(remove_odd('abcde12345'), 'abcde')

    def test_special_characters(self):
        self.assertEqual(remove_odd('!@#$%^&*()'), '!@#$%^&*()')

    def test_numeric_string(self):
        self.assertEqual(remove_odd('1234567890'), '24680')

import unittest
from mbpp_437_code import remove_odd

class TestRemoveOdd(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(remove_odd('abcde'), 'bde')

    def test_empty_input(self):
        self.assertEqual(remove_odd(''), '')

    def test_single_character_input(self):
        self.assertEqual(remove_odd('a'), '')

    def test_even_length_input(self):
        self.assertEqual(remove_odd('abcdef'), 'bdf')

    def test_odd_length_input(self):
        self.assertEqual(remove_odd('abcdefg'), 'bdf')

    def test_special_characters_input(self):
        self.assertEqual(remove_odd('!@#$%^&*'), '^')

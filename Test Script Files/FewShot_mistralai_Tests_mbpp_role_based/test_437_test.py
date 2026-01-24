import unittest
from mbpp_437_code import remove_odd

class TestRemoveOdd(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_odd(''), '')

    def test_single_character_string(self):
        self.assertEqual(remove_odd('a'), 'a')

    def test_even_length_string(self):
        self.assertEqual(remove_odd('abcde'), 'ac')

    def test_odd_length_string(self):
        self.assertEqual(remove_odd('abcd'), 'a')

    def test_long_string(self):
        self.assertEqual(remove_odd('abcdefghijklmnopqrstuvwxyz'), 'ab')

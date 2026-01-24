import unittest
from mbpp_437_code import remove_odd

class TestRemoveOdd(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_odd('abcdefg'), 'bdf')

    def test_empty_string(self):
        self.assertEqual(remove_odd(''), '')

    def test_single_character(self):
        self.assertEqual(remove_odd('a'), '')

    def test_even_length_string(self):
        self.assertEqual(remove_odd('abcdef'), 'bdf')

    def test_odd_length_string(self):
        self.assertEqual(remove_odd('abcdefg'), 'bdf')

    def test_string_with_spaces(self):
        self.assertEqual(remove_odd('abc def ghi'), 'b df')

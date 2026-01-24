import unittest
from mbpp_202_code import remove_even

class TestRemoveEven(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(remove_even('abcde'), 'bd')

    def test_empty_input(self):
        self.assertEqual(remove_even(''), '')

    def test_single_character_input(self):
        self.assertEqual(remove_even('a'), '')

    def test_even_length_input(self):
        self.assertEqual(remove_even('abcdef'), 'bdf')

    def test_all_even_positions(self):
        self.assertEqual(remove_even('123456'), '246')

    def test_all_odd_positions(self):
        self.assertEqual(remove_even('abcdefg'), 'bdf')

    def test_mixed_even_odd_positions(self):
        self.assertEqual(remove_even('1a2b3c4d5e6f'), 'a2b4d6f')

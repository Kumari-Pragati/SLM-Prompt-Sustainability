import unittest
from mbpp_202_code import remove_even

class TestRemoveEven(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_even('1234567890'), '13579')

    def test_empty_string(self):
        self.assertEqual(remove_even(''), '')

    def test_single_character(self):
        self.assertEqual(remove_even('1'), '1')

    def test_all_even_characters(self):
        self.assertEqual(remove_even('24680'), '')

    def test_all_odd_characters(self):
        self.assertEqual(remove_even('13579'), '13579')

    def test_mixed_characters(self):
        self.assertEqual(remove_even('123456'), '135')

    def test_special_characters(self):
        self.assertEqual(remove_even('abcde'), 'b')

    def test_numeric_and_alphabetic_characters(self):
        self.assertEqual(remove_even( '123abc456def7890'), '13ab56df90')

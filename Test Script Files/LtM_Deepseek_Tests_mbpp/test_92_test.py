import unittest
from mbpp_92_code import is_undulating

class TestIsUndulating(unittest.TestCase):
    def test_simple_undulating_numbers(self):
        self.assertTrue(is_undulating('11'))
        self.assertTrue(is_undulating('22'))
        self.assertTrue(is_undulating('33'))
        self.assertTrue(is_undulating('44'))
        self.assertTrue(is_undulating('55'))
        self.assertTrue(is_undulating('66'))
        self.assertTrue(is_undulating('77'))
        self.assertTrue(is_undulating('88'))
        self.assertTrue(is_undulating('99'))

    def test_non_undulating_numbers(self):
        self.assertFalse(is_undulating('12'))
        self.assertFalse(is_undulating('23'))
        self.assertFalse(is_undulating('34'))
        self.assertFalse(is_undulating('45'))
        self.assertFalse(is_undulating('56'))
        self.assertFalse(is_undulating('67'))
        self.assertFalse(is_undulating('78'))
        self.assertFalse(is_undulating('89'))
        self.assertFalse(is_undulating('90'))

    def test_empty_input(self):
        self.assertFalse(is_undulating(''))

    def test_single_digit_input(self):
        self.assertFalse(is_undulating('1'))
        self.assertFalse(is_undulating('2'))
        self.assertFalse(is_undulating('3'))
        self.assertFalse(is_undulating('4'))
        self.assertFalse(is_undulating('5'))
        self.assertFalse(is_undulating('6'))
        self.assertFalse(is_undulating('7'))
        self.assertFalse(is_undulating('8'))
        self.assertFalse(is_undulating('9'))

    def test_multiple_digit_undulating_numbers(self):
        self.assertTrue(is_undulating('1111'))
        self.assertTrue(is_undulating('2222'))
        self.assertTrue(is_undulating('3333'))
        self.assertTrue(is_undulating('4444'))
        self.assertTrue(is_undulating('5555'))
        self.assertTrue(is_undulating('6666'))
        self.assertTrue(is_undulating('7777'))
        self.assertTrue(is_undulating('8888'))
        self.assertTrue(is_undulating('9999'))

    def test_multiple_digit_non_undulating_numbers(self):
        self.assertFalse(is_undulating('1234'))
        self.assertFalse(is_undulating('2345'))
        self.assertFalse(is_undulating('3456'))
        self.assertFalse(is_undulating('4567'))
        self.assertFalse(is_undulating('5678'))
        self.assertFalse(is_undulating('6789'))
        self.assertFalse(is_undulating('7890'))

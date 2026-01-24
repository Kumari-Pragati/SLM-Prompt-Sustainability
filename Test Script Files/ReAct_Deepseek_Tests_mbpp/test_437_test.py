import unittest
from mbpp_437_code import remove_odd

class TestRemoveOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_odd('1234567890'), '24680')

    def test_empty_string(self):
        self.assertEqual(remove_odd(''), '')

    def test_single_character(self):
        self.assertEqual(remove_odd('a'), '')

    def test_all_odd_characters(self):
        self.assertEqual(remove_odd('13579'), '')

    def test_all_even_characters(self):
        self.assertEqual(remove_odd('02468'), '02468')

    def test_mixed_characters(self):
        self.assertEqual(remove_odd('1a3b5c7d9e'), 'abde')

    def test_special_characters(self):
        self.assertEqual(remove_odd('!@#$%^&*()'), '(@%*')

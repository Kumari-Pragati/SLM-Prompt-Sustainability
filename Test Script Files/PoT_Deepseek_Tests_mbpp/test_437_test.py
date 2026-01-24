import unittest
from mbpp_437_code import remove_odd

class TestRemoveOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_odd('abcdefg'), 'bdf')

    def test_empty_string(self):
        self.assertEqual(remove_odd(''), '')

    def test_single_character(self):
        self.assertEqual(remove_odd('a'), '')

    def test_all_same_characters(self):
        self.assertEqual(remove_odd('aaaaa'), 'a')

    def test_odd_length_string(self):
        self.assertEqual(remove_odd('abcdef'), 'bdf')

    def test_edge_case_with_spaces(self):
        self.assertEqual(remove_odd('a b c d e f g'), ' b d f ')

    def test_edge_case_with_numbers(self):
        self.assertEqual(remove_odd('123456789'), '2468')

    def test_edge_case_with_special_characters(self):
        self.assertEqual(remove_odd('!@#$%^&*'), '@$%^')

import unittest
from mbpp_165_code import count_char_position

class TestCountCharPosition(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_char_position('ABC'), 3)
        self.assertEqual(count_char_position('abc'), 3)
        self.assertEqual(count_char_position('AaBbCc'), 6)

    def test_edge_case_empty_string(self):
        self.assertEqual(count_char_position(''), 0)

    def test_edge_case_single_char(self):
        self.assertEqual(count_char_position('A'), 1)
        self.assertEqual(count_char_position('a'), 1)

    def test_edge_case_upper_and_lower(self):
        self.assertEqual(count_char_position('AbC'), 2)
        self.assertEqual(count_char_position('aBc'), 2)

    def test_edge_case_non_alphabetic_characters(self):
        self.assertEqual(count_char_position('123'), 0)
        self.assertEqual(count_char_position('A1B'), 1)
        self.assertEqual(count_char_position('A_B'), 2)

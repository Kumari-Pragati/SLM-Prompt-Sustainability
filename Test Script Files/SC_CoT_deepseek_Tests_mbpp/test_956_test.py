import unittest
from mbpp_956_code import split_list

class TestSplitList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(split_list('A1B2C3D4'), ['A1', 'B2', 'C3', 'D4'])

    def test_single_capital_letter(self):
        self.assertEqual(split_list('A'), ['A'])

    def test_empty_string(self):
        self.assertEqual(split_list(''), [])

    def test_no_capital_letters(self):
        self.assertEqual(split_list('123456'), [])

    def test_capital_letters_with_spaces(self):
        self.assertEqual(split_list('A1 B2 C3 D4'), ['A1', 'B2', 'C3', 'D4'])

    def test_capital_letters_with_special_chars(self):
        self.assertEqual(split_list('A1!B2@C3#D4$'), ['A1', 'B2', 'C3', 'D4'])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            split_list(123456)

import unittest
from mbpp_715_code import str_to_tuple

class TestStrToTuple(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(str_to_tuple('1, 2, 3'), (1, 2, 3))

    def test_edge_case_empty_input(self):
        self.assertEqual(str_to_tuple(''), ())

    def test_edge_case_single_element_input(self):
        self.assertEqual(str_to_tuple('1'), (1,))

    def test_edge_case_single_element_input_with_spaces(self):
        self.assertEqual(str_to_tuple(' 1  '), (1,))

    def test_edge_case_multiple_spaces_between_elements(self):
        self.assertEqual(str_to_tuple('1, 2, 3'), (1, 2, 3))

    def test_edge_case_multiple_spaces_between_elements_with_leading_trailing_spaces(self):
        self.assertEqual(str_to_tuple(' 1, 2, 3  '), (1, 2, 3))

    def test_edge_case_invalid_input_non_numeric_characters(self):
        with self.assertRaises(ValueError):
            str_to_tuple('1, a, 3')

    def test_edge_case_invalid_input_non_numeric_characters_with_leading_trailing_spaces(self):
        with self.assertRaises(ValueError):
            str_to_tuple(' 1, a, 3  ')

    def test_edge_case_invalid_input_non_numeric_characters_with_multiple_spaces(self):
        with self.assertRaises(ValueError):
            str_to_tuple('1, a, 3')

    def test_edge_case_invalid_input_non_numeric_characters_with_multiple_spaces_and_leading_trailing_spaces(self):
        with self.assertRaises(ValueError):
            str_to_tuple(' 1, a, 3  ')

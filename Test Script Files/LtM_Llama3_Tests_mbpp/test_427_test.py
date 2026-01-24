import unittest
from mbpp_427_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(change_date_format('2022-07-25'), '25-07-2022')

    def test_edge_case_empty_input(self):
        self.assertIsNone(change_date_format(''))

    def test_edge_case_invalid_input(self):
        self.assertIsNone(change_date_format('abc'))

    def test_edge_case_invalid_input_with_spaces(self):
        self.assertIsNone(change_date_format('2022-07-25 abc'))

    def test_edge_case_invalid_input_with_punctuation(self):
        self.assertIsNone(change_date_format('2022-07-25!'))

    def test_edge_case_invalid_input_with_special_chars(self):
        self.assertIsNone(change_date_format('2022-07-25@'))

    def test_edge_case_invalid_input_with_newline(self):
        self.assertIsNone(change_date_format('2022-07-25\n'))

    def test_edge_case_invalid_input_with_tab(self):
        self.assertIsNone(change_date_format('2022-07-25\t'))

    def test_edge_case_invalid_input_with_multiple_spaces(self):
        self.assertIsNone(change_date_format('2022-07-25   '))

    def test_edge_case_invalid_input_with_multiple_punctuation(self):
        self.assertIsNone(change_date_format('2022-07-25!!'))

    def test_edge_case_invalid_input_with_multiple_special_chars(self):
        self.assertIsNone(change_date_format('2022-07-25@@'))

    def test_edge_case_invalid_input_with_newline_and_spaces(self):
        self.assertIsNone(change_date_format('2022-07-25\n   '))

    def test_edge_case_invalid_input_with_tab_and_spaces(self):
        self.assertIsNone(change_date_format('2022-07-25\t   '))

    def test_edge_case_invalid_input_with_multiple_newlines(self):
        self.assertIsNone(change_date_format('2022-07-25\n\n\n'))

    def test_edge_case_invalid_input_with_multiple_tabs(self):
        self.assertIsNone(change_date_format('2022-07-25\t\t\t'))

    def test_edge_case_invalid_input_with_multiple_newlines_and_spaces(self):
        self.assertIsNone(change_date_format('2022-07-25\n\n\n   '))

    def test_edge_case_invalid_input_with_multiple_tabs_and_spaces(self):
        self.assertIsNone(change_date_format('2022-07-25\t\t\t   '))

    def test_edge_case_invalid_input_with_multiple_newlines_and_tabs(self):
        self.assertIsNone(change_date_format('2022-07-25\n\n\n\t\t\t'))

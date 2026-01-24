import unittest
from mbpp_226_code import odd_values_string

class TestOddValuesString(unittest.TestCase):

    def test_odd_values_string_typical_case(self):
        self.assertEqual(odd_values_string("abcdefg"), "aceg")

    def test_odd_values_string_empty_string(self):
        self.assertEqual(odd_values_string(""), "")

    def test_odd_values_string_single_character(self):
        self.assertEqual(odd_values_string("a"), "a")

    def test_odd_values_string_long_string(self):
        self.assertEqual(odd_values_string("abcdefghijklmnopqrstuvwxyz"), "acegikmoqsuwy")

    def test_odd_values_string_string_with_spaces(self):
        self.assertEqual(odd_values_string("abc def ghi"), "ac fg")

    def test_odd_values_string_string_with_special_characters(self):
        self.assertEqual(odd_values_string("abc!def@ghi"), "ac!g")

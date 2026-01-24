import unittest
from mbpp_95_code import Find_Min_Length

class TestFindMinLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Find_Min_Length(['abc', 'defgh', 'ijklm']), 3)

    def test_single_element(self):
        self.assertEqual(Find_Min_Length(['abcdefgh']), 8)

    def test_empty_list(self):
        self.assertEqual(Find_Min_Length([]), 0)

    def test_all_empty_strings(self):
        self.assertEqual(Find_Min_Length(['', '']), 0)

    def test_mixed_empty_strings_and_non_empty_strings(self):
        self.assertEqual(Find_Min_Length(['abc', '', 'def']), 3)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            Find_Min_Length(None)

    def test_integer_input(self):
        with self.assertRaises(TypeError):
            Find_Min_Length(123)

    def test_float_input(self):
        with self.assertRaises(TypeError):
            Find_Min_Length(123.45)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            Find_Min_Length('abc')

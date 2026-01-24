import unittest
from mbpp_562_code import Find_Max_Length

class TestFindMaxLength(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(Find_Max_Length(['abc', 'defgh', 'ijklm']), 5)

    def test_single_element(self):
        self.assertEqual(Find_Max_Length(['abc']), 3)

    def test_empty_list(self):
        self.assertEqual(Find_Max_Length([]), 0)

    def test_all_empty_strings(self):
        self.assertEqual(Find_Max_Length(['', '']), 0)

    def test_mixed_empty_and_non_empty_strings(self):
        self.assertEqual(Find_Max_Length(['abc', '', 'def']), 3)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            Find_Max_Length(None)

    def test_integer_input(self):
        with self.assertRaises(TypeError):
            Find_Max_Length(123)

    def test_float_input(self):
        with self.assertRaises(TypeError):
            Find_Max_Length(123.45)

    def test_list_with_non_string_elements(self):
        with self.assertRaises(TypeError):
            Find_Max_Length([1, 'abc', 2])

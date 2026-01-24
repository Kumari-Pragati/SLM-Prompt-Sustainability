import unittest
from mbpp_667_code import Check_Vow

class TestCheckVow(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Check_Vow('hello', 'aeiou'), 2)

    def test_no_vowels(self):
        self.assertEqual(Check_Vow('rhythm', 'aeiou'), 0)

    def test_all_vowels(self):
        self.assertEqual(Check_Vow('aeiou', 'aeiou'), 5)

    def test_empty_string(self):
        self.assertEqual(Check_Vow('', 'aeiou'), 0)

    def test_vowels_not_in_string(self):
        self.assertEqual(Check_Vow('bcdfghjklmnpqrstvwxyz', 'aeiou'), 0)

    def test_vowels_in_string(self):
        self.assertEqual(Check_Vow('aeiou', 'aeiou'), 5)

    def test_case_sensitivity(self):
        self.assertEqual(Check_Vow('AEIOU', 'aeiou'), 0)

    def test_invalid_string_type(self):
        with self.assertRaises(TypeError):
            Check_Vow(12345, 'aeiou')

    def test_invalid_vowels_type(self):
        with self.assertRaises(TypeError):
            Check_Vow('hello', 12345)

import unittest
from mbpp_226_code import odd_values_string

class TestOddValuesString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(odd_values_string(""), "")

    def test_single_character_string(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(odd_values_string(char), "")

    def test_odd_length_string(self):
        self.assertEqual(odd_values_string("abc"), "c")
        self.assertEqual(odd_values_string("abcdef"), "cdef")
        self.assertEqual(odd_values_string("abcdefgh"), "gh")

    def test_even_length_string(self):
        self.assertEqual(odd_values_string("abcd"), "d")
        self.assertEqual(odd_values_string("abcde"), "e")
        self.assertEqual(odd_values_string("abcdefg"), "g")

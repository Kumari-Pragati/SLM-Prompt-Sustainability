import unittest
from mbpp_226_code import odd_values_string

class TestOddValuesString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(odd_values_string(""), "")

    def test_single_character_string(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(odd_values_string(char), "")

    def test_even_length_string(self):
        for i in range(1, 101, 2):
            self.assertEqual(odd_values_string("a" * i), "a" * (i - 1))

    def test_odd_length_string(self):
        for i in range(2, 101, 2):
            self.assertEqual(odd_values_string("a" * i), "a")

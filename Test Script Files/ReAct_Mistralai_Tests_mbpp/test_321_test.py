import unittest
from321_code import find_demlo

class TestFindDemlo(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(find_demlo(""), "")

    def test_single_character_string(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(find_demlo(char), str(1) + char)

    def test_multiple_characters_string(self):
        for string in ("aa", "123", "abcdef", "ABCDEFGHIJKLM"):
            self.assertEqual(find_demlo(string), find_demlo(string[::-1]))

    def test_long_string(self):
        long_string = "x" * 100
        self.assertEqual(find_demlo(long_string), find_demlo(long_string[::-1]))

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            find_demlo(-1)

    def test_zero_input(self):
        with self.assertRaises(ValueError):
            find_demlo(0)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            find_demlo(123)

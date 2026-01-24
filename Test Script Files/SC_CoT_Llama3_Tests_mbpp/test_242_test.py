import unittest
from mbpp_242_code import count_charac

class TestCountCharac(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(count_charac('Hello'), 5)

    def test_empty_string(self):
        self.assertEqual(count_charac(''), 0)

    def test_single_character(self):
        self.assertEqual(count_charac('a'), 1)

    def test_multiple_characters(self):
        self.assertEqual(count_charac('abc'), 3)

    def test_long_string(self):
        self.assertEqual(count_charac('abcdefghijklmnopqrstuvwxyz'), 26)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            count_charac(123)

    def test_mixed_case(self):
        self.assertEqual(count_charac('Abc'), 3)

    def test_spaces(self):
        self.assertEqual(count_charac('   '), 3)

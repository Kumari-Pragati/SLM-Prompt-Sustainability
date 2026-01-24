import unittest
from mbpp_92_code import is_undulating

class TestIsUndulating(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertTrue(is_undulating("abc"))

    def test_empty_input(self):
        self.assertFalse(is_undulating(""))

    def test_single_character_input(self):
        self.assertFalse(is_undulating("a"))

    def test_two_character_input(self):
        self.assertFalse(is_undulating("ab"))

    def test_valid_undulating_input(self):
        self.assertTrue(is_undulating("abcabc"))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_undulating(123)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            is_undulating([1, 2, 3])

    def test_long_undulating_input(self):
        self.assertTrue(is_undulating("abcabcabc"))

    def test_non_undulating_input(self):
        self.assertFalse(is_undulating("abcd"))

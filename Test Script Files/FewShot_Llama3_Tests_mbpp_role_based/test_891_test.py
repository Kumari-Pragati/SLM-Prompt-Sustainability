import unittest
from mbpp_891_code import same_Length

class TestSame_Length(unittest.TestCase):
    def test_same_length_positive_numbers(self):
        self.assertTrue(same_Length(123, 456))

    def test_same_length_zero(self):
        self.assertTrue(same_Length(0, 0))

    def test_same_length_negative_numbers(self):
        self.assertTrue(same_Length(-123, -456))

    def test_same_length_mixed_signs(self):
        self.assertTrue(same_Length(-123, 456))

    def test_same_length_non_integer(self):
        with self.assertRaises(TypeError):
            same_Length(123.45, 456)

    def test_same_length_empty_strings(self):
        self.assertFalse(same_Length("", "abc"))

    def test_same_length_non_string(self):
        with self.assertRaises(TypeError):
            same_Length(123, "abc")

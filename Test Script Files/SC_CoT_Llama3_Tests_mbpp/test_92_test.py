import unittest
from mbpp_92_code import is_undulating

class TestIsUndulating(unittest.TestCase):
    def test_typical_input(self):
        self.assertTrue(is_undulating("123456"))

    def test_edge_case_short(self):
        self.assertFalse(is_undulating("12"))

    def test_edge_case_long(self):
        self.assertTrue(is_undulating("123456789"))

    def test_edge_case_single_digit(self):
        self.assertFalse(is_undulating("1"))

    def test_edge_case_two_digits(self):
        self.assertFalse(is_undulating("12"))

    def test_edge_case_three_digits(self):
        self.assertTrue(is_undulating("123"))

    def test_edge_case_four_digits(self):
        self.assertFalse(is_undulating("1234"))

    def test_edge_case_five_digits(self):
        self.assertTrue(is_undulating("12345"))

    def test_edge_case_six_digits(self):
        self.assertFalse(is_undulating("123456"))

    def test_edge_case_seven_digits(self):
        self.assertTrue(is_undulating("1234567"))

    def test_edge_case_eight_digits(self):
        self.assertFalse(is_undulating("12345678"))

    def test_edge_case_nine_digits(self):
        self.assertTrue(is_undulating("123456789"))

    def test_edge_case_ten_digits(self):
        self.assertFalse(is_undulating("1234567890"))

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            is_undulating(123)

    def test_invalid_input_empty_string(self):
        with self.assertRaises(TypeError):
            is_undulating("")

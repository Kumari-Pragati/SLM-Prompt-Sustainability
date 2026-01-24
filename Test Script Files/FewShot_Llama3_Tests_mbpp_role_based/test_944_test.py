import unittest
from mbpp_944_code import num_position

class TestNumPosition(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(num_position("Hello 123 world"), 6)

    def test_multiple_numbers(self):
        self.assertEqual(num_position("Hello 123 456 world"), 6)

    def test_single_digit_number(self):
        self.assertEqual(num_position("Hello 1 world"), 6)

    def test_no_numbers(self):
        self.assertIsNone(num_position("Hello world"))

    def test_empty_string(self):
        self.assertIsNone(num_position(""))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            num_position(123)

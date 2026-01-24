import unittest
from mbpp_350_code import minimum_Length

class TestMinimumLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(minimum_Length('aabbbcc'), 2)

    def test_single_character(self):
        self.assertEqual(minimum_Length('a'), 1)

    def test_same_characters(self):
        self.assertEqual(minimum_Length('aaaaa'), 5)

    def test_empty_string(self):
        self.assertEqual(minimum_Length(''), 0)

    def test_edge_case_with_multiple_max_occurences(self):
        self.assertEqual(minimum_Length('aabbcc'), 3)

    def test_edge_case_with_all_characters_same_frequency(self):
        self.assertEqual(minimum_Length('abc'), 1)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            minimum_Length(123)

    def test_invalid_input_with_special_characters(self):
        with self.assertRaises(ValueError):
            minimum_Length('a$b')

import unittest
from mbpp_647_code import split_upperstring

class TestSplitUpperstring(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(split_upperstring(""), [])

    def test_single_word(self):
        self.assertEqual(split_upperstring("Hello"), ["Hello"])

    def test_multiple_words(self):
        self.assertEqual(split_upperstring("Hello World"), ["Hello", "World"])

    def test_punctuation(self):
        self.assertEqual(split_upperstring("Hello, World!"), ["Hello", "World"])

    def test_numbers(self):
        self.assertEqual(split_upperstring("Hello123World"), ["Hello", "123", "World"])

    def test_non_ascii(self):
        self.assertEqual(split_upperstring("Hëllo"), ["Hëllo"])

    def test_edge_case(self):
        self.assertEqual(split_upperstring("HelloWorld"), ["Hello", "World"])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            split_upperstring(123)

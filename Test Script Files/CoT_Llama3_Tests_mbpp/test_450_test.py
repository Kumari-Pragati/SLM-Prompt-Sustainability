import unittest
from mbpp_450_code import extract_string

class TestExtractString(unittest.TestCase):
    def test_extract_string_typical(self):
        self.assertEqual(extract_string("hello world", 2), ['he', 'll', 'o ', 'wo', 'rl', 'rd'])

    def test_extract_string_edge(self):
        self.assertEqual(extract_string("hello world", 5), ['world'])

    def test_extract_string_empty_string(self):
        self.assertEqual(extract_string("", 2), [])

    def test_extract_string_single_char(self):
        self.assertEqual(extract_string("a", 1), ['a'])

    def test_extract_string_non_integer_length(self):
        with self.assertRaises(TypeError):
            extract_string("hello world", 'a')

    def test_extract_string_negative_length(self):
        with self.assertRaises(TypeError):
            extract_string("hello world", -1)

    def test_extract_string_empty_string_and_zero_length(self):
        self.assertEqual(extract_string("", 0), [])

    def test_extract_string_empty_string_and_non_integer_length(self):
        with self.assertRaises(TypeError):
            extract_string("", 'a')

    def test_extract_string_empty_string_and_negative_length(self):
        with self.assertRaises(TypeError):
            extract_string("", -1)

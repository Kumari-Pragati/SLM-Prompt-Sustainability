import unittest
from mbpp_220_code import replace_max_specialchar

class TestReplaceMaxSpecialchar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace_max_specialchar("Hello, world! 123", 2), "Hello:, world!: 123")

    def test_edge_case_no_special_chars(self):
        self.assertEqual(replace_max_specialchar("Hello world", 2), "Hello world")

    def test_edge_case_no_replacements(self):
        self.assertEqual(replace_max_specialchar("Hello, world! 123", 0), "Hello, world! 123")

    def test_edge_case_max_replacements(self):
        self.assertEqual(replace_max_specialchar("Hello, world! 123", 5), "Hello:, world!: 123")

    def test_edge_case_negative_replacement_count(self):
        with self.assertRaises(ValueError):
            replace_max_specialchar("Hello, world! 123", -1)

    def test_edge_case_non_integer_replacement_count(self):
        with self.assertRaises(TypeError):
            replace_max_specialchar("Hello, world! 123", "a")

import unittest
from mbpp_220_code import replace_max_specialchar

class TestReplaceMaxSpecialchar(unittest.TestCase):
    def test_typical_use_case(self):
        text = "Hello, World! This is a test."
        n = 2
        expected_output = "Hello:World!: This :is :a :test."
        self.assertEqual(replace_max_specialchar(text, n), expected_output)

    def test_edge_case_empty_string(self):
        text = ""
        n = 1
        expected_output = ""
        self.assertEqual(replace_max_specialchar(text, n), expected_output)

    def test_edge_case_single_character_string(self):
        text = "a"
        n = 1
        expected_output = "a"
        self.assertEqual(replace_max_specialchar(text, n), expected_output)

    def test_edge_case_zero_replacement(self):
        text = "Hello, World! This is a test."
        n = 0
        expected_output = "Hello, World! This is a test."
        self.assertEqual(replace_max_specialchar(text, n), expected_output)

    def test_edge_case_negative_replacement(self):
        text = "Hello, World! This is a test."
        n = -1
        expected_output = "Hello, World! This is a test."
        self.assertEqual(replace_max_specialchar(text, n), expected_output)

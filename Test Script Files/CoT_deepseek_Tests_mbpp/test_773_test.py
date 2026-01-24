import unittest
from mbpp_773_code import occurance_substring

class TestOccuranceSubstring(unittest.TestCase):

    def test_typical_case(self):
        text = "Hello, world!"
        pattern = "world"
        self.assertEqual(occurance_substring(text, pattern), ('world', 7, 12))

    def test_edge_case_no_match(self):
        text = "Hello, world!"
        pattern = "universe"
        self.assertIsNone(occurance_substring(text, pattern))

    def test_edge_case_empty_text(self):
        text = ""
        pattern = "world"
        self.assertIsNone(occurance_substring(text, pattern))

    def test_edge_case_empty_pattern(self):
        text = "Hello, world!"
        pattern = ""
        self.assertIsNone(occurance_substring(text, pattern))

    def test_invalid_input_type(self):
        text = 12345
        pattern = "world"
        with self.assertRaises(TypeError):
            occurance_substring(text, pattern)

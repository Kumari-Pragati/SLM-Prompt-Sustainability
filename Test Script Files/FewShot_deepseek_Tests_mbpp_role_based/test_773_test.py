import unittest
from mbpp_773_code import occurance_substring

class TestOccuranceSubstring(unittest.TestCase):
    def test_typical_use_case(self):
        text = "Hello, world!"
        pattern = "world"
        self.assertEqual(occurance_substring(text, pattern), ('world', 7, 12))

    def test_edge_condition(self):
        text = "Hello, world!"
        pattern = ""
        self.assertEqual(occurance_substring(text, pattern), (None, None, None))

    def test_boundary_condition(self):
        text = "Hello, world!"
        pattern = "H"
        self.assertEqual(occurance_substring(text, pattern), ('H', 0, 1))

    def test_invalid_input(self):
        text = 12345
        pattern = "world"
        with self.assertRaises(TypeError):
            occurance_substring(text, pattern)

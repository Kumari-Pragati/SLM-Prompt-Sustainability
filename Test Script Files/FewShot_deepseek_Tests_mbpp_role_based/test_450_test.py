import unittest
from mbpp_450_code import extract_string

class TestExtractString(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(extract_string(['abc', 'def', 'ghi'], 3), ['abc', 'def', 'ghi'])

    def test_edge_condition(self):
        self.assertEqual(extract_string(['a', 'bc', 'defg'], 1), ['a', 'b', 'c'])

    def test_boundary_condition(self):
        self.assertEqual(extract_string(['abcd', 'ef', 'gh'], 2), ['abcd', 'ef'])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            extract_string('abc', 3)

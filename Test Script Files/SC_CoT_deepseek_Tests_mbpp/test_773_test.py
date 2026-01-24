import unittest
from mbpp_773_code import occurance_substring

class TestOccuranceSubstring(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(occurance_substring('Hello, world!', 'world'), ('world', 7, 12))

    def test_edge_case(self):
        self.assertEqual(occurance_substring('Hello, world!', ''), ('', 0, 0))

    def test_corner_case(self):
        self.assertEqual(occurance_substring('Hello, world!', 'Hello, world!'), ('Hello, world!', 0, 13))

    def test_no_match(self):
        self.assertIsNone(occurance_substring('Hello, world!', 'nonexistent'))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            occurance_substring(123, 'world')
        with self.assertRaises(TypeError):
            occurance_substring('Hello, world!', 123)

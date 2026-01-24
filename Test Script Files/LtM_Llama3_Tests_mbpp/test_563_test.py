import unittest
from mbpp_563_code import extract_values

class TestExtractValues(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(extract_values('"hello"'), ['"hello"'])

    def test_multiple(self):
        self.assertEqual(extract_values('"hello" "world"'), ['"hello"', '"world"'])

    def test_empty_input(self):
        self.assertEqual(extract_values(""), [])

    def test_no_matches(self):
        self.assertEqual(extract_values('This is a test'), [])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            extract_values(123)

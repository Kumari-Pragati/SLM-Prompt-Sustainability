import unittest
from mbpp_563_code import extract_values

class TestExtractValues(unittest.TestCase):
    def test_typical_use_case(self):
        text = 'This is a "test" string with "multiple" "values"'
        self.assertEqual(extract_values(text), ['test', 'multiple', 'values'])

    def test_edge_condition(self):
        text = 'No quotes in this string'
        self.assertEqual(extract_values(text), [])

    def test_boundary_condition(self):
        text = '""'
        self.assertEqual(extract_values(text), [''])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            extract_values(123)

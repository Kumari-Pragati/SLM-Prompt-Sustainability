import unittest
from mbpp_563_code import extract_values

class TestExtractValues(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(extract_values('"hello"'), ['hello'])

    def test_multiple_values(self):
        self.assertEqual(extract_values('"hello", "world"'), ['hello', 'world'])

    def test_empty_input(self):
        self.assertEqual(extract_values(''), [])

    def test_no_values(self):
        self.assertEqual(extract_values('no quotes here'), [])

    def test_special_characters(self):
        self.assertEqual(extract_values('"h@ll0", "w0rld"'), ['h@ll0', 'w0rld'])

    def test_numbers_in_quotes(self):
        self.assertEqual(extract_values('"123", "456"'), ['123', '456'])

    def test_mixed_types(self):
        self.assertEqual(extract_values('"hello", "123", "world"'), ['hello', '123', 'world'])

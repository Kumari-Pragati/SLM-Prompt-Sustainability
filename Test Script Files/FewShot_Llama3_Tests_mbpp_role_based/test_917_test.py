import unittest
from mbpp_917_code import text_uppercase_lowercase

class TestText_Uppercase_Lowercase(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(text_uppercase_lowercase('HelloWorld'), 'Found a match!')

    def test_edge_case_uppercase(self):
        self.assertEqual(text_uppercase_lowercase('WORLD'), 'Found a match!')

    def test_edge_case_lowercase(self):
        self.assertEqual(text_uppercase_lowercase('world'), 'Found a match!')

    def test_edge_case_mixed_case(self):
        self.assertEqual(text_uppercase_lowercase('HelloWorld'), 'Found a match!')

    def test_edge_case_no_match(self):
        self.assertEqual(text_uppercase_lowercase('hello'), 'Not matched!')

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            text_uppercase_lowercase(123)

import unittest
from mbpp_917_code import text_uppercase_lowercase

class TestText_Uppercase_Lowercase(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(text_uppercase_lowercase('HelloWorld'), 'Found a match!')

    def test_edge_case_uppercase(self):
        self.assertEqual(text_uppercase_lowercase('HELLO'), 'Not matched!')

    def test_edge_case_lowercase(self):
        self.assertEqual(text_uppercase_lowercase('world'), 'Not matched!')

    def test_edge_case_mixed_case(self):
        self.assertEqual(text_uppercase_lowercase('HelloWorld123'), 'Not matched!')

    def test_edge_case_empty_input(self):
        self.assertEqual(text_uppercase_lowercase(''), 'Not matched!')

    def test_edge_case_non_string_input(self):
        with self.assertRaises(TypeError):
            text_uppercase_lowercase(123)

    def test_edge_case_non_string_input2(self):
        with self.assertRaises(TypeError):
            text_uppercase_lowercase(None)

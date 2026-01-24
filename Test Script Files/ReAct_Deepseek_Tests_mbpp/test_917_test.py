import unittest
from mbpp_917_code import text_uppercase_lowercase

class TestTextUppercaseLowercase(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_uppercase_lowercase('AbC'), 'Found a match!')

    def test_edge_case_all_lowercase(self):
        self.assertEqual(text_uppercase_lowercase('abc'), 'Not matched!')

    def test_edge_case_all_uppercase(self):
        self.assertEqual(text_uppercase_lowercase('ABC'), 'Not matched!')

    def test_edge_case_no_uppercase_no_lowercase(self):
        self.assertEqual(text_uppercase_lowercase('123'), 'Not matched!')

    def test_edge_case_empty_string(self):
        self.assertEqual(text_uppercase_lowercase(''), 'Not matched!')

    def test_explicitly_handled_error_case(self):
        with self.assertRaises(TypeError):
            text_uppercase_lowercase(123)

import unittest
from mbpp_917_code import text_uppercase_lowercase

class TestTextUpperLowercase(unittest.TestCase):
    def test_match(self):
        self.assertEqual(text_uppercase_lowercase('HelloWorld'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_uppercase_lowercase('hello'), 'Not matched!')

    def test_edge_case(self):
        self.assertEqual(text_uppercase_lowercase('HELLO'), 'Not matched!')

    def test_edge_case2(self):
        self.assertEqual(text_uppercase_lowercase('helloWorld'), 'Not matched!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_uppercase_lowercase(123)

    def test_empty_input(self):
        self.assertEqual(text_uppercase_lowercase(''), 'Not matched!')

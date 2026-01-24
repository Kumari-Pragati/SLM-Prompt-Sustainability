import unittest
from mbpp_917_code import text_uppercase_lowercase

class TestText_Uppercase_Lowercase(unittest.TestCase):

    def test_found_match(self):
        self.assertEqual(text_uppercase_lowercase('HelloWorld'), 'Found a match!')

    def test_not_found_match(self):
        self.assertEqual(text_uppercase_lowercase('Hello'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_uppercase_lowercase(''), 'Not matched!')

    def test_no_match(self):
        self.assertEqual(text_uppercase_lowercase('Hello123'), 'Not matched!')

    def test_multiple_matches(self):
        self.assertEqual(text_uppercase_lowercase('HelloWorld123'), 'Found a match!')

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            text_uppercase_lowercase(123)

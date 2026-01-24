import unittest
from mbpp_917_code import text_uppercase_lowercase

class TestTextUpperLowercase(unittest.TestCase):
    def test_match_found(self):
        self.assertEqual(text_uppercase_lowercase('HelloWorld'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_uppercase_lowercase('hello'), 'Not matched!')

    def test_match_at_start(self):
        self.assertEqual(text_uppercase_lowercase('HELLOworld'), 'Found a match!')

    def test_match_at_end(self):
        self.assertEqual(text_uppercase_lowercase('worldHELLO'), 'Found a match!')

    def test_match_at_middle(self):
        self.assertEqual(text_uppercase_lowercase('HelloWORLD'), 'Found a match!')

    def test_no_match_at_start(self):
        self.assertEqual(text_uppercase_lowercase('hello'), 'Not matched!')

    def test_no_match_at_end(self):
        self.assertEqual(text_uppercase_lowercase('world'), 'Not matched!')

    def test_no_match_at_middle(self):
        self.assertEqual(text_uppercase_lowercase('helloworld'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_uppercase_lowercase(''), 'Not matched!')

    def test_single_char(self):
        self.assertEqual(text_uppercase_lowercase('A'), 'Not matched!')

    def test_single_char_lowercase(self):
        self.assertEqual(text_uppercase_lowercase('a'), 'Not matched!')

    def test_single_char_uppercase(self):
        self.assertEqual(text_uppercase_lowercase('Z'), 'Not matched!')

    def test_single_char_mixed(self):
        self.assertEqual(text_uppercase_lowercase('aZ'), 'Not matched!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_uppercase_lowercase(123)

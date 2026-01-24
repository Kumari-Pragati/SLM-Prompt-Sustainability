import unittest
from mbpp_917_code import text_uppercase_lowercase

class TestTextUppercaseLowercase(unittest.TestCase):

    def test_uppercase_and_lowercase(self):
        self.assertEqual(text_uppercase_lowercase('Hello World'), 'Found a match!')
        self.assertEqual(text_uppercase_lowercase('HELLO WORLD'), 'Found a match!')
        self.assertEqual(text_uppercase_lowercase('Hello123World'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('123HelloWorld'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('Hello'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('World'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_uppercase_lowercase(''), 'Not matched!')

    def test_single_case(self):
        self.assertEqual(text_uppercase_lowercase('A'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('a'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('Z'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('z'), 'Not matched!')

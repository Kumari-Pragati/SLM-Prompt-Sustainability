import unittest
from mbpp_917_code import text_uppercase_lowercase

class TestTextUppercaseLowercase(unittest.TestCase):
    def test_found_match(self):
        self.assertEqual(text_uppercase_lowercase('HelloWorld'), 'Found a match!')
        self.assertEqual(text_uppercase_lowercase('HeLLOwOrLd'), 'Found a match!')
        self.assertEqual(text_uppercase_lowercase('HELLOWORLD'), 'Found a match!')
        self.assertEqual(text_uppercase_lowercase('HeLLOwOrLd123'), 'Found a match!')

    def test_not_matched(self):
        self.assertEqual(text_uppercase_lowercase('helloWorld'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('123'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('_'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('Hello'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('World'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_uppercase_lowercase(''), 'Not matched!')

    def test_single_case(self):
        self.assertEqual(text_uppercase_lowercase('A'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('a'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('1'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('_'), 'Not matched!')

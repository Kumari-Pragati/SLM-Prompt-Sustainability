import unittest
from mbpp_917_code import text_uppercase_lowercase

class TestTextUppercaseLowercase(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(text_uppercase_lowercase('HelloWorld'), 'Found a match!')
        self.assertEqual(text_uppercase_lowercase('HeLlOwOrLd'), 'Found a match!')

    def test_edge_case(self):
        self.assertEqual(text_uppercase_lowercase(''), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase(' '), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('A'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('a'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('Aa'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('AaB'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('AaBc'), 'Not matched!')

    def test_special_case(self):
        self.assertEqual(text_uppercase_lowercase('HeLlOwOrLd123'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('HeLlOwOrLd_'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('HeLlOwOrLd!'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('HeLlOwOrLd@'), 'Not matched!')
        self.assertEqual(text_uppercase_lowercase('HeLlOwOrLd#'), 'Not matched!')

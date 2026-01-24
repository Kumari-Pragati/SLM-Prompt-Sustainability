import unittest
from mbpp_917_code import text_uppercase_lowercase

class TestTextUppercaseLowercase(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(text_uppercase_lowercase("HelloWorld"), "Found a match!")
        self.assertEqual(text_uppercase_lowercase("HeLLOwOrLd"), "Found a match!")
        self.assertEqual(text_uppercase_lowercase("HELLOWORLD"), "Found a match!")

    def test_edge_case(self):
        self.assertEqual(text_uppercase_lowercase("HeLLO"), "Not matched!")
        self.assertEqual(text_uppercase_lowercase("HELLO "), "Not matched!")
        self.assertEqual(text_uppercase_lowercase("HELLOWorld!"), "Not matched!")
        self.assertEqual(text_uppercase_lowercase("HELLOWorld123"), "Not matched!")

    def test_corner_case(self):
        self.assertEqual(text_uppercase_lowercase(""), "Not matched!")
        self.assertEqual(text_uppercase_lowercase("A"), "Not matched!")
        self.assertEqual(text_uppercase_lowercase("a"), "Not matched!")
        self.assertEqual(text_uppercase_lowercase("Aa"), "Not matched!")
        self.assertEqual(text_uppercase_lowercase("AaB"), "Not matched!")
        self.assertEqual(text_uppercase_lowercase("AaBc"), "Not matched!")

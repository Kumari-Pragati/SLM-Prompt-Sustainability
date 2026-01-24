import unittest
from mbpp_917_code import text_uppercase_lowercase

class TestTextUpperLowercase(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_uppercase_lowercase("HelloWorld"), 'Found a match!')

    def test_edge_case_uppercase(self):
        self.assertEqual(text_uppercase_lowercase("HELLOworld"), 'Found a match!')

    def test_edge_case_lowercase(self):
        self.assertEqual(text_uppercase_lowercase("helloWORLD"), 'Found a match!')

    def test_edge_case_mixed(self):
        self.assertEqual(text_uppercase_lowercase("HeLlOwOrLd"), 'Found a match!')

    def test_edge_case_no_match(self):
        self.assertEqual(text_uppercase_lowercase("Hello"), 'Not matched!')

    def test_edge_case_no_match2(self):
        self.assertEqual(text_uppercase_lowercase("world"), 'Not matched!')

    def test_edge_case_no_match3(self):
        self.assertEqual(text_uppercase_lowercase("HelloWorld123"), 'Not matched!')

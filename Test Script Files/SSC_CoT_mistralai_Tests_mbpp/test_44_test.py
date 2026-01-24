import unittest
from mbpp_44_code import text_match_string

class TestTextMatchString(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(text_match_string('HelloWorld'), 'Found a match!')

    def test_edge_cases(self):
        self.assertEqual(text_match_string('_HelloWorld'), 'Found a match!')
        self.assertEqual(text_match_string('HelloWorld_'), 'Found a match!')
        self.assertEqual(text_match_string('HelloWorld123'), 'Found a match!')
        self.assertEqual(text_match_string('123HelloWorld'), 'Not matched!')
        self.assertEqual(text_match_string('HelloWorld1234'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_match_string(''), 'Not matched!')

    def test_special_characters(self):
        self.assertEqual(text_match_string('HelloWorld@'), 'Not matched!')
        self.assertEqual(text_match_string('HelloWorld#'), 'Not matched!')
        self.assertEqual(text_match_string('HelloWorld$'), 'Not matched!')
        self.assertEqual(text_match_string('HelloWorld%'), 'Not matched!')
        self.assertEqual(text_match_string('HelloWorld!'), 'Not matched!')
        self.assertEqual(text_match_string('HelloWorld_'), 'Found a match!')

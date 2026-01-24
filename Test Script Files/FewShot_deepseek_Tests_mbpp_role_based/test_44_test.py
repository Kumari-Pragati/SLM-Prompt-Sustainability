import unittest
from mbpp_44_code import text_match_string

class TestTextMatchString(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(text_match_string('HelloWorld'), 'Found a match!')

    def test_edge_condition(self):
        self.assertEqual(text_match_string(''), 'Not matched!')

    def test_boundary_condition(self):
        self.assertEqual(text_match_string('123456'), 'Found a match!')

    def test_invalid_input(self):
        self.assertEqual(text_match_string(123456), 'Not matched!')

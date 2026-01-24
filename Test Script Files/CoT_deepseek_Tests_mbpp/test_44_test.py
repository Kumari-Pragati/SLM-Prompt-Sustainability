import unittest
from mbpp_44_code import text_match_string

class TestTextMatchString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match_string('HelloWorld'), 'Found a match!')

    def test_edge_case(self):
        self.assertEqual(text_match_string(''), 'Not matched!')

    def test_boundary_case(self):
        self.assertEqual(text_match_string('123456'), 'Found a match!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_match_string(123456)

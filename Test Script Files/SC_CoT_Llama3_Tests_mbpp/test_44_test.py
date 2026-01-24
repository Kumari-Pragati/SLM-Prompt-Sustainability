import unittest
from mbpp_44_code import text_match_string

class TestTextMatchString(unittest.TestCase):
    def test_match_string(self):
        self.assertEqual(text_match_string('Hello'), 'Found a match!')

    def test_no_match_string(self):
        self.assertEqual(text_match_string('123'), 'Not matched!')

    def test_match_string_edge_case(self):
        self.assertEqual(text_match_string(''), 'Not matched!')

    def test_match_string_edge_case2(self):
        self.assertEqual(text_match_string('abc'), 'Found a match!')

    def test_match_string_edge_case3(self):
        self.assertEqual(text_match_string('   '), 'Not matched!')

    def test_match_string_edge_case4(self):
        self.assertEqual(text_match_string('  abc  '), 'Found a match!')

    def test_match_string_edge_case5(self):
        self.assertEqual(text_match_string('   abc   '), 'Found a match!')

    def test_match_string_edge_case6(self):
        self.assertEqual(text_match_string('   abc  '+' '* 100), 'Found a match!')

    def test_match_string_invalid_input(self):
        with self.assertRaises(TypeError):
            text_match_string(None)

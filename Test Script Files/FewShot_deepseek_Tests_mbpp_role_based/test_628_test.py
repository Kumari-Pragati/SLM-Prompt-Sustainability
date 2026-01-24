import unittest
from mbpp_628_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(replace_spaces("Hello World"), "Hello%20World")

    def test_edge_case_with_no_spaces(self):
        self.assertEqual(replace_spaces("HelloWorld"), "HelloWorld")

    def test_boundary_case_with_max_length(self):
        long_string = 'a' * 1000
        self.assertEqual(replace_spaces(long_string), long_string.replace(' ', '%20'))

    def test_boundary_case_exceeding_max_length(self):
        long_string = 'a' * 1001
        self.assertEqual(replace_spaces(long_string), -1)

    def test_invalid_input_type(self):
        self.assertEqual(replace_spaces(12345), -1)

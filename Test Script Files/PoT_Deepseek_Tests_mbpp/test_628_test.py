import unittest
from mbpp_628_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace_spaces("Hello World"), "Hello%20World")

    def test_edge_case_with_no_spaces(self):
        self.assertEqual(replace_spaces("NoSpacesHere"), "NoSpacesHere")

    def test_boundary_case_with_single_space(self):
        self.assertEqual(replace_spaces(" "), "%20")

    def test_boundary_case_with_multiple_spaces(self):
        self.assertEqual(replace_spaces("Multiple   Spaces"), "Multiple%20%20%20%20%20Spaces")

    def test_corner_case_with_empty_string(self):
        self.assertEqual(replace_spaces(""), "")

    def test_corner_case_with_max_length_string(self):
        long_string = "a" * 1000
        self.assertEqual(replace_spaces(long_string), long_string)

    def test_corner_case_with_more_than_max_length_string(self):
        long_string = "a" * 1001
        self.assertEqual(replace_spaces(long_string), -1)

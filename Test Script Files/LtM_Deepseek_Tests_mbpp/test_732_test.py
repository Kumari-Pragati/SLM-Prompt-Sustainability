import unittest
from mbpp_732_code import replace_specialchar

class TestReplaceSpecialChar(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(replace_specialchar("hello world"), "hello:world")

    def test_edge_condition_empty_string(self):
        self.assertEqual(replace_specialchar(""), "")

    def test_edge_condition_string_with_only_special_chars(self):
        self.assertEqual(replace_specialchar(" ,."), ":")

    def test_complex_input(self):
        self.assertEqual(replace_specialchar("hello, world. how are you?"), "hello:world:how are you:")

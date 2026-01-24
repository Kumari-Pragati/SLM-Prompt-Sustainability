import unittest
from mbpp_813_code import string_length

class TestStringLength(unittest.TestCase):

    def test_simple_string(self):
        self.assertEqual(string_length("hello"), 5)

    def test_empty_string(self):
        self.assertEqual(string_length(""), 0)

    def test_single_character_string(self):
        self.assertEqual(string_length("a"), 1)

    def test_long_string(self):
        self.assertEqual(string_length("abcdefghijklmnopqrstuvwxyz"), 26)

    def test_multi_line_string(self):
        multi_line_string = """\
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Aliquam at sapien id nibh viverra laoreet.
In hac habitasse platea dictumst.
"""
        self.assertEqual(string_length(multi_line_string), 124)

    def test_special_characters(self):
        self.assertEqual(string_length("!@#$%^&*()_+-=[]{}|;:'\",.<>?/"), 32)

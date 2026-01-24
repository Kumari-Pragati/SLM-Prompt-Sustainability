import unittest
from mbpp_732_code import replace_specialchar

class TestReplaceSpecialChar(unittest.TestCase):

    def test_replace_specialchar_typical_case(self):
        self.assertEqual(replace_specialchar("hello,world"), "hello:world")

    def test_replace_specialchar_edge_case(self):
        self.assertEqual(replace_specialchar(""), "")

    def test_replace_specialchar_multiple_special_chars(self):
        self.assertEqual(replace_specialchar("hello...world"), "hello:world")

    def test_replace_specialchar_no_special_chars(self):
        self.assertEqual(replace_specialchar("helloworld"), "helloworld")

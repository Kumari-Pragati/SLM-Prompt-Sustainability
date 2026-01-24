import unittest
from mbpp_118_code import string_to_list

class TestStringToList(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(string_to_list("Hello World"), ['Hello', 'World'])

    def test_empty_string(self):
        self.assertEqual(string_to_list(""), [])

    def test_single_word(self):
        self.assertEqual(string_to_list("Python"), ['Python'])

    def test_multiple_spaces(self):
        self.assertEqual(string_to_list("Hello   World"), ['Hello', 'World'])

    def test_no_spaces(self):
        self.assertEqual(string_to_list("HelloWorld"), ['HelloWorld'])

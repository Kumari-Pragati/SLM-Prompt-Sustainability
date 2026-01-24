import unittest
from mbpp_118_code import string_to_list

class TestStringToList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(string_to_list("Hello World"), ['Hello', 'World'])

    def test_empty_string(self):
        self.assertEqual(string_to_list(""), [])

    def test_single_word(self):
        self.assertEqual(string_to_list("Python"), ['Python'])

    def test_multiple_spaces(self):
        self.assertEqual(string_to_list("Hello   World"), ['Hello', 'World'])

    def test_trailing_spaces(self):
        self.assertEqual(string_to_list("Hello World "), ['Hello', 'World'])

    def test_leading_spaces(self):
        self.assertEqual(string_to_list(" Hello World"), ['Hello', 'World'])

    def test_special_characters(self):
        self.assertEqual(string_to_list("Hello,World"), ['Hello,World'])

    def test_numbers_in_string(self):
        self.assertEqual(string_to_list("Hello123World456"), ['Hello123World456'])

import unittest
from mbpp_727_code import remove_char

class TestRemoveChar(unittest.TestCase):

    def test_simple_string(self):
        self.assertEqual(remove_char("Hello World"), "HelloWorld")

    def test_empty_string(self):
        self.assertEqual(remove_char(""), "")

    def test_string_with_special_characters(self):
        self.assertEqual(remove_char("Hello!@#World"), "HelloWorld")

    def test_string_with_numbers(self):
        self.assertEqual(remove_char("Hello123World456"), "HelloWorld")

    def test_string_with_underscores(self):
        self.assertEqual(remove_char("Hello_World"), "HelloWorld")

    def test_string_with_mixed_case(self):
        self.assertEqual(remove_char("HelloWorLD"), "HelloWorld")

    def test_string_with_mixed_case_and_special_characters(self):
        self.assertEqual(remove_char("HelloWorLD!@#"), "HelloWorld")

    def test_string_with_mixed_case_and_numbers(self):
        self.assertEqual(remove_char("HelloWorLD123"), "HelloWorld")

    def test_string_with_mixed_case_and_underscores(self):
        self.assertEqual(remove_char("HelloWorLD_"), "HelloWorld")

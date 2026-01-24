import unittest
from mbpp_676_code import remove_extra_char

class TestRemoveExtraChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_extra_char("Hello, World!"), "HelloWorld")

    def test_edge_case_with_whitespace(self):
        self.assertEqual(remove_extra_char("   Hello, World!   "), "HelloWorld")

    def test_edge_case_with_numbers(self):
        self.assertEqual(remove_extra_char("123Hello456World789"), "123Hello456World789")

    def test_edge_case_with_special_characters(self):
        self.assertEqual(remove_extra_char("@Hello@World@"), "HelloWorld")

    def test_edge_case_with_empty_string(self):
        self.assertEqual(remove_extra_char(""), "")

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            remove_extra_char(12345)

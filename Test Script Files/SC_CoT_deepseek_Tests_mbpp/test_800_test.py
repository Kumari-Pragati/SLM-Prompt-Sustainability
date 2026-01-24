import unittest
from mbpp_800_code import remove_all_spaces

class TestRemoveAllSpaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_all_spaces("Hello World"), "HelloWorld")

    def test_edge_case_single_space(self):
        self.assertEqual(remove_all_spaces("Hello World "), "HelloWorld")

    def test_edge_case_trailing_spaces(self):
        self.assertEqual(remove_all_spaces("Hello World   "), "HelloWorld")

    def test_edge_case_leading_spaces(self):
        self.assertEqual(remove_all_spaces("   Hello World"), "HelloWorld")

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(remove_all_spaces("Hello   World"), "HelloWorld")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_all_spaces(""), "")

    def test_special_case_new_line(self):
        self.assertEqual(remove_all_spaces("Hello\nWorld"), "HelloWorld")

    def test_special_case_tab(self):
        self.assertEqual(remove_all_spaces("Hello\tWorld"), "HelloWorld")

    def test_special_case_mix_of_spaces_new_line_tab(self):
        self.assertEqual(remove_all_spaces("Hello\n\tWorld"), "HelloWorld")

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            remove_all_spaces(None)

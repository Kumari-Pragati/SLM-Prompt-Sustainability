import unittest
from mbpp_800_code import remove_all_spaces

class TestRemoveAllSpaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_all_spaces("Hello World"), "HelloWorld")

    def test_edge_case_single_space(self):
        self.assertEqual(remove_all_spaces(" "), "")

    def test_edge_case_no_spaces(self):
        self.assertEqual(remove_all_spaces(""), "")

    def test_edge_case_leading_trailing_spaces(self):
        self.assertEqual(remove_all_spaces(" Hello World "), "HelloWorld")

    def test_edge_case_tab(self):
        self.assertEqual(remove_all_spaces("\tHello World"), "HelloWorld")

    def test_edge_case_newline(self):
        self.assertEqual(remove_all_spaces("\nHello World\n"), "HelloWorld")

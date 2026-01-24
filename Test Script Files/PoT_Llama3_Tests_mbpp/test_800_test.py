import unittest
from mbpp_800_code import remove_all_spaces

class TestRemoveAllSpaces(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_all_spaces("Hello World"), "HelloWorld")

    def test_multiple_spaces(self):
        self.assertEqual(remove_all_spaces("Hello   World"), "HelloWorld")

    def test_single_space(self):
        self.assertEqual(remove_all_spaces("Hello World"), "HelloWorld")

    def test_no_spaces(self):
        self.assertEqual(remove_all_spaces(""), "")

    def test_empty_string(self):
        self.assertEqual(remove_all_spaces("   "), "")

    def test_edge_case(self):
        self.assertEqual(remove_all_spaces("Hello\tWorld"), "HelloWorld")

    def test_tricky_case(self):
        self.assertEqual(remove_all_spaces("Hello\nWorld"), "HelloWorld")

import unittest
from mbpp_800_code import remove_all_spaces

class TestRemoveAllSpaces(unittest.TestCase):
    def test_remove_all_spaces(self):
        self.assertEqual(remove_all_spaces("Hello World"), "HelloWorld")
        self.assertEqual(remove_all_spaces("   Hello   World   "), "HelloWorld")
        self.assertEqual(remove_all_spaces("Hello\nWorld"), "HelloWorld")
        self.assertEqual(remove_all_spaces("Hello\tWorld"), "HelloWorld")
        self.assertEqual(remove_all_spaces(""), "")
        self.assertEqual(remove_all_spaces("   "), "")
        self.assertEqual(remove_all_spaces("   \t\n"), "")
        self.assertEqual(remove_all_spaces("   Hello   World   \t\n"), "HelloWorld")

    def test_remove_all_spaces_edge_cases(self):
        self.assertEqual(remove_all_spaces("   "), "")
        self.assertEqual(remove_all_spaces("   \t\n"), "")

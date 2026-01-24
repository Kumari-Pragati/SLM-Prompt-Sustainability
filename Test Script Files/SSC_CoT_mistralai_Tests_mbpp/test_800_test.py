import unittest
from mbpp_800_code import remove_all_spaces

class TestRemoveAllSpaces(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(remove_all_spaces("Hello World"), "HelloWorld")

    def test_edge_cases(self):
        self.assertEqual(remove_all_spaces(""), "")
        self.assertEqual(remove_all_spaces("   "), "")
        self.assertEqual(remove_all_spaces("Hello   World"), "HelloWorld")
        self.assertEqual(remove_all_spaces("Hello\tWorld"), "HelloWorld")

    def test_boundary_cases(self):
        self.assertEqual(remove_all_spaces("A "), "A")
        self.assertEqual(remove_all_spaces("World "), "World")
        self.assertEqual(remove_all_spaces("Hello\nWorld"), "HelloWorld")
        self.assertEqual(remove_all_spaces("HelloWorld\n"), "HelloWorld")

    def test_special_cases(self):
        self.assertEqual(remove_all_spaces("Hello, World!"), "Hello,World!")
        self.assertEqual(remove_all_spaces("Hello World\t\n"), "HelloWorld")
        self.assertEqual(remove_all_spaces("123 456 789"), "123456789")

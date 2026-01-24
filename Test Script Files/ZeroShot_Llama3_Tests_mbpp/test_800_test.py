import unittest
from mbpp_800_code import remove_all_spaces

class TestRemoveAllSpaces(unittest.TestCase):

    def test_remove_all_spaces(self):
        self.assertEqual(remove_all_spaces("Hello   World"), "HelloWorld")
        self.assertEqual(remove_all_spaces("   Hello   World   "), "HelloWorld")
        self.assertEqual(remove_all_spaces("Hello   World  !"), "HelloWorld!")
        self.assertEqual(remove_all_spaces("   Hello   World  !   "), "HelloWorld!")
        self.assertEqual(remove_all_spaces("Hello   World  !   @   #"), "HelloWorld!@#")
        self.assertEqual(remove_all_spaces("   Hello   World  !   @   #   "), "HelloWorld!@#")
        self.assertEqual(remove_all_spaces("   Hello   World  !   @   #   $"), "HelloWorld!@#$")
        self.assertEqual(remove_all_spaces("   Hello   World  !   @   #   $   "), "HelloWorld!@#$")

    def test_remove_all_spaces_empty_string(self):
        self.assertEqual(remove_all_spaces(""), "")

    def test_remove_all_spaces_single_space(self):
        self.assertEqual(remove_all_spaces("Hello World"), "HelloWorld")

    def test_remove_all_spaces_multiple_spaces(self):
        self.assertEqual(remove_all_spaces("Hello   World  !   @   #   $"), "HelloWorld!@#$")

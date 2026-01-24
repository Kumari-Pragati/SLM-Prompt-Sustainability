import unittest
from mbpp_892_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):

    def test_remove_spaces(self):
        self.assertEqual(remove_spaces("   Hello   World   "), "Hello World")
        self.assertEqual(remove_spaces("   Hello   World  !"), "Hello World!")
        self.assertEqual(remove_spaces("   Hello   World  !   "), "Hello World!")
        self.assertEqual(remove_spaces("   Hello   World  !  ,   "), "Hello World!,")
        self.assertEqual(remove_spaces("   Hello   World  !  ,  .   "), "Hello World!,.")
        self.assertEqual(remove_spaces("   Hello   World  !  ,  .  ,   "), "Hello World!,.,")
        self.assertEqual(remove_spaces("   Hello   World  !  ,  .  ,  ,   "), "Hello World!,.,,")

    def test_remove_spaces_empty_string(self):
        self.assertEqual(remove_spaces(""), "")

    def test_remove_spaces_single_space(self):
        self.assertEqual(remove_spaces("Hello"), "Hello")

    def test_remove_spaces_multiple_spaces(self):
        self.assertEqual(remove_spaces("Hello   World"), "Hello World")

    def test_remove_spaces_multiple_spaces_with_punctuation(self):
        self.assertEqual(remove_spaces("Hello   World,!"), "Hello World,!")

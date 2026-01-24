import unittest
from mbpp_693_code import remove_multiple_spaces

class TestRemoveMultipleSpaces(unittest.TestCase):

    def test_remove_multiple_spaces(self):
        self.assertEqual(remove_multiple_spaces("   Hello   World   "), "Hello World")
        self.assertEqual(remove_multiple_spaces("   Hello   World  !"), "Hello World!")
        self.assertEqual(remove_multiple_spaces("   Hello   World  !,   "), "Hello World!,")
        self.assertEqual(remove_multiple_spaces("   Hello   World  !,  .   "), "Hello World!,.")
        self.assertEqual(remove_multiple_spaces("   Hello   World  !,  .  ,   "), "Hello World!,.,")
        self.assertEqual(remove_multiple_spaces("   Hello   World  !,  .  ,  ,   "), "Hello World!,.,,")
        self.assertEqual(remove_multiple_spaces("   Hello   World  !,  .  ,  ,  ,   "), "Hello World!,.,,,")
        self.assertEqual(remove_multiple_spaces("   Hello   World  !,  .  ,  ,  ,  ,   "), "Hello World!,.,,,,")
        self.assertEqual(remove_multiple_spaces("   Hello   World  !,  .  ,  ,  ,  ,  ,  ,   "), "Hello World!,.,,,,,")
        self.assertEqual(remove_multiple_spaces("   Hello   World  !,  .  ,  ,  ,  ,  ,  ,  ,  ,   "), "Hello World!,,,,,,,,,")
        self.assertEqual(remove_multiple_spaces("   Hello   World  !,  .  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,   "), "Hello World!,,,,,,,,,,")

    def test_remove_multiple_spaces_with_empty_string(self):
        self.assertEqual(remove_multiple_spaces(""), "")

    def test_remove_multiple_spaces_with_single_space(self):
        self.assertEqual(remove_multiple_spaces("Hello"), "Hello")

    def test_remove_multiple_spaces_with_single_space_and_punctuation(self):
        self.assertEqual(remove_multiple_spaces("Hello!"), "Hello!")
        self.assertEqual(remove_multiple_spaces("Hello?"), "Hello?")
        self.assertEqual(remove_multiple_spaces("Hello,"), "Hello,")

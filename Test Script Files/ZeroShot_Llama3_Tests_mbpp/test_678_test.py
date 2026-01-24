import unittest
from mbpp_678_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):

    def test_remove_spaces(self):
        self.assertEqual(remove_spaces("Hello World"), "HelloWorld")
        self.assertEqual(remove_spaces("   Hello   World   "), "HelloWorld")
        self.assertEqual(remove_spaces(""), "")
        self.assertEqual(remove_spaces("Hello"), "Hello")
        self.assertEqual(remove_spaces("   "), "")

    def test_remove_spaces_with_punctuation(self):
        self.assertEqual(remove_spaces("Hello, World!"), "Hello,World!")
        self.assertEqual(remove_spaces("Hello. World,!"), "Hello.World,!")
        self.assertEqual(remove_spaces("Hello? World!"), "Hello?World!")

    def test_remove_spaces_with_numbers(self):
        self.assertEqual(remove_spaces("Hello 123 World"), "Hello123World")
        self.assertEqual(remove_spaces("   123   "), "")
        self.assertEqual(remove_spaces("123"), "123")

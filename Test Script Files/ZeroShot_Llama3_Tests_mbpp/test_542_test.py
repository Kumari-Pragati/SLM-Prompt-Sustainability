import unittest
from mbpp_542_code import fill_spaces

class TestFillSpaces(unittest.TestCase):

    def test_fill_spaces(self):
        self.assertEqual(fill_spaces("Hello, world!"), "Hello:world!")
        self.assertEqual(fill_spaces("This is a test. 123"), "This:is:a:test.:123")
        self.assertEqual(fill_spaces("Python is awesome"), "Python:is:awesome")
        self.assertEqual(fill_spaces("No spaces needed"), "No:spaces:needed")
        self.assertEqual(fill_spaces("Multiple spaces"), "Multiple:spaces")
        self.assertEqual(fill_spaces("No punctuation needed"), "No:punctuation:needed")
        self.assertEqual(fill_spaces("No text"), "")
        self.assertEqual(fill_spaces("Only spaces"), ":")
        self.assertEqual(fill_spaces("Only punctuation"), ":")

    def test_fill_spaces_empty_string(self):
        self.assertEqual(fill_spaces(""), "")

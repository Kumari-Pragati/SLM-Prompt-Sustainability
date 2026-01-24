import unittest
from mbpp_542_code import fill_spaces

class TestFillSpaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(fill_spaces("Hello, world."), "Hello:world:")

    def test_empty_string(self):
        self.assertEqual(fill_spaces(""), "")

    def test_no_spaces_or_punctuation(self):
        self.assertEqual(fill_spaces("nospaces"), "nospaces")

    def test_multiple_spaces_and_punctuation(self):
        self.assertEqual(fill_spaces("Hello,   world!  ."), "Hello:world!:")

    def test_spaces_at_start_and_end(self):
        self.assertEqual(fill_spaces(" Hello, world. "), "Hello:world:")

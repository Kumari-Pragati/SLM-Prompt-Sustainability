import unittest
from mbpp_73_code import multiple_split

class TestMultipleSplit(unittest.TestCase):
    def test_single_split(self):
        self.assertEqual(multiple_split("Hello;World"), ["Hello", "World"])

    def test_multiple_splits(self):
        self.assertEqual(multiple_split("Hello;World;Python"), ["Hello", "World", "Python"])

    def test_split_with_comma(self):
        self.assertEqual(multiple_split("Hello,World,Python"), ["Hello", "World", "Python"])

    def test_split_with_star(self):
        self.assertEqual(multiple_split("Hello*World*Python"), ["Hello", "World", "Python"])

    def test_split_with_newline(self):
        self.assertEqual(multiple_split("Hello\nWorld\nPython"), ["Hello", "World", "Python"])

    def test_empty_input(self):
        self.assertEqual(multiple_split(""), [])

    def test_single_input(self):
        self.assertEqual(multiple_split("Hello"), ["Hello"])

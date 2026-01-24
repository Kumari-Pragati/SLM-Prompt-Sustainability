import unittest
from mbpp_73_code import multiple_split

class TestMultipleSplit(unittest.TestCase):
    def test_simple_split(self):
        self.assertEqual(multiple_split("Hello;World"), ["Hello", "World"])
    def test_split_with_comma(self):
        self.assertEqual(multiple_split("Hello,World"), ["Hello", "World"])
    def test_split_with_star(self):
        self.assertEqual(multiple_split("Hello*World"), ["Hello", "World"])
    def test_split_with_newline(self):
        self.assertEqual(multiple_split("Hello\nWorld"), ["Hello", "World"])
    def test_split_with_multiple_separators(self):
        self.assertEqual(multiple_split("Hello;World,*, Foo\nBar"), ["Hello", "World", "Foo", "Bar"])
    def test_split_with_empty_input(self):
        self.assertEqual(multiple_split(""), [])
    def test_split_with_single_input(self):
        self.assertEqual(multiple_split("Hello"), ["Hello"])
    def test_split_with_multiple_inputs(self):
        self.assertEqual(multiple_split("Hello;World,*, Foo\nBar"), ["Hello", "World", "Foo", "Bar"])

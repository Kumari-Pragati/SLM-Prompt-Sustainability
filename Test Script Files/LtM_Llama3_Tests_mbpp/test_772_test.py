import unittest
from mbpp_772_code import remove_length

class TestRemoveLength(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(remove_length("Hello World", 5), "Hello World")
        self.assertEqual(remove_length("Hello World", 11), "Hello")
        self.assertEqual(remove_length("Hello World", 3), "Hello World")

    def test_empty(self):
        self.assertEqual(remove_length("", 5), "")
        self.assertEqual(remove_length(" ", 5), " ")

    def test_single_word(self):
        self.assertEqual(remove_length("Hello", 5), "Hello")
        self.assertEqual(remove_length("Hello", 3), "Hello")

    def test_multiple_words(self):
        self.assertEqual(remove_length("Hello World Foo", 5), "Hello World Foo")
        self.assertEqual(remove_length("Hello World Foo", 11), "Hello Foo")
        self.assertEqual(remove_length("Hello World Foo", 3), "Hello World Foo")

    def test_edge_case(self):
        self.assertEqual(remove_length("Hello World Foo", 0), "Hello World Foo")
        self.assertEqual(remove_length("Hello World Foo", 12), "Hello")

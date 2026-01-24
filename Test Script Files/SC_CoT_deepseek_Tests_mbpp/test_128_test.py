import unittest
from mbpp_128_code import long_words

class TestLongWords(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(long_words(5, "Hello World"), ["Hello", "World"])

    def test_edge_case(self):
        self.assertEqual(long_words(0, "Hello World"), ["Hello", "World"])
        self.assertEqual(long_words(11, "Hello World"), [])

    def test_corner_case(self):
        self.assertEqual(long_words(5, ""), [])
        self.assertEqual(long_words(5, "a"), [])
        self.assertEqual(long_words(5, "a b c d e f g h i j"), ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            long_words("five", "Hello World")
        with self.assertRaises(TypeError):
            long_words(5, ["Hello", "World"])

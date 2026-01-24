import unittest
from mbpp_128_code import long_words

class TestLongWords(unittest.TestCase):
    def test_long_words_typical(self):
        self.assertEqual(long_words(5, "Hello World"), ["World"])
    def test_long_words_edge(self):
        self.assertEqual(long_words(5, "a b c"), [])
    def test_long_words_edge2(self):
        self.assertEqual(long_words(5, "a b c d"), ["d"])
    def test_long_words_invalid_input(self):
        with self.assertRaises(TypeError):
            long_words("five", "Hello World")
    def test_long_words_invalid_input2(self):
        with self.assertRaises(TypeError):
            long_words(5, 123)

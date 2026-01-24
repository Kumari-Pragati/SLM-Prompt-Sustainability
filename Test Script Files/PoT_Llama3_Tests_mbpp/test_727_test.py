import unittest
from mbpp_727_code import remove_char

class TestRemoveChar(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(remove_char("Hello World!"), "HelloWorld")
        self.assertEqual(remove_char("Python is fun!"), "Pythonisfun")
        self.assertEqual(remove_char("1234567890"), "1234567890")

    def test_edge(self):
        self.assertEqual(remove_char(""), "")
        self.assertEqual(remove_char("a"), "a")
        self.assertEqual(remove_char("abc"), "abc")

    def test_corner(self):
        self.assertEqual(remove_char("a_b"), "a")
        self.assertEqual(remove_char("a@b"), "a")
        self.assertEqual(remove_char("a#b"), "a")

    def test_invalid(self):
        with self.assertRaises(TypeError):
            remove_char(None)
        with self.assertRaises(TypeError):
            remove_char(123)

import unittest
from mbpp_727_code import remove_char

class TestRemoveChar(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(remove_char("Hello World"), "HelloWorld")
        self.assertEqual(remove_char("Hello_World"), "HelloWorld")
        self.assertEqual(remove_char("Hello123"), "Hello123")
        self.assertEqual(remove_char("Hello123!"), "Hello123")

    def test_edge(self):
        self.assertEqual(remove_char(""), "")
        self.assertEqual(remove_char("a"), "a")
        self.assertEqual(remove_char("a b"), "ab")
        self.assertEqual(remove_char("a b c"), "abc")

    def test_invalid(self):
        with self.assertRaises(TypeError):
            remove_char(None)
        with self.assertRaises(TypeError):
            remove_char(123)

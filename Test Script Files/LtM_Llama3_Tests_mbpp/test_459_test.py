import unittest
from mbpp_459_code import remove_uppercase

class TestRemoveUppercase(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(remove_uppercase("hello"), "ello")
        self.assertEqual(remove_uppercase("HELLO"), "ello")
        self.assertEqual(remove_uppercase("123"), "123")
        self.assertEqual(remove_uppercase("abc"), "abc")

    def test_edge(self):
        self.assertEqual(remove_uppercase(""), "")
        self.assertEqual(remove_uppercase("a"), "a")
        self.assertEqual(remove_uppercase("ABC"), "")

    def test_invalid(self):
        with self.assertRaises(TypeError):
            remove_uppercase(123)
        with self.assertRaises(TypeError):
            remove_uppercase([1, 2, 3])

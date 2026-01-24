import unittest
from mbpp_668_code import replace

class TestReplace(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(replace("Hello, world!", 'o'), "Hello, world!")
        self.assertEqual(replace("Hello, world!", 'w'), "Hell, rld!")
        self.assertEqual(replace("Hello, world!", 'H'), "ello, world!")

    def test_edge(self):
        self.assertEqual(replace("", 'o'), "")
        self.assertEqual(replace("Hello, world!", 'o'), "Hello, world!")
        self.assertEqual(replace("Hello, world!", 'o'), "Hello, world!")
        self.assertEqual(replace("Hello, world!", 'o'), "Hello, world!")

    def test_invalid(self):
        with self.assertRaises(TypeError):
            replace(None, 'o')
        with self.assertRaises(TypeError):
            replace("Hello, world!", None)

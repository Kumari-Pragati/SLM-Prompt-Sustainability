import unittest
from mbpp_204_code import count

class TestCount(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(count('hello', 'l'), 2)
        self.assertEqual(count('hello', 'o'), 1)
        self.assertEqual(count('hello', 'h'), 1)

    def test_edge(self):
        self.assertEqual(count('', 'a'), 0)
        self.assertEqual(count('a', 'a'), 1)
        self.assertEqual(count('abc', 'b'), 1)

    def test_corner(self):
        self.assertEqual(count('hello', 'x'), 0)
        self.assertEqual(count('hello', 'H'), 1)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            count(123, 'a')
        with self.assertRaises(TypeError):
            count('hello', 123)

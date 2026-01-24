import unittest
from mbpp_350_code import minimum_Length

class TestMinimumLength(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(minimum_Length("abc"), 1)
        self.assertEqual(minimum_Length("abca"), 1)
        self.assertEqual(minimum_Length("abcabc"), 1)

    def test_edge(self):
        self.assertEqual(minimum_Length(""), 26)
        self.assertEqual(minimum_Length("a"), 25)
        self.assertEqual(minimum_Length("abcde"), 1)

    def test_corner(self):
        self.assertEqual(minimum_Length("aabbcc"), 2)
        self.assertEqual(minimum_Length("aabbccdd"), 2)
        self.assertEqual(minimum_Length("aabbccddaa"), 1)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            minimum_Length(123)
        with self.assertRaises(TypeError):
            minimum_Length([1, 2, 3])

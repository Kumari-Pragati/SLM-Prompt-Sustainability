import unittest
from mbpp_944_code import num_position

class TestNumPosition(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(num_position("123abc"), 0)
        self.assertEqual(num_position("abc456"), 3)
        self.assertEqual(num_position("123456"), 0)

    def test_edge(self):
        self.assertEqual(num_position(""), None)
        self.assertEqual(num_position("abc"), None)
        self.assertEqual(num_position("123456789"), 0)

    def test_edge2(self):
        self.assertEqual(num_position("abc123"), 3)
        self.assertEqual(num_position("123abc"), 0)
        self.assertEqual(num_position("1234567890"), 0)

    def test_edge3(self):
        self.assertEqual(num_position("123"), 0)
        self.assertEqual(num_position("456"), 0)
        self.assertEqual(num_position("789"), 0)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            num_position("abc def")

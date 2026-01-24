import unittest
from mbpp_944_code import num_position

class TestNumPosition(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(num_position("Hello123World"), 4)
        self.assertEqual(num_position("abc456def"), 3)
        self.assertEqual(num_position("123abc456"), 0)

    def test_edge(self):
        self.assertEqual(num_position(""), -1)
        self.assertEqual(num_position("abc"), -1)
        self.assertEqual(num_position("123"), 0)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            num_position(None)
        with self.assertRaises(TypeError):
            num_position("")

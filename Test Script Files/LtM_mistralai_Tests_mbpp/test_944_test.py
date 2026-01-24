import unittest
from mbpp_944_code import num_position

class TestNumPosition(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(num_position("123"), 0)
        self.assertEqual(num_position("12345"), 0)
        self.assertEqual(num_position("123456"), 0)
        self.assertEqual(num_position("1234567"), 1)
        self.assertEqual(num_position("12345678"), 0)

    def test_edge_and_boundary(self):
        self.assertEqual(num_position(""), -1)
        self.assertEqual(num_position("0"), 0)
        self.assertEqual(num_position("1"), 0)
        self.assertEqual(num_position("9"), 0)
        self.assertEqual(num_position("10"), -1)
        self.assertEqual(num_position("123456789"), 8)
        self.assertEqual(num_position("1234567890"), 9)

    def test_complex(self):
        self.assertEqual(num_position("a1b2c3"), 1)
        self.assertEqual(num_position("1a2b3c"), 0)
        self.assertEqual(num_position("12a3b4c"), 2)
        self.assertEqual(num_position("123a4b5c"), 3)
        self.assertEqual(num_position("1234a5b6c"), 4)
        self.assertEqual(num_position("12345a6b7c"), 5)
        self.assertEqual(num_position("123456a7b8c"), 6)
        self.assertEqual(num_position("1234567a8b9c"), 7)

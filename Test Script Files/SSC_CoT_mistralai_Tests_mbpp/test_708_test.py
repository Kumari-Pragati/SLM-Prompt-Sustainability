import unittest
from mbpp_708_code import Convert

class TestConvert(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(Convert("hello world"), ["hello", "world"])
        self.assertListEqual(Convert("a b c"), ["a", "b", "c"])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(Convert(""), [])
        self.assertListEqual(Convert("   "), [""])
        self.assertListEqual(Convert("a b c d e f g h i j k l m n o p q r s t u v w x y z"), ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
        self.assertListEqual(Convert("a b c d e f g h i j k l m n o p q r s t u v w x y z a"), ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a"])

    def test_invalid_input(self):
        self.assertRaises(ValueError, Convert, "123")
        self.assertRaises(ValueError, Convert, "hello123")
        self.assertRaises(ValueError, Convert, "hello world!")

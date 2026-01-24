import unittest
from mbpp_118_code import string_to_list

class TestStringToList(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(string_to_list("hello world"), ["hello", "world"])

    def test_edge_and_boundary_cases(self):
        self.assertListEqual(string_to_list(""), [])
        self.assertListEqual(string_to_list("a"), ["a"])
        self.assertListEqual(string_to_list("a b c d e f g h i j k l m n o p q r s t u v w x y z"),
                              ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                               "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
        self.assertListEqual(string_to_list("a b c d e f g h i j k l m n o p q r s t u v w x y z a"),
                              ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                               "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a"])

    def test_special_cases(self):
        self.assertListEqual(string_to_list("hello world!"), ["hello", "world", "!"])
        self.assertListEqual(string_to_list("hello-world"), ["hello", "-", "world"])

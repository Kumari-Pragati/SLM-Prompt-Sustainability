import unittest
from mbpp_15_code import split_lowerstring

class TestSplitLowerstring(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(split_lowerstring("HelloWorld"), ["Hello", "World"])

    def test_edge_case(self):
        self.assertEqual(split_lowerstring("Hello"), ["Hello"])

    def test_edge_case2(self):
        self.assertEqual(split_lowerstring("World"), ["World"])

    def test_edge_case3(self):
        self.assertEqual(split_lowerstring(""), [])

    def test_edge_case4(self):
        self.assertEqual(split_lowerstring("abc"), ["abc"])

    def test_edge_case5(self):
        self.assertEqual(split_lowerstring("abc123"), ["abc", "123"])

    def test_edge_case6(self):
        self.assertEqual(split_lowerstring("abcABC"), ["abc", "ABC"])

    def test_edge_case7(self):
        self.assertEqual(split_lowerstring("abc123ABC"), ["abc", "123", "ABC"])

    def test_edge_case8(self):
        self.assertEqual(split_lowerstring("abc123ABC123"), ["abc", "123", "ABC", "123"])

    def test_edge_case9(self):
        self.assertEqual(split_lowerstring("abc123ABC123abc"), ["abc", "123", "ABC", "123", "abc"])

    def test_edge_case10(self):
        self.assertEqual(split_lowerstring("abc123ABC123abcABC"), ["abc", "123", "ABC", "123", "abc", "ABC"])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            split_lowerstring(123)

import unittest
from mbpp_128_code import long_words

class TestLongWords(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(long_words(5, "Hello World"), ["World"])

    def test_edge_case(self):
        self.assertEqual(long_words(5, "Hello"), [])

    def test_edge_case2(self):
        self.assertEqual(long_words(5, "Hello World Hello"), ["World"])

    def test_edge_case3(self):
        self.assertEqual(long_words(5, "Hello World Hello World"), ["World", "World"])

    def test_edge_case4(self):
        self.assertEqual(long_words(5, "Hello World Hello World Hello"), ["World", "World"])

    def test_edge_case5(self):
        self.assertEqual(long_words(5, "Hello World Hello World Hello World"), ["World", "World"])

    def test_edge_case6(self):
        self.assertEqual(long_words(5, "Hello World Hello World Hello World Hello"), ["World", "World"])

    def test_edge_case7(self):
        self.assertEqual(long_words(5, "Hello World Hello World Hello World Hello World"), ["World", "World"])

    def test_edge_case8(self):
        self.assertEqual(long_words(5, "Hello World Hello World Hello World Hello World Hello"), ["World", "World"])

    def test_edge_case9(self):
        self.assertEqual(long_words(5, "Hello World Hello World Hello World Hello World Hello World"), ["World", "World"])

    def test_edge_case10(self):
        self.assertEqual(long_words(5, "Hello World Hello World Hello World Hello World Hello World Hello"), ["World", "World"])

    def test_edge_case11(self):
        self.assertEqual(long_words(5, "Hello World Hello World Hello World Hello World Hello World Hello World"), ["World", "World"])

    def test_edge_case12(self):
        self.assertEqual(long_words(5, "Hello World Hello World Hello World Hello World Hello World Hello World"), ["World", "World"])

    def test_edge_case13(self):
        self.assertEqual(long_words(5, "Hello World Hello World Hello World Hello World Hello World Hello World Hello"), ["World", "World"])

    def test_edge_case14(self):
        self.assertEqual(long_words(5, "Hello World Hello World Hello World Hello World Hello World Hello World Hello"), ["World", "World"])

    def test_edge_case15(self):
        self.assertEqual(long_words(5, "Hello World Hello World Hello World Hello World Hello World Hello World Hello"), ["World", "World"])

    def test_edge_case16(self):
        self.assertEqual(long_words(5, "Hello World Hello World Hello World Hello World Hello World Hello World Hello"), ["World", "World"])

    def test_edge_case17(self):
        self.assertEqual(long_words(5, "Hello World Hello World Hello World Hello World Hello World Hello World Hello"), ["World", "World"])

    def test_edge_case18(self):
        self.assertEqual(long_words(5, "Hello World Hello World Hello World Hello World Hello World Hello World Hello"), ["World", "World"])

    def test_edge_case19(self):
        self.assertEqual(long_words(5, "Hello World Hello World Hello World Hello World Hello World Hello World Hello"), ["World", "World"])

    def test_edge_case20(self):
        self.assertEqual(long_words(5, "Hello World Hello World Hello World Hello World Hello World Hello World Hello"), ["World", "World"])

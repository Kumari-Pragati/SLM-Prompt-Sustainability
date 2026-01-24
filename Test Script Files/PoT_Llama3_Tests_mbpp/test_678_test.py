import unittest
from mbpp_678_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(remove_spaces("Hello World"), "HelloWorld")

    def test_edge(self):
        self.assertEqual(remove_spaces(""), "")
        self.assertEqual(remove_spaces("a"), "a")

    def test_edge2(self):
        self.assertEqual(remove_spaces("   "), "")

    def test_edge3(self):
        self.assertEqual(remove_spaces("a b c"), "abc")

    def test_edge4(self):
        self.assertEqual(remove_spaces("a   b   c"), "abc")

    def test_edge5(self):
        self.assertEqual(remove_spaces("a b c d"), "abcd")

    def test_edge6(self):
        self.assertEqual(remove_spaces("a   b   c   d"), "abcd")

    def test_edge7(self):
        self.assertEqual(remove_spaces("a b c d e"), "abcde")

    def test_edge8(self):
        self.assertEqual(remove_spaces("a   b   c   d   e"), "abcde")

    def test_edge9(self):
        self.assertEqual(remove_spaces("a b c d e f"), "abcdef")

    def test_edge10(self):
        self.assertEqual(remove_spaces("a   b   c   d   e   f"), "abcdef")

    def test_edge11(self):
        self.assertEqual(remove_spaces("a b c d e f g"), "abcdefg")

    def test_edge12(self):
        self.assertEqual(remove_spaces("a   b   c   d   e   f   g"), "abcdefg")

    def test_edge13(self):
        self.assertEqual(remove_spaces("a b c d e f g h"), "abcdefgh")

    def test_edge14(self):
        self.assertEqual(remove_spaces("a   b   c   d   e   f   g   h"), "abcdefgh")

    def test_edge15(self):
        self.assertEqual(remove_spaces("a b c d e f g h i"), "abcdefghi")

    def test_edge16(self):
        self.assertEqual(remove_spaces("a   b   c   d   e   f   g   h   i"), "abcdefghi")

    def test_edge17(self):
        self.assertEqual(remove_spaces("a b c d e f g h i j"), "abcdefghij")

    def test_edge18(self):
        self.assertEqual(remove_spaces("a   b   c   d   e   f   g   h   i   j"), "abcdefghij")

    def test_edge19(self):
        self.assertEqual(remove_spaces("a b c d e f g h i j k"), "abcdefghijk")

    def test_edge20(self):
        self.assertEqual(remove_spaces("a   b   c   d   e   f   g   h   i   j   k"), "abcdefghijk")

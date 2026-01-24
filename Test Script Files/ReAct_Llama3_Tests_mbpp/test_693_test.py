import unittest
from mbpp_693_code import remove_multiple_spaces

class TestRemoveMultipleSpaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_multiple_spaces("Hello   World"), "Hello World")

    def test_edge_case1(self):
        self.assertEqual(remove_multiple_spaces("   "), " ")

    def test_edge_case2(self):
        self.assertEqual(remove_multiple_spaces("a b c"), "a b c")

    def test_edge_case3(self):
        self.assertEqual(remove_multiple_spaces("a   b   c"), "a b c")

    def test_edge_case4(self):
        self.assertEqual(remove_multiple_spaces("a   b   c   d"), "a b c d")

    def test_edge_case5(self):
        self.assertEqual(remove_multiple_spaces("a   b   c   d   e"), "a b c d e")

    def test_edge_case6(self):
        self.assertEqual(remove_multiple_spaces("a   b   c   d   e   f"), "a b c d e f")

    def test_edge_case7(self):
        self.assertEqual(remove_multiple_spaces("a   b   c   d   e   f   g"), "a b c d e f g")

    def test_edge_case8(self):
        self.assertEqual(remove_multiple_spaces("a   b   c   d   e   f   g   h"), "a b c d e f g h")

    def test_edge_case9(self):
        self.assertEqual(remove_multiple_spaces("a   b   c   d   e   f   g   h   i"), "a b c d e f g h i")

    def test_edge_case10(self):
        self.assertEqual(remove_multiple_spaces("a   b   c   d   e   f   g   h   i   j"), "a b c d e f g h i j")

    def test_edge_case11(self):
        self.assertEqual(remove_multiple_spaces("a   b   c   d   e   f   g   h   i   j   k"), "a b c d e f g h i j k")

    def test_edge_case12(self):
        self.assertEqual(remove_multiple_spaces("a   b   c   d   e   f   g   h   i   j   k   l"), "a b c d e f g h i j k l")

    def test_edge_case13(self):
        self.assertEqual(remove_multiple_spaces("a   b   c   d   e   f   g   h   i   j   k   l   m"), "a b c d e f g h i j k l m")

    def test_edge_case14(self):
        self.assertEqual(remove_multiple_spaces("a   b   c   d   e   f   g   h   i   j   k   l   m   n"), "a b c d e f g h i j k l m n")

    def test_edge_case15(self):
        self.assertEqual(remove_multiple_spaces("a   b   c   d   e   f   g   h   i   j   k   l   m   n   o"), "a b c d e f g h i j k l m n o")

    def test_edge_case16(self):
        self.assertEqual(remove_multiple_spaces("a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p"), "a b c d e f g h i j k l m n o p")

    def test_edge_case17(self):
        self.assertEqual(remove_multiple_spaces("a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q"), "a b c d e f g h i j k l m n o p q")

    def test_edge_case18(self):
        self.assertEqual(remove_multiple_spaces("a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   r"), "a b c d e f g h i j k l m n o p q r")

    def test_edge_case19(self):
        self.assertEqual(remove_multiple_spaces("a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   r   s"), "a b c d e f g h i j k l m n o p q r s")

    def test_edge_case20(self):
        self.assertEqual(remove_multiple_spaces("a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   r   s   t"), "a b c d e f g h i j k l m n o p q r s t")

import unittest
from mbpp_377_code import remove_Char

class TestRemoveChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_Char("hello world", "o"), "hell wrld")

    def test_edge_case(self):
        self.assertEqual(remove_Char("hello world", "l"), "hwo rd")

    def test_edge_case2(self):
        self.assertEqual(remove_Char("hello world", "w"), "helo orl")

    def test_edge_case3(self):
        self.assertEqual(remove_Char("hello world", "h"), "ello orld")

    def test_edge_case4(self):
        self.assertEqual(remove_Char("hello world", "d"), "hello world")

    def test_edge_case5(self):
        self.assertEqual(remove_Char("hello world", "z"), "hello world")

    def test_edge_case6(self):
        self.assertEqual(remove_Char("hello world", "x"), "hello world")

    def test_edge_case7(self):
        self.assertEqual(remove_Char("hello world", " "), "helloworld")

    def test_edge_case8(self):
        self.assertEqual(remove_Char("hello world", "a"), "hello world")

    def test_edge_case9(self):
        self.assertEqual(remove_Char("hello world", "b"), "hello world")

    def test_edge_case10(self):
        self.assertEqual(remove_Char("hello world", "c"), "hello world")

    def test_edge_case11(self):
        self.assertEqual(remove_Char("hello world", "e"), "hello world")

    def test_edge_case12(self):
        self.assertEqual(remove_Char("hello world", "f"), "hello world")

    def test_edge_case13(self):
        self.assertEqual(remove_Char("hello world", "g"), "hello world")

    def test_edge_case14(self):
        self.assertEqual(remove_Char("hello world", "i"), "hello world")

    def test_edge_case15(self):
        self.assertEqual(remove_Char("hello world", "j"), "hello world")

    def test_edge_case16(self):
        self.assertEqual(remove_Char("hello world", "k"), "hello world")

    def test_edge_case17(self):
        self.assertEqual(remove_Char("hello world", "m"), "hello world")

    def test_edge_case18(self):
        self.assertEqual(remove_Char("hello world", "n"), "hello world")

    def test_edge_case19(self):
        self.assertEqual(remove_Char("hello world", "p"), "hello world")

    def test_edge_case20(self):
        self.assertEqual(remove_Char("hello world", "q"), "hello world")

    def test_edge_case21(self):
        self.assertEqual(remove_Char("hello world", "r"), "hello world")

    def test_edge_case22(self):
        self.assertEqual(remove_Char("hello world", "s"), "hello world")

    def test_edge_case23(self):
        self.assertEqual(remove_Char("hello world", "t"), "hello world")

    def test_edge_case24(self):
        self.assertEqual(remove_Char("hello world", "u"), "hello world")

    def test_edge_case25(self):
        self.assertEqual(remove_Char("hello world", "v"), "hello world")

    def test_edge_case26(self):
        self.assertEqual(remove_Char("hello world", "w"), "hello world")

    def test_edge_case27(self):
        self.assertEqual(remove_Char("hello world", "x"), "hello world")

    def test_edge_case28(self):
        self.assertEqual(remove_Char("hello world", "y"), "hello world")

    def test_edge_case29(self):
        self.assertEqual(remove_Char("hello world", "z"), "hello world")

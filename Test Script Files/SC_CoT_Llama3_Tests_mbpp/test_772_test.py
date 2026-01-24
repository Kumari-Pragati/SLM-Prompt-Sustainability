import unittest
from mbpp_772_code import remove_length

class TestRemoveLength(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(remove_length("Hello World", 5), "Hello World")

    def test_edge_case1(self):
        self.assertEqual(remove_length("Hello", 5), "Hello")

    def test_edge_case2(self):
        self.assertEqual(remove_length("Hello", 1), "")

    def test_edge_case3(self):
        self.assertEqual(remove_length("Hello", 0), "Hello")

    def test_edge_case4(self):
        self.assertEqual(remove_length("Hello", 7), "")

    def test_edge_case5(self):
        self.assertEqual(remove_length("Hello World", 0), "Hello World")

    def test_edge_case6(self):
        self.assertEqual(remove_length("Hello World", 7), "Hello")

    def test_edge_case7(self):
        self.assertEqual(remove_length("Hello World", 11), "")

    def test_edge_case8(self):
        self.assertEqual(remove_length("Hello World", 12), "Hello World")

    def test_edge_case9(self):
        self.assertEqual(remove_length("Hello World", 13), "")

    def test_edge_case10(self):
        self.assertEqual(remove_length("Hello World", 14), "Hello World")

    def test_edge_case11(self):
        self.assertEqual(remove_length("Hello World", 15), "")

    def test_edge_case12(self):
        self.assertEqual(remove_length("Hello World", 16), "Hello World")

    def test_edge_case13(self):
        self.assertEqual(remove_length("Hello World", 17), "")

    def test_edge_case14(self):
        self.assertEqual(remove_length("Hello World", 18), "Hello World")

    def test_edge_case15(self):
        self.assertEqual(remove_length("Hello World", 19), "")

    def test_edge_case16(self):
        self.assertEqual(remove_length("Hello World", 20), "Hello World")

    def test_edge_case17(self):
        self.assertEqual(remove_length("Hello World", 21), "")

    def test_edge_case18(self):
        self.assertEqual(remove_length("Hello World", 22), "Hello World")

    def test_edge_case19(self):
        self.assertEqual(remove_length("Hello World", 23), "")

    def test_edge_case20(self):
        self.assertEqual(remove_length("Hello World", 24), "Hello World")

    def test_edge_case21(self):
        self.assertEqual(remove_length("Hello World", 25), "")

    def test_edge_case22(self):
        self.assertEqual(remove_length("Hello World", 26), "Hello World")

    def test_edge_case23(self):
        self.assertEqual(remove_length("Hello World", 27), "")

    def test_edge_case24(self):
        self.assertEqual(remove_length("Hello World", 28), "Hello World")

    def test_edge_case25(self):
        self.assertEqual(remove_length("Hello World", 29), "")

    def test_edge_case26(self):
        self.assertEqual(remove_length("Hello World", 30), "Hello World")

    def test_edge_case27(self):
        self.assertEqual(remove_length("Hello World", 31), "")

    def test_edge_case28(self):
        self.assertEqual(remove_length("Hello World", 32), "Hello World")

    def test_edge_case29(self):
        self.assertEqual(remove_length("Hello World", 33), "")

    def test_edge_case30(self):
        self.assertEqual(remove_length("Hello World", 34), "Hello World")

    def test_edge_case31(self):
        self.assertEqual(remove_length("Hello World", 35), "")

    def test_edge_case32(self):
        self.assertEqual(remove_length("Hello World", 36), "Hello World")

    def test_edge_case33(self):
        self.assertEqual(remove_length("Hello World", 37), "")

    def test_edge_case34(self):
        self.assertEqual(remove_length("Hello World", 38), "Hello World")

    def test_edge_case35(self):
        self.assertEqual(remove_length("Hello World", 39), "")

    def test_edge_case36(self):
        self.assertEqual(remove_length("Hello World", 40), "Hello World")

    def test_edge_case37(self):
        self.assertEqual(remove_length("Hello World", 41), "")

    def test_edge_case38(self):
        self.assertEqual(remove_length("Hello World", 42), "Hello World")

    def test_edge_case39(self):
        self.assertEqual(remove_length("Hello World", 43), "")

    def test_edge_case40(self):
        self.assertEqual(remove_length("Hello World", 44), "Hello World")

    def test_edge_case41(self):
        self.assertEqual(remove_length("Hello World", 45), "")

    def test_edge_case42(self):
        self.assertEqual(remove_length("Hello World", 46), "Hello World")

    def test_edge_case43(self):
        self.assertEqual(remove_length("Hello World", 47), "")

    def test_edge_case44(self):
        self.assertEqual(remove_length("Hello World", 48),
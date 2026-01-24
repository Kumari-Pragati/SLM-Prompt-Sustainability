import unittest
from mbpp_173_code import remove_splchar

class TestRemoveSplchar(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(remove_splchar("Hello, World!"), "Hello World")

    def test_edge_case(self):
        self.assertEqual(remove_splchar("Hello World!"), "Hello World")

    def test_edge_case2(self):
        self.assertEqual(remove_splchar("Hello World"), "Hello World")

    def test_edge_case3(self):
        self.assertEqual(remove_splchar("Hello"), "Hello")

    def test_edge_case4(self):
        self.assertEqual(remove_splchar("World"), "World")

    def test_edge_case5(self):
        self.assertEqual(remove_splchar("123"), "123")

    def test_edge_case6(self):
        self.assertEqual(remove_splchar("123abc"), "123abc")

    def test_edge_case7(self):
        self.assertEqual(remove_splchar("123abc456"), "123abc456")

    def test_edge_case8(self):
        self.assertEqual(remove_splchar("123abc456def"), "123abc456def")

    def test_edge_case9(self):
        self.assertEqual(remove_splchar("123abc456defghi"), "123abc456defghi")

    def test_edge_case10(self):
        self.assertEqual(remove_splchar("123abc456defghij"), "123abc456defghij")

    def test_edge_case11(self):
        self.assertEqual(remove_splchar("123abc456defghijk"), "123abc456defghijk")

    def test_edge_case12(self):
        self.assertEqual(remove_splchar("123abc456defghijkl"), "123abc456defghijkl")

    def test_edge_case13(self):
        self.assertEqual(remove_splchar("123abc456defghijklm"), "123abc456defghijklm")

    def test_edge_case14(self):
        self.assertEqual(remove_splchar("123abc456defghijklmn"), "123abc456defghijklmn")

    def test_edge_case15(self):
        self.assertEqual(remove_splchar("123abc456defghijklmno"), "123abc456defghijklmno")

    def test_edge_case16(self):
        self.assertEqual(remove_splchar("123abc456defghijklmnop"), "123abc456defghijklmnop")

    def test_edge_case17(self):
        self.assertEqual(remove_splchar("123abc456defghijklmnopq"), "123abc456defghijklmnopq")

    def test_edge_case18(self):
        self.assertEqual(remove_splchar("123abc456defghijklmnopqr"), "123abc456defghijklmnopqr")

    def test_edge_case19(self):
        self.assertEqual(remove_splchar("123abc456defghijklmnopqrs"), "123abc456defghijklmnopqrs")

    def test_edge_case20(self):
        self.assertEqual(remove_splchar("123abc456defghijklmnopqrst"), "123abc456defghijklmnopqrst")

    def test_edge_case21(self):
        self.assertEqual(remove_splchar("123abc456defghijklmnopqrstu"), "123abc456defghijklmnopqrstu")

    def test_edge_case22(self):
        self.assertEqual(remove_splchar("123abc456defghijklmnopqrstuv"), "123abc456defghijklmnopqrstuv")

    def test_edge_case23(self):
        self.assertEqual(remove_splchar("123abc456defghijklmnopqrstuva"), "123abc456defghijklmnopqrstuva")

    def test_edge_case24(self):
        self.assertEqual(remove_splchar("123abc456defghijklmnopqrstuvab"), "123abc456defghijklmnopqrstuvab")

    def test_edge_case25(self):
        self.assertEqual(remove_splchar("123abc456defghijklmnopqrstuvaab"), "123abc456defghijklmnopqrstuvaab")

    def test_edge_case26(self):
        self.assertEqual(remove_splchar("123abc456defghijklmnopqrstuvabc"), "123abc456defghijklmnopqrstuvabc")

    def test_edge_case27(self):
        self.assertEqual(remove_splchar("123abc456defghijklmnopqrstuvaabc"), "123abc456defghijklmnopqrstuvaabc")

    def test_edge_case28(self):
        self.assertEqual(remove_splchar("123abc456defghijklmnopqrstuvabcd"), "123abc456defghijklmnopqrstuvabcd")

    def test_edge_case29(self):
        self.assertEqual(remove_splchar("123abc456defghijklmnopqrstuvaabcd"), "123abc456defghijklmnopqrstuvaabcd")

    def test_edge_case30(self):
        self.assertEqual(remove_splchar("123abc456defghijklmnopqrstuvabcde"), "123abc456defghijklmnopqrstuvabcde")

    def
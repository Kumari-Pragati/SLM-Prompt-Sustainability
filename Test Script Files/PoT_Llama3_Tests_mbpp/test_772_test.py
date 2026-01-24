import unittest
from mbpp_772_code import remove_length

class TestRemoveLength(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(remove_length("Hello World", 5), "Hello World")

    def test_edge1(self):
        self.assertEqual(remove_length("Hello", 5), "Hello")

    def test_edge2(self):
        self.assertEqual(remove_length("Hello", 3), "Hello")

    def test_edge3(self):
        self.assertEqual(remove_length("Hello", 1), "Hello")

    def test_edge4(self):
        self.assertEqual(remove_length("Hello", 6), "")

    def test_edge5(self):
        self.assertEqual(remove_length("", 5), "")

    def test_edge6(self):
        self.assertEqual(remove_length("Hello", 0), "Hello")

    def test_edge7(self):
        self.assertEqual(remove_length("Hello", 7), "")

    def test_edge8(self):
        self.assertEqual(remove_length("Hello", 3), "Hello")

    def test_edge9(self):
        self.assertEqual(remove_length("Hello", 5), "Hello")

    def test_edge10(self):
        self.assertEqual(remove_length("Hello", 6), "")

    def test_edge11(self):
        self.assertEqual(remove_length("Hello", 7), "")

    def test_edge12(self):
        self.assertEqual(remove_length("Hello", 8), "")

    def test_edge13(self):
        self.assertEqual(remove_length("Hello", 9), "")

    def test_edge14(self):
        self.assertEqual(remove_length("Hello", 10), "")

    def test_edge15(self):
        self.assertEqual(remove_length("Hello", 11), "")

    def test_edge16(self):
        self.assertEqual(remove_length("Hello", 12), "")

    def test_edge17(self):
        self.assertEqual(remove_length("Hello", 13), "")

    def test_edge18(self):
        self.assertEqual(remove_length("Hello", 14), "")

    def test_edge19(self):
        self.assertEqual(remove_length("Hello", 15), "")

    def test_edge20(self):
        self.assertEqual(remove_length("Hello", 16), "")

    def test_edge21(self):
        self.assertEqual(remove_length("Hello", 17), "")

    def test_edge22(self):
        self.assertEqual(remove_length("Hello", 18), "")

    def test_edge23(self):
        self.assertEqual(remove_length("Hello", 19), "")

    def test_edge24(self):
        self.assertEqual(remove_length("Hello", 20), "")

    def test_edge25(self):
        self.assertEqual(remove_length("Hello", 21), "")

    def test_edge26(self):
        self.assertEqual(remove_length("Hello", 22), "")

    def test_edge27(self):
        self.assertEqual(remove_length("Hello", 23), "")

    def test_edge28(self):
        self.assertEqual(remove_length("Hello", 24), "")

    def test_edge29(self):
        self.assertEqual(remove_length("Hello", 25), "")

    def test_edge30(self):
        self.assertEqual(remove_length("Hello", 26), "")

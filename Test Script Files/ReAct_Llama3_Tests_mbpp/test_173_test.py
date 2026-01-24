import unittest
from mbpp_173_code import remove_splchar

class TestRemoveSplchar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_splchar("Hello, World!"), "Hello World")

    def test_edge_case1(self):
        self.assertEqual(remove_splchar("Hello_World"), "Hello World")

    def test_edge_case2(self):
        self.assertEqual(remove_splchar("Hello*World"), "Hello World")

    def test_edge_case3(self):
        self.assertEqual(remove_splchar("Hello-World"), "Hello World")

    def test_edge_case4(self):
        self.assertEqual(remove_splchar("Hello World!"), "Hello World")

    def test_edge_case5(self):
        self.assertEqual(remove_splchar("Hello World"), "Hello World")

    def test_edge_case6(self):
        self.assertEqual(remove_splchar("Hello"), "Hello")

    def test_edge_case7(self):
        self.assertEqual(remove_splchar(""), "")

    def test_edge_case8(self):
        self.assertEqual(remove_splchar("Hello World!"), "Hello World")

    def test_edge_case9(self):
        self.assertEqual(remove_splchar("Hello World!"), "Hello World")

    def test_edge_case10(self):
        self.assertEqual(remove_splchar("Hello World!"), "Hello World")

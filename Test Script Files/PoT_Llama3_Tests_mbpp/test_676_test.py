import unittest
from mbpp_676_code import remove_extra_char

class TestRemoveExtraChar(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_extra_char("Hello World"), "HelloWorld")

    def test_edge_case(self):
        self.assertEqual(remove_extra_char("Hello_World"), "HelloWorld")

    def test_edge_case2(self):
        self.assertEqual(remove_extra_char("Hello!World"), "HelloWorld")

    def test_edge_case3(self):
        self.assertEqual(remove_extra_char("Hello World!"), "HelloWorld")

    def test_edge_case4(self):
        self.assertEqual(remove_extra_char("Hello,World"), "HelloWorld")

    def test_edge_case5(self):
        self.assertEqual(remove_extra_char("Hello-World"), "HelloWorld")

    def test_edge_case6(self):
        self.assertEqual(remove_extra_char("Hello World"), "HelloWorld")

    def test_edge_case7(self):
        self.assertEqual(remove_extra_char("Hello"), "Hello")

    def test_edge_case8(self):
        self.assertEqual(remove_extra_char("World"), "World")

    def test_edge_case9(self):
        self.assertEqual(remove_extra_char("HelloWorld"), "HelloWorld")

    def test_edge_case10(self):
        self.assertEqual(remove_extra_char("Hello World World"), "HelloWorldWorld")

import unittest
from mbpp_474_code import replace_char

class TestReplaceChar(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(replace_char("Hello World", "o", "o"), "Hello World")

    def test_edge_case(self):
        self.assertEqual(replace_char("Hello World", "o", ""), "Hello World")

    def test_edge_case2(self):
        self.assertEqual(replace_char("Hello World", "", "o"), "Hello World")

    def test_edge_case3(self):
        self.assertEqual(replace_char("Hello World", "o", "o"), "Hello World")

    def test_edge_case4(self):
        self.assertEqual(replace_char("Hello World", "o", "o"), "Hello World")

    def test_edge_case5(self):
        self.assertEqual(replace_char("Hello World", "o", "o"), "Hello World")

    def test_edge_case6(self):
        self.assertEqual(replace_char("Hello World", "o", "o"), "Hello World")

    def test_edge_case7(self):
        self.assertEqual(replace_char("Hello World", "o", "o"), "Hello World")

    def test_edge_case8(self):
        self.assertEqual(replace_char("Hello World", "o", "o"), "Hello World")

    def test_edge_case9(self):
        self.assertEqual(replace_char("Hello World", "o", "o"), "Hello World")

    def test_edge_case10(self):
        self.assertEqual(replace_char("Hello World", "o", "o"), "Hello World")

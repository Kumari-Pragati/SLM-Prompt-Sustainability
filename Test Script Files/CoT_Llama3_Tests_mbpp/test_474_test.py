import unittest
from mbpp_474_code import replace_char

class TestReplaceChar(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(replace_char("Hello, World!", ",", "."), "Hello.. World!")

    def test_edge_case(self):
        self.assertEqual(replace_char("", "a", "b"), "")

    def test_edge_case2(self):
        self.assertEqual(replace_char("abc", "a", "b"), "bc")

    def test_edge_case3(self):
        self.assertEqual(replace_char("abc", "a", "a"), "abc")

    def test_edge_case4(self):
        self.assertEqual(replace_char("abc", "b", "b"), "abc")

    def test_edge_case5(self):
        self.assertEqual(replace_char("abc", "c", "c"), "abc")

    def test_edge_case6(self):
        self.assertEqual(replace_char("abc", "d", "d"), "abc")

    def test_edge_case7(self):
        self.assertEqual(replace_char("abc", "a", "z"), "bzc")

    def test_edge_case8(self):
        self.assertEqual(replace_char("abc", "b", "z"), "acz")

    def test_edge_case9(self):
        self.assertEqual(replace_char("abc", "c", "z"), "abz")

    def test_edge_case10(self):
        self.assertEqual(replace_char("abc", "d", "z"), "abc")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            replace_char(123, "a", "b")

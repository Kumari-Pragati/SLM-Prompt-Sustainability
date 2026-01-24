import unittest
from mbpp_178_code import string_literals

class TestStringLiterals(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world'), 'Matched!')

    def test_edge_case(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello'), 'Matched!')

    def test_edge_case2(self):
        self.assertEqual(string_literals(['hello', 'world'], 'world'), 'Matched!')

    def test_edge_case3(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world hello'), 'Matched!')

    def test_edge_case4(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world world'), 'Matched!')

    def test_edge_case5(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world world hello'), 'Matched!')

    def test_edge_case6(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world world world'), 'Matched!')

    def test_edge_case7(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world world world hello'), 'Matched!')

    def test_edge_case8(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world world world world',), 'Matched!')

    def test_edge_case9(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world world world world hello',), 'Matched!')

    def test_edge_case10(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world world world world world',), 'Matched!')

    def test_edge_case11(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world world world world world hello',), 'Matched!')

    def test_edge_case12(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world world world world world world',), 'Matched!')

    def test_edge_case13(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world world world world world world hello',), 'Matched!')

    def test_edge_case14(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world world world world world world world',), 'Matched!')

    def test_edge_case15(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world world world world world world world hello',), 'Matched!')

    def test_edge_case16(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world world world world world world world world',), 'Matched!')

    def test_edge_case17(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world world world world world world world world hello',), 'Matched!')

    def test_edge_case18(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world world world world world world world world world',), 'Matched!')

    def test_edge_case19(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world world world world world world world world world hello',), 'Matched!')

    def test_edge_case20(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world world world world world world world world world world',), 'Matched!')

    def test_edge_case21(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world world world world world world world world world world hello',), 'Matched!')

    def test_edge_case22(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world world world world world world world world world world world',), 'Matched!')

    def test_edge_case23(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world world world world world world world world world world world hello',), 'Matched!')

    def test_edge_case24(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world world world world world world world world world world world world',), 'Matched!')

    def test_edge_case25(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world world world world world world world world world world world world hello',), 'Matched!')

    def test_edge_case26(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world world world world world world world world world world world world world',), 'Matched!')

    def test_edge_case27(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world world world world world world world world world world world world world world',), 'Matched!')

    def test_edge_case28(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello world world world world world world world world world world world world world world world',), 'Matched!')

    def test_edge_case29(self):
        self.assertEqual(string_literals(['hello', 'world'], 'hello
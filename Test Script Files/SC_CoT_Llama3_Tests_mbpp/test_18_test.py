import unittest
from mbpp_18_code import remove_dirty_chars

class TestRemoveDirtyChars(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(remove_dirty_chars('Hello, World!', 'Hello'), 'Hello')

    def test_edge_case(self):
        self.assertEqual(remove_dirty_chars('Hello, World!', 'World'), 'World')

    def test_edge_case2(self):
        self.assertEqual(remove_dirty_chars('Hello, World!', 'H'), 'H')

    def test_edge_case3(self):
        self.assertEqual(remove_dirty_chars('Hello, World!', 'W'), 'W')

    def test_edge_case4(self):
        self.assertEqual(remove_dirty_chars('Hello, World!', 'o'), 'o')

    def test_edge_case5(self):
        self.assertEqual(remove_dirty_chars('Hello, World!', 'l'), 'l')

    def test_edge_case6(self):
        self.assertEqual(remove_dirty_chars('Hello, World!', 'o,'), 'o,')

    def test_edge_case7(self):
        self.assertEqual(remove_dirty_chars('Hello, World!', 'o, W'), 'o, W')

    def test_edge_case8(self):
        self.assertEqual(remove_dirty_chars('Hello, World!', 'o, W, l'), 'o, W, l')

    def test_edge_case9(self):
        self.assertEqual(remove_dirty_chars('Hello, World!', 'o, W, l, o'), 'o, W, l, o')

    def test_edge_case10(self):
        self.assertEqual(remove_dirty_chars('Hello, World!', 'o, W, l, o, H'), 'o, W, l, o, H')

    def test_edge_case11(self):
        self.assertEqual(remove_dirty_chars('Hello, World!', 'o, W, l, o, H, W'), 'o, W, l, o, H, W')

    def test_edge_case12(self):
        self.assertEqual(remove_dirty_chars('Hello, World!', 'o, W, l, o, H, W, l'), 'o, W, l, o, H, W, l')

    def test_edge_case13(self):
        self.assertEqual(remove_dirty_chars('Hello, World!', 'o, W, l, o, H, W, l, o'), 'o, W, l, o, H, W, l, o')

    def test_edge_case14(self):
        self.assertEqual(remove_dirty_chars('Hello, World!', 'o, W, l, o, H, W, l, o, H'), 'o, W, l, o, H, W, l, o, H')

    def test_edge_case15(self):
        self.assertEqual(remove_dirty_chars('Hello, World!', 'o, W, l, o, H, W, l, o, H, W'), 'o, W, l, o, H, W, l, o, H, W')

    def test_edge_case16(self):
        self.assertEqual(remove_dirty_chars('Hello, World!', 'o, W, l, o, H, W, l, o, H, W, l'), 'o, W, l, o, H, W, l, o, H, W, l')

    def test_edge_case17(self):
        self.assertEqual(remove_dirty_chars('Hello, World!', 'o, W, l, o, H, W, l, o, H, W, l, o'), 'o, W, l, o, H, W, l, o, H, W, l, o')

    def test_edge_case18(self):
        self.assertEqual(remove_dirty_chars('Hello, World!', 'o, W, l, o, H, W, l, o, H, W, l, o, H'), 'o, W, l, o, H, W, l, o, H, W, l, o, H')

    def test_edge_case19(self):
        self.assertEqual(remove_dirty_chars('Hello, World!', 'o, W, l, o, H, W, l, o, H, W, l, o, H, W'), 'o, W, l, o, H, W, l, o, H, W, l, o, H, W')

    def test_edge_case20(self):
        self.assertEqual(remove_dirty_chars('Hello, World!', 'o, W, l, o, H, W, l, o, H, W, l, o, H, W, l'), 'o, W, l, o, H, W, l, o, H, W, l, o, H, W, l')

    def test_edge_case21(self):
        self.assertEqual(remove_dirty_chars('Hello, World!', 'o, W, l, o, H, W, l, o, H, W, l, o, H, W, l, o'), 'o, W, l
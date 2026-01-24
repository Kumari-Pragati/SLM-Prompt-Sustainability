import unittest
from mbpp_11_code import remove_Occ

class TestRemove_Occ(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_Occ("hello world", 'o'), "hell wrld")

    def test_edge_case1(self):
        self.assertEqual(remove_Occ("hello world", 'o'), "hell wrld")

    def test_edge_case2(self):
        self.assertEqual(remove_Occ("hello world", 'z'), "hello world")

    def test_edge_case3(self):
        self.assertEqual(remove_Occ("hello world", 'x'), "hello world")

    def test_edge_case4(self):
        self.assertEqual(remove_Occ("hello world", 'h'), "")

    def test_edge_case5(self):
        self.assertEqual(remove_Occ("hello world", 'w'), "hello rld")

    def test_edge_case6(self):
        self.assertEqual(remove_Occ("hello world", 'l'), "heo wrd")

    def test_edge_case7(self):
        self.assertEqual(remove_Occ("hello world", 'o',), "hell wrld")

    def test_edge_case8(self):
        self.assertEqual(remove_Occ("hello world", 'o'), "hell wrld")

    def test_edge_case9(self):
        self.assertEqual(remove_Occ("hello world", 'o'), "hell wrld")

    def test_edge_case10(self):
        self.assertEqual(remove_Occ("hello world", 'o'), "hell wrld")

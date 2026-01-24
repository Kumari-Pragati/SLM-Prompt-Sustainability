import unittest
from mbpp_11_code import remove_Occ

class TestRemoveOcc(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(remove_Occ("hello world", 'o'), "hell wrld")

    def test_edge1(self):
        self.assertEqual(remove_Occ("hello world", 'o'), "hell wrld")

    def test_edge2(self):
        self.assertEqual(remove_Occ("hello world", 'z'), "hello world")

    def test_edge3(self):
        self.assertEqual(remove_Occ("hello world", 'x'), "hello world")

    def test_edge4(self):
        self.assertEqual(remove_Occ("hello world",''), "hello world")

    def test_edge5(self):
        self.assertEqual(remove_Occ("hello world", 'h'), "ello world")

    def test_edge6(self):
        self.assertEqual(remove_Occ("hello world", 'l'), "heo world")

    def test_edge7(self):
        self.assertEqual(remove_Occ("hello world", 'o',), "hell wrld")

    def test_edge8(self):
        self.assertEqual(remove_Occ("hello world", 'o',), "hell wrld")

    def test_edge9(self):
        self.assertEqual(remove_Occ("hello world", 'o'), "hell wrld")

    def test_edge10(self):
        self.assertEqual(remove_Occ("hello world", 'o'), "hell wrld")

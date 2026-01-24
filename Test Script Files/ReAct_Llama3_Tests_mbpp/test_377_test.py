import unittest
from mbpp_377_code import remove_Char

class TestRemoveChar(unittest.TestCase):

    def test_remove_Char_typical(self):
        self.assertEqual(remove_Char("hello world", 'o'), "hell wrld")

    def test_remove_Char_edge1(self):
        self.assertEqual(remove_Char("hello world", 'l'), "hwo rd")

    def test_remove_Char_edge2(self):
        self.assertEqual(remove_Char("hello world", 'z'), "hello world")

    def test_remove_Char_edge3(self):
        self.assertEqual(remove_Char("hello world", 'x'), "hello world")

    def test_remove_Char_edge4(self):
        self.assertEqual(remove_Char("hello world",''), "helloworld")

    def test_remove_Char_edge5(self):
        self.assertEqual(remove_Char("hello world", 'h'), "ello wrld")

    def test_remove_Char_edge6(self):
        self.assertEqual(remove_Char("hello world", 'w'), "heloorld")

    def test_remove_Char_edge7(self):
        self.assertEqual(remove_Char("hello world", 'o',), "hell wrld")

    def test_remove_Char_edge8(self):
        self.assertEqual(remove_Char("hello world", 'o'), "hell wrld")

    def test_remove_Char_edge9(self):
        self.assertEqual(remove_Char("hello world", 'o'), "hell wrld")

    def test_remove_Char_edge10(self):
        self.assertEqual(remove_Char("hello world", 'o'), "hell wrld")

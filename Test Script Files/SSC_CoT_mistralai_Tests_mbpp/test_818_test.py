import unittest
from mbpp_818_code import lower_ctr

class TestLowerCtr(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(lower_ctr("hello"), 5)
        self.assertEqual(lower_ctr("world"), 5)
        self.assertEqual(lower_ctr("Python"), 6)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(lower_ctr("A"), 1)
        self.assertEqual(lower_ctr("Z"), 1)
        self.assertEqual(lower_ctr("a"), 1)
        self.assertEqual(lower_ctr("z"), 1)
        self.assertEqual(lower_ctr(""), 0)
        self.assertEqual(lower_ctr("abcdefghijklmnopqrstuvwxyz"), 26)

    def test_special_input(self):
        self.assertEqual(lower_ctr("Hello World"), 10)
        self.assertEqual(lower_ctr("Python3"), 6)
        self.assertEqual(lower_ctr("12345"), 0)
        self.assertEqual(lower_ctr("Hello World!"), 10)
        self.assertEqual(lower_ctr("Hello_World"), 5)

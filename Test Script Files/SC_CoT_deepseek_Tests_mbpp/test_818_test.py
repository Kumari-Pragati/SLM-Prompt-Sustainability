import unittest
from mbpp_818_code import lower_ctr

class TestLowerCtr(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(lower_ctr("HelloWorld"), 2)

    def test_edge_case(self):
        self.assertEqual(lower_ctr(""), 0)

    def test_corner_case(self):
        self.assertEqual(lower_ctr("12345"), 0)
        self.assertEqual(lower_ctr("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 0)
        self.assertEqual(lower_ctr("abcdefghijklmnopqrstuvwxyz"), 26)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            lower_ctr(12345)

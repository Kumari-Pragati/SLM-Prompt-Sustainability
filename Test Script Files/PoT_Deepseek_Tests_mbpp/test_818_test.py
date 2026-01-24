import unittest
from mbpp_818_code import lower_ctr

class TestLowerCtr(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(lower_ctr('HelloWorld'), 2)
        self.assertEqual(lower_ctr('hElLO'), 2)
        self.assertEqual(lower_ctr('123'), 0)
        self.assertEqual(lower_ctr(''), 0)

    def test_edge_cases(self):
        self.assertEqual(lower_ctr('a'), 1)
        self.assertEqual(lower_ctr('A'), 0)
        self.assertEqual(lower_ctr('0a'), 1)
        self.assertEqual(lower_ctr('0A'), 0)

    def test_corner_cases(self):
        self.assertEqual(lower_ctr('abcdefghijklmnopqrstuvwxyz'), 26)
        self.assertEqual(lower_ctr('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 0)
        self.assertEqual(lower_ctr('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'), 26)

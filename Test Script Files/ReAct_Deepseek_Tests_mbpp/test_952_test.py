import unittest
from mbpp_952_code import nCr_mod_p

class TestNCRModP(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(nCr_mod_p(5, 2, 13), 6)
        self.assertEqual(nCr_mod_p(10, 5, 29), 28)
        self.assertEqual(nCr_mod_p(15, 8, 101), 22)

    def test_edge_cases(self):
        self.assertEqual(nCr_mod_p(0, 0, 17), 1)
        self.assertEqual(nCr_mod_p(1, 0, 23), 1)
        self.assertEqual(nCr_mod_p(2, 1, 31), 2)

    def test_error_cases(self):
        with self.assertRaises(Exception):
            nCr_mod_p(-1, 2, 11)
        with self.assertRaises(Exception):
            nCr_mod_p(5, -3, 19)
        with self.assertRaises(Exception):
            nCr_mod_p(4, 5, 7)

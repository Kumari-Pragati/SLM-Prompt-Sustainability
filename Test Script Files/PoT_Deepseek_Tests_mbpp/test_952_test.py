import unittest
from mbpp_952_code import nCr_mod_p

class TestNCRModP(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(nCr_mod_p(5, 2, 13), 10)
        self.assertEqual(nCr_mod_p(10, 5, 21), 1)
        self.assertEqual(nCr_mod_p(15, 10, 31), 26)

    def test_edge_cases(self):
        self.assertEqual(nCr_mod_p(0, 0, 17), 1)
        self.assertEqual(nCr_mod_p(1, 0, 23), 1)
        self.assertEqual(nCr_mod_p(2, 1, 37), 2)

    def test_boundary_cases(self):
        self.assertEqual(nCr_mod_p(10, 10, 101), 1)
        self.assertEqual(nCr_mod_p(20, 10, 103), 1)
        self.assertEqual(nCr_mod_p(30, 15, 107), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(Exception):
            nCr_mod_p(-5, 2, 13)
        with self.assertRaises(Exception):
            nCr_mod_p(5, -2, 13)
        with self.assertRaises(Exception):
            nCr_mod_p(5, 2, -13)
        with self.assertRaises(Exception):
            nCr_mod_p(5, 6, 13)

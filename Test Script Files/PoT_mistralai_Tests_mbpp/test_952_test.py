import unittest
from mbpp_952_code import nCr_mod_p

class TestNCRModP(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(nCr_mod_p(5, 2, 3), 2)
        self.assertEqual(nCr_mod_p(10, 3, 5), 8)
        self.assertEqual(nCr_mod_p(20, 10, 7), 6)

    def test_edge_cases(self):
        self.assertEqual(nCr_mod_p(0, 0, 2), 1)
        self.assertEqual(nCr_mod_p(1, 1, 2), 1)
        self.assertEqual(nCr_mod_p(100, 100, 101), 0)

    def test_boundary_cases(self):
        self.assertEqual(nCr_mod_p(2, 1, 2), 1)
        self.assertEqual(nCr_mod_p(2, 2, 2), 1)
        self.assertEqual(nCr_mod_p(3, 3, 2), 1)
        self.assertEqual(nCr_mod_p(4, 4, 2), 1)

    def test_negative_r(self):
        self.assertRaises(ValueError, nCr_mod_p, 5, -2, 3)

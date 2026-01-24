import unittest
from mbpp_952_code import nCr_mod_p

class TestNCRModP(unittest.TestCase):

    def test_nCr_mod_p_positive(self):
        self.assertEqual(nCr_mod_p(5, 2, 3), 2)
        self.assertEqual(nCr_mod_p(10, 5, 11), 5)
        self.assertEqual(nCr_mod_p(20, 10, 19), 10)

    def test_nCr_mod_p_zero(self):
        self.assertEqual(nCr_mod_p(0, 0, 7), 1)
        self.assertEqual(nCr_mod_p(1, 0, 7), 1)
        self.assertEqual(nCr_mod_p(5, 0, 7), 1)

    def test_nCr_mod_p_negative(self):
        self.assertEqual(nCr_mod_p(-1, 1, 3), 0)
        self.assertEqual(nCr_mod_p(0, -1, 3), 0)
        self.assertEqual(nCr_mod_p(1, -1, 3), 0)

    def test_nCr_mod_p_large_input(self):
        self.assertEqual(nCr_mod_p(100, 50, 101), 50)

    def test_nCr_mod_p_r_gt_n(self):
        self.assertEqual(nCr_mod_p(5, 6, 3), 2)
        self.assertEqual(nCr_mod_p(10, 11, 11), 1)

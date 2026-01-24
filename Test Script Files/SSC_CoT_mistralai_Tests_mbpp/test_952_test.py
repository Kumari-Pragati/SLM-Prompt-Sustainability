import unittest
from mbpp_952_code import nCr_mod_p

class TestNCRModP(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(nCr_mod_p(5, 2, 3), 2)
        self.assertEqual(nCr_mod_p(10, 3, 5), 4)
        self.assertEqual(nCr_mod_p(20, 10, 7), 6)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(nCr_mod_p(0, 0, 2), 1)
        self.assertEqual(nCr_mod_p(1, 0, 2), 0)
        self.assertEqual(nCr_mod_p(1, 1, 2), 1)
        self.assertEqual(nCr_mod_p(2, 2, 2), 0)
        self.assertEqual(nCr_mod_p(3, 3, 3), 1)
        self.assertEqual(nCr_mod_p(4, 4, 4), 1)
        self.assertEqual(nCr_mod_p(5, 5, 5), 1)

    def test_negative_input(self):
        self.assertRaises(ValueError, nCr_mod_p, -1, 2, 3)
        self.assertRaises(ValueError, nCr_mod_p, 1, -2, 3)

    def test_zero_input(self):
        self.assertRaises(ValueError, nCr_mod_p, 0, 0, 0)
        self.assertRaises(ValueError, nCr_mod_p, 0, 1, 0)

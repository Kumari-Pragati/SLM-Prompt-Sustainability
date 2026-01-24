import unittest
from mbpp_952_code import nCr_mod_p

class TestNCRModP(unittest.TestCase):
    def test_nCr_mod_p_typical_case(self):
        self.assertEqual(nCr_mod_p(5, 2, 3), 2)
        self.assertEqual(nCr_mod_p(10, 3, 5), 8)
        self.assertEqual(nCr_mod_p(20, 10, 7), 6)

    def test_nCr_mod_p_edge_cases(self):
        self.assertEqual(nCr_mod_p(0, 0, 11), 1)
        self.assertEqual(nCr_mod_p(1, 1, 11), 1)
        self.assertEqual(nCr_mod_p(10, 10, 11), 1)
        self.assertEqual(nCr_mod_p(1, 10, 11), 0)
        self.assertEqual(nCr_mod_p(0, 10, 11), 0)

    def test_nCr_mod_p_boundary_conditions(self):
        self.assertEqual(nCr_mod_p(1, 0, 11), 1)
        self.assertEqual(nCr_mod_p(1, -1, 11), 0)
        self.assertEqual(nCr_mod_p(-1, 1, 11), 0)
        self.assertEqual(nCr_mod_p(-1, -1, 11), 0)

    def test_nCr_mod_p_invalid_inputs(self):
        self.assertRaises(ValueError, nCr_mod_p, -2, 2, 11)
        self.assertRaises(ValueError, nCr_mod_p, 0, -2, 11)
        self.assertRaises(ValueError, nCr_mod_p, 0, 0, 0)

import unittest
from mbpp_952_code import nCr_mod_p

class TestNCRModP(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(nCr_mod_p(2, 1, 3), 2)
        self.assertEqual(nCr_mod_p(3, 2, 5), 2)
        self.assertEqual(nCr_mod_p(4, 3, 7), 4)

    def test_edge_cases(self):
        self.assertEqual(nCr_mod_p(0, 0, 2), 1)
        self.assertEqual(nCr_mod_p(1, 0, 2), 1)
        self.assertEqual(nCr_mod_p(1, 1, 2), 1)
        self.assertEqual(nCr_mod_p(2, 2, 2), 0)
        self.assertEqual(nCr_mod_p(3, 3, 3), 1)

    def test_boundary_conditions(self):
        self.assertEqual(nCr_mod_p(100, 100, 101), 1)
        self.assertEqual(nCr_mod_p(100, 99, 101), 100)
        self.assertEqual(nCr_mod_p(100, 1, 101), 100)
        self.assertEqual(nCr_mod_p(100, 100, 2), 0)

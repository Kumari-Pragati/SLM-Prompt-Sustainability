import unittest
from mbpp_952_code import nCr_mod_p

class TestNCRModP(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(nCr_mod_p(5, 2, 13), 10)

    def test_boundary_case(self):
        self.assertEqual(nCr_mod_p(0, 0, 13), 1)
        self.assertEqual(nCr_mod_p(1, 0, 13), 1)
        self.assertEqual(nCr_mod_p(1, 1, 13), 1)

    def test_edge_case(self):
        self.assertEqual(nCr_mod_p(10, 5, 13), 1)
        self.assertEqual(nCr_mod_p(10, 10, 13), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            nCr_mod_p('a', 2, 13)
        with self.assertRaises(TypeError):
            nCr_mod_p(5, 'b', 13)
        with self.assertRaises(TypeError):
            nCr_mod_p(5, 2, 'c')
        with self.assertRaises(ValueError):
            nCr_mod_p(5, 6, 13)
        with self.assertRaises(ValueError):
            nCr_mod_p(-1, 2, 13)
        with self.assertRaises(ValueError):
            nCr_mod_p(5, -2, 13)
        with self.assertRaises(ValueError):
            nCr_mod_p(5, 2, -13)

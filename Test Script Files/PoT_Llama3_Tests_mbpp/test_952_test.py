import unittest
from mbpp_952_code import nCr_mod_p

class TestNcrModP(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(nCr_mod_p(5, 2, 7), 6)

    def test_edge_case(self):
        self.assertEqual(nCr_mod_p(5, 5, 7), 1)

    def test_boundary_case(self):
        self.assertEqual(nCr_mod_p(5, 0, 7), 1)
        self.assertEqual(nCr_mod_p(5, 5, 7), 1)
        self.assertEqual(nCr_mod_p(5, 1, 7), 5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            nCr_mod_p('a', 2, 7)

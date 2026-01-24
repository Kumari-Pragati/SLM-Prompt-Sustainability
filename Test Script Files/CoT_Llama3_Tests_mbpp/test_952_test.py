import unittest
from mbpp_952_code import nCr_mod_p

class TestNcrModP(unittest.TestCase):

    def test_nCr_mod_p_typical(self):
        self.assertEqual(nCr_mod_p(10, 3, 7), 10)

    def test_nCr_mod_p_edge(self):
        self.assertEqual(nCr_mod_p(10, 10, 7), 1)

    def test_nCr_mod_p_boundary(self):
        self.assertEqual(nCr_mod_p(10, 0, 7), 1)

    def test_nCr_mod_p_invalid_input(self):
        with self.assertRaises(TypeError):
            nCr_mod_p('a', 3, 7)

    def test_nCr_mod_p_invalid_input2(self):
        with self.assertRaises(TypeError):
            nCr_mod_p(10, 'b', 7)

    def test_nCr_mod_p_invalid_input3(self):
        with self.assertRaises(TypeError):
            nCr_mod_p(10, 3, 'c')

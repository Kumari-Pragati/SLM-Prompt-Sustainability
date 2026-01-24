import unittest
from mbpp_952_code import nCr_mod_p

class TestNcrModP(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(nCr_mod_p(5, 2, 7), 6)

    def test_edge_case(self):
        self.assertEqual(nCr_mod_p(5, 5, 7), 1)

    def test_edge_case2(self):
        self.assertEqual(nCr_mod_p(5, 0, 7), 1)

    def test_edge_case3(self):
        self.assertEqual(nCr_mod_p(5, 6, 7), 0)

    def test_edge_case4(self):
        self.assertEqual(nCr_mod_p(5, 1, 7), 5)

    def test_edge_case5(self):
        self.assertEqual(nCr_mod_p(5, 5, 1), 1)

    def test_edge_case6(self):
        self.assertEqual(nCr_mod_p(5, 0, 1), 1)

    def test_edge_case7(self):
        self.assertEqual(nCr_mod_p(5, 6, 1), 0)

    def test_edge_case8(self):
        self.assertEqual(nCr_mod_p(5, 1, 1), 5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            nCr_mod_p('a', 2, 7)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            nCr_mod_p(5, 'b', 7)

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            nCr_mod_p(5, 2, 'c')

    def test_invalid_input4(self):
        with self.assertRaises(TypeError):
            nCr_mod_p('a', 'b', 'c')

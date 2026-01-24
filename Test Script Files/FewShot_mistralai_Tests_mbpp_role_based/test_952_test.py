import unittest
from mbpp_952_code import nCr_mod_p

class TestnCr_mod_p(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(nCr_mod_p(5, 2, 3), 2)
        self.assertEqual(nCr_mod_p(10, 5, 7), 3)
        self.assertEqual(nCr_mod_p(20, 10, 11), 5)

    def test_edge_cases(self):
        self.assertEqual(nCr_mod_p(0, 0, 2), 1)
        self.assertEqual(nCr_mod_p(1, 0, 2), 0)
        self.assertEqual(nCr_mod_p(1, 1, 2), 1)

    def test_boundary_cases(self):
        self.assertEqual(nCr_mod_p(1, 1, 1), 1)
        self.assertEqual(nCr_mod_p(2, 2, 2), 1)
        self.assertEqual(nCr_mod_p(3, 3, 3), 1)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            nCr_mod_p(-1, 2, 3)

    def test_zero_input(self):
        with self.assertRaises(ValueError):
            nCr_mod_p(0, 0, 0)

    def test_invalid_p(self):
        with self.assertRaises(ValueError):
            nCr_mod_p(5, 2, 0)

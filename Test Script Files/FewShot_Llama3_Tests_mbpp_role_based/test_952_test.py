import unittest
from mbpp_952_code import nCr_mod_p

class TestNcrModP(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(nCr_mod_p(10, 3, 7), 21)

    def test_edge_case_n_equal_r(self):
        self.assertEqual(nCr_mod_p(5, 5, 11), 1)

    def test_edge_case_r_greater_than_n(self):
        self.assertEqual(nCr_mod_p(10, 15, 13), 0)

    def test_edge_case_p_equal_to_2(self):
        self.assertEqual(nCr_mod_p(10, 3, 2), 3)

    def test_invalid_input_n_negative(self):
        with self.assertRaises(ValueError):
            nCr_mod_p(-5, 3, 7)

    def test_invalid_input_r_negative(self):
        with self.assertRaises(ValueError):
            nCr_mod_p(10, -3, 7)

    def test_invalid_input_p_negative(self):
        with self.assertRaises(ValueError):
            nCr_mod_p(10, 3, -7)

import unittest
from mbpp_402_code import ncr_modp

class TestNcrModp(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(ncr_modp(10, 3, 7), 35)

    def test_edge_case_n_zero(self):
        self.assertEqual(ncr_modp(0, 0, 7), 1)

    def test_edge_case_r_zero(self):
        self.assertEqual(ncr_modp(10, 0, 7), 1)

    def test_edge_case_p_one(self):
        self.assertEqual(ncr_modp(10, 3, 1), 6)

    def test_edge_case_p_large(self):
        self.assertEqual(ncr_modp(10, 3, 1000), 35)

    def test_invalid_input_type_n(self):
        with self.assertRaises(TypeError):
            ncr_modp("a", 3, 7)

    def test_invalid_input_type_r(self):
        with self.assertRaises(TypeError):
            ncr_modp(10, "b", 7)

    def test_invalid_input_type_p(self):
        with self.assertRaises(TypeError):
            ncr_modp(10, 3, "c")

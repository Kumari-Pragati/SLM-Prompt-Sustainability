import unittest
from mbpp_334_code import check_Validity

class TestCheckValidity(unittest.TestCase):
    def test_typical_valid(self):
        self.assertTrue(check_Validity(1, 2, 3))

    def test_typical_invalid(self):
        self.assertFalse(check_Validity(1, 2, 1))

    def test_edge_a_b_c_equal(self):
        self.assertFalse(check_Validity(1, 1, 1))

    def test_edge_a_b_c_close(self):
        self.assertFalse(check_Validity(1, 2, 2))

    def test_edge_a_b_c_far(self):
        self.assertTrue(check_Validity(1, 2, 3))

    def test_edge_b_c_a_equal(self):
        self.assertFalse(check_Validity(1, 1, 1))

    def test_edge_b_c_a_close(self):
        self.assertFalse(check_Validity(1, 2, 2))

    def test_edge_b_c_a_far(self):
        self.assertTrue(check_Validity(1, 2, 3))

    def test_edge_c_a_b_equal(self):
        self.assertFalse(check_Validity(1, 1, 1))

    def test_edge_c_a_b_close(self):
        self.assertFalse(check_Validity(1, 2, 2))

    def test_edge_c_a_b_far(self):
        self.assertTrue(check_Validity(1, 2, 3))

    def test_edge_a_b_zero(self):
        self.assertFalse(check_Validity(0, 0, 1))

    def test_edge_b_c_zero(self):
        self.assertFalse(check_Validity(0, 1, 0))

    def test_edge_c_a_zero(self):
        self.assertFalse(check_Validity(1, 0, 0))

    def test_edge_a_b_c_negative(self):
        self.assertFalse(check_Validity(-1, -2, -3))

    def test_edge_b_c_a_negative(self):
        self.assertFalse(check_Validity(-1, -2, -3))

    def test_edge_c_a_b_negative(self):
        self.assertFalse(check_Validity(-1, -2, -3))

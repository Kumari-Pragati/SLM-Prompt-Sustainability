import unittest
from mbpp_354_code import tn_ap

class TestTnAp(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(tn_ap(2, 5, 1), 12)

    def test_edge_case_n_zero(self):
        self.assertEqual(tn_ap(2, 0, 1), 2)

    def test_edge_case_d_zero(self):
        self.assertEqual(tn_ap(2, 5, 0), 2)

    def test_edge_case_a_zero(self):
        self.assertEqual(tn_ap(0, 5, 1), 5)

    def test_edge_case_n_negative(self):
        self.assertEqual(tn_ap(2, -5, 1), 2)

    def test_edge_case_d_negative(self):
        self.assertEqual(tn_ap(2, 5, -1), 2)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            tn_ap('a', 5, 1)

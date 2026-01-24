import unittest
from mbpp_354_code import tn_ap

class TestTnAp(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(tn_ap(1, 5, 2), 7)

    def test_edge_case_n_zero(self):
        self.assertEqual(tn_ap(1, 0, 2), 1)

    def test_edge_case_d_zero(self):
        self.assertEqual(tn_ap(1, 5, 0), 1)

    def test_edge_case_a_zero(self):
        self.assertEqual(tn_ap(0, 5, 2), 2)

    def test_edge_case_n_one(self):
        self.assertEqual(tn_ap(1, 1, 2), 1)

    def test_edge_case_d_one(self):
        self.assertEqual(tn_ap(1, 5, 1), 6)

    def test_edge_case_a_one(self):
        self.assertEqual(tn_ap(1, 5, 2), 7)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            tn_ap('a', 5, 2)

    def test_invalid_input_value(self):
        with self.assertRaises(TypeError):
            tn_ap(1, 'a', 2)

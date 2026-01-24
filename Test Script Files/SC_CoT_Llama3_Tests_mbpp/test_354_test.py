import unittest
from mbpp_354_code import tn_ap

class TestTnAp(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(tn_ap(2, 4, 1), 7)

    def test_edge_case_n_zero(self):
        self.assertEqual(tn_ap(2, 0, 1), 2)

    def test_edge_case_d_zero(self):
        self.assertEqual(tn_ap(2, 4, 0), 2)

    def test_edge_case_n_one(self):
        self.assertEqual(tn_ap(2, 1, 1), 3)

    def test_special_case_n_negative(self):
        with self.assertRaises(TypeError):
            tn_ap(2, -1, 1)

    def test_special_case_d_negative(self):
        with self.assertRaises(TypeError):
            tn_ap(2, 4, -1)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            tn_ap('a', 4, 1)

    def test_invalid_input_non_integer_n(self):
        with self.assertRaises(TypeError):
            tn_ap(2, 'a', 1)

    def test_invalid_input_non_integer_d(self):
        with self.assertRaises(TypeError):
            tn_ap(2, 4, 'a')

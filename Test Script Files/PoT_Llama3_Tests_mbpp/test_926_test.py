import unittest
from mbpp_926_code import rencontres_number

class TestRencontresNumber(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rencontres_number(3, 1), 2)

    def test_edge_case_zero_m(self):
        self.assertEqual(rencontres_number(3, 0), 1)

    def test_edge_case_zero_n(self):
        self.assertEqual(rencontres_number(0, 0), 1)

    def test_edge_case_one_n(self):
        self.assertEqual(rencontres_number(1, 0), 0)

    def test_edge_case_zero_n_and_m(self):
        self.assertEqual(rencontres_number(0, 1), 0)

    def test_edge_case_negative_n(self):
        with self.assertRaises(ValueError):
            rencontres_number(-1, 1)

    def test_edge_case_negative_m(self):
        with self.assertRaises(ValueError):
            rencontres_number(1, -1)

    def test_edge_case_large_n(self):
        self.assertEqual(rencontres_number(100, 50), 0)

    def test_edge_case_large_m(self):
        self.assertEqual(rencontres_number(100, 50), 0)

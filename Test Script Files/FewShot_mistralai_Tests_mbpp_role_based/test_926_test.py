import unittest
from mbpp_926_code import rencontres_number

class TestRencontresNumber(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(rencontres_number(5, 3), 10)

    def test_edge_case_n_0_m_0(self):
        self.assertEqual(rencontres_number(0, 0), 1)

    def test_edge_case_n_1_m_0(self):
        self.assertEqual(rencontres_number(1, 0), 0)

    def test_edge_case_m_0(self):
        self.assertEqual(rencontres_number(5, 0), 4)

    def test_negative_n(self):
        self.assertRaises(ValueError, rencontres_number, -1, 2)

    def test_negative_m(self):
        self.assertRaises(ValueError, rencontres_number, 5, -2)

import unittest
from mbpp_402_code import ncr_modp

class TestNcrModp(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(ncr_modp(5, 2, 7), 6)

    def test_edge_case_n(self):
        self.assertEqual(ncr_modp(10, 2, 7), 10)

    def test_edge_case_r(self):
        self.assertEqual(ncr_modp(5, 0, 7), 1)

    def test_edge_case_p(self):
        self.assertEqual(ncr_modp(5, 2, 1), 6)

    def test_edge_case_n_and_r(self):
        self.assertEqual(ncr_modp(0, 0, 7), 1)

    def test_edge_case_n_and_p(self):
        self.assertEqual(ncr_modp(5, 2, 0), 0)

    def test_edge_case_r_and_p(self):
        self.assertEqual(ncr_modp(5, 0, 7), 1)

import unittest
from mbpp_637_code import noprofit_noloss

class TestNoprofitNoloss(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(noprofit_noloss(10, 10))

    def test_edge_case_1(self):
        self.assertFalse(noprofit_noloss(10, 9))

    def test_edge_case_2(self):
        self.assertFalse(noprofit_noloss(10, 11))

    def test_boundary_case_1(self):
        self.assertFalse(noprofit_noloss(0, 0))

    def test_boundary_case_2(self):
        self.assertTrue(noprofit_noloss(0, 1))

import unittest
from mbpp_637_code import noprofit_noloss

class TestNoProfitNoLoss(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(noprofit_noloss(100, 100))

    def test_edge_case_profit(self):
        self.assertFalse(noprofit_noloss(100, 200))

    def test_edge_case_loss(self):
        self.assertFalse(noprofit_noloss(200, 100))

    def test_boundary_case_zero_cost(self):
        self.assertTrue(noprofit_noloss(0, 0))

    def test_boundary_case_zero_sale(self):
        self.assertFalse(noprofit_noloss(100, 0))

    def test_boundary_case_negative_cost(self):
        self.assertFalse(noprofit_noloss(-100, 100))

    def test_boundary_case_negative_sale(self):
        self.assertFalse(noprofit_noloss(100, -100))

    def test_corner_case_negative_both(self):
        self.assertFalse(noprofit_noloss(-100, -100))

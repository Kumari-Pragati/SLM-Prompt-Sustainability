import unittest
from mbpp_637_code import noprofit_noloss

class TestNoProfitNoLoss(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(noprofit_noloss(100, 100))

    def test_edge_case_sale_equal_cost(self):
        self.assertTrue(noprofit_noloss(0, 0))
        self.assertTrue(noprofit_noloss(100, 100))

    def test_edge_case_sale_greater_cost(self):
        self.assertFalse(noprofit_noloss(100, 200))

    def test_edge_case_sale_less_cost(self):
        self.assertFalse(noprofit_noloss(200, 100))

    def test_negative_values(self):
        self.assertTrue(noprofit_noloss(-100, -100))
        self.assertFalse(noprofit_noloss(-100, 0))
        self.assertFalse(noprofit_noloss(0, -100))

    def test_large_numbers(self):
        self.assertTrue(noprofit_noloss(10**9, 10**9))
        self.assertFalse(noprofit_noloss(10**9, 2*10**9))

import unittest
from mbpp_637_code import noprofit_noloss

class TestNoprofitNoloss(unittest.TestCase):
    def test_equal_costs(self):
        self.assertTrue(noprofit_noloss(10, 10))
    def test_greater_costs(self):
        self.assertFalse(noprofit_noloss(10, 15))
    def test_less_costs(self):
        self.assertFalse(noprofit_noloss(15, 10))
    def test_zero_cost(self):
        self.assertTrue(noprofit_noloss(0, 0))
    def test_negative_costs(self):
        self.assertFalse(noprofit_noloss(-10, 10))
    def test_negative_sales(self):
        self.assertFalse(noprofit_noloss(10, -10))

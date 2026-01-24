import unittest
from mbpp_637_code import noprofit_noloss

class TestNoprofitNoLoss(unittest.TestCase):

    def test_same_values(self):
        """Test when actual_cost and sale_amount are equal"""
        self.assertTrue(noprofit_noloss(10, 10))

    def test_positive_values(self):
        """Test when actual_cost is greater than sale_amount"""
        self.assertFalse(noprofit_noloss(15, 10))

    def test_negative_values(self):
        """Test when actual_cost is less than sale_amount"""
        self.assertFalse(noprofit_noloss(5, 10))

    def test_zero_values(self):
        """Test when actual_cost and sale_amount are zero"""
        self.assertTrue(noprofit_noloss(0, 0))
        self.assertFalse(noprofit_noloss(0, 1))
        self.assertFalse(noprofit_noloss(1, 0))

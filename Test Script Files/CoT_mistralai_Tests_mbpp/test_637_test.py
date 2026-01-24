import unittest
from mbpp_637_code import noprofit_noloss

class TestNoprofitNoloss(unittest.TestCase):
    def test_same_values(self):
        self.assertTrue(noprofit_noloss(10, 10))

    def test_higher_sale_amount(self):
        self.assertFalse(noprofit_noloss(5, 10))

    def test_lower_sale_amount(self):
        self.assertFalse(noprofit_noloss(10, 5))

    def test_zero_values(self):
        self.assertFalse(noprofit_noloss(0, 0))

    def test_negative_values(self):
        self.assertRaises(ValueError, noprofit_noloss, -5, -5)

    def test_mixed_types(self):
        self.assertRaises(TypeError, noprofit_noloss, 5, "string")

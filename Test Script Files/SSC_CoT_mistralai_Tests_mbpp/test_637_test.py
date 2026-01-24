import unittest
from mbpp_637_code import noprofit_noloss

class TestNoprofitNoloss(unittest.TestCase):
    def test_normal(self):
        self.assertTrue(noprofit_noloss(10, 10))
        self.assertTrue(noprofit_noloss(5, 5))
        self.assertTrue(noprofit_noloss(0, 0))

    def test_edge_cases(self):
        self.assertFalse(noprofit_noloss(10, 11))
        self.assertFalse(noprofit_noloss(11, 10))
        self.assertFalse(noprofit_noloss(0, 1))
        self.assertFalse(noprofit_noloss(1, 0))

    def test_negative_numbers(self):
        self.assertFalse(noprofit_noloss(-10, -10))
        self.assertFalse(noprofit_noloss(-5, -5))
        self.assertFalse(noprofit_noloss(-0, -0))

    def test_zero_division(self):
        self.assertRaises(ZeroDivisionError, noprofit_noloss, 0, 0)

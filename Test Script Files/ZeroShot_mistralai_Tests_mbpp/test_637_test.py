import unittest
from mbpp_637_code import noprofit_noloss

class TestNoprofitNoLoss(unittest.TestCase):

    def test_same_values(self):
        self.assertTrue(noprofit_noloss(10, 10))

    def test_different_values(self):
        self.assertFalse(noprofit_noloss(10, 20))

    def test_zero_values(self):
        self.assertFalse(noprofit_noloss(0, 0))

    def test_negative_values(self):
        self.assertFalse(noprofit_noloss(-10, -10))

import unittest
from mbpp_637_code import noprofit_noloss

class TestNoProfitNoLoss(unittest.TestCase):

    def test_equal_values(self):
        self.assertTrue(noprofit_noloss(100, 100))

    def test_unequal_values(self):
        self.assertFalse(noprofit_noloss(100, 200))

    def test_negative_values(self):
        self.assertTrue(noprofit_noloss(-100, -100))

    def test_mixed_values(self):
        self.assertFalse(noprofit_noloss(-100, 100))

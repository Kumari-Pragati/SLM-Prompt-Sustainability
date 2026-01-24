import unittest

from mbpp_637_code import noprofit_noloss

class TestNoProfitNoLoss(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(noprofit_noloss(100, 100))

    def test_boundary_conditions(self):
        self.assertTrue(noprofit_noloss(0, 0))
        self.assertFalse(noprofit_noloss(100, 0))
        self.assertFalse(noprofit_noloss(0, 100))

    def test_edge_cases(self):
        self.assertTrue(noprofit_noloss(1, 1))
        self.assertFalse(noprofit_noloss(1, 2))
        self.assertFalse(noprofit_noloss(2, 1))

    def test_special_cases(self):
        self.assertTrue(noprofit_noloss(1000000000, 1000000000))
        self.assertFalse(noprofit_noloss(-100, 100))
        self.assertFalse(noprofit_noloss(100, -100))
        self.assertFalse(noprofit_noloss(-100, -100))

import unittest
from mbpp_637_code import noprofit_noloss

class TestNoprofitNoloss(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(noprofit_noloss(10, 10))
        self.assertFalse(noprofit_noloss(10, 20))

    def test_edge_cases(self):
        self.assertTrue(noprofit_noloss(0, 0))
        self.assertFalse(noprofit_noloss(0, 1))
        self.assertFalse(noprofit_noloss(1, 0))

    def test_complex_cases(self):
        self.assertFalse(noprofit_noloss(-10, 10))
        self.assertFalse(noprofit_noloss(10, -10))
        self.assertFalse(noprofit_noloss(10.5, 10))
        self.assertFalse(noprofit_noloss(10, 10.5))

import unittest
from mbpp_637_code import noprofit_noloss

class TestNoprofitNoloss(unittest.TestCase):

    def test_noprofit_noloss_true(self):
        self.assertTrue(noprofit_noloss(100,100))

    def test_noprofit_noloss_false(self):
        self.assertFalse(noprofit_noloss(100,50))

    def test_noprofit_noloss_equal(self):
        self.assertTrue(noprofit_noloss(100,100))

    def test_noprofit_noloss_not_equal(self):
        self.assertFalse(noprofit_noloss(100,200))

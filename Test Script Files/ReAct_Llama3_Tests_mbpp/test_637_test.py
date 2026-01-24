import unittest
from mbpp_637_code import noprofit_noloss

class TestNoprofitNoloss(unittest.TestCase):

    def test_profit(self):
        self.assertFalse(noprofit_noloss(10, 5))

    def test_loss(self):
        self.assertFalse(noprofit_noloss(5, 10))

    def test_noprofit_noloss(self):
        self.assertTrue(noprofit_noloss(10, 10))

    def test_noprofit_noloss_equal(self):
        self.assertTrue(noprofit_noloss(10, 10))

    def test_noprofit_noloss_negative(self):
        with self.assertRaises(TypeError):
            noprofit_noloss(-10, 10)

    def test_noprofit_noloss_non_integer(self):
        with self.assertRaises(TypeError):
            noprofit_noloss("10", 10)

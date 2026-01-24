import unittest
from mbpp_637_code import noprofit_noloss

class TestNoProfitNoLoss(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(noprofit_noloss(100, 100))

    def test_edge_case_profit(self):
        self.assertFalse(noprofit_noloss(100, 200))

    def test_edge_case_loss(self):
        self.assertFalse(noprofit_noloss(200, 100))

    def test_zero_cost(self):
        self.assertTrue(noprofit_noloss(0, 0))

    def test_negative_cost(self):
        self.assertFalse(noprofit_noloss(-100, 100))

    def test_negative_sale(self):
        self.assertFalse(noprofit_noloss(100, -100))

    def test_negative_both(self):
        self.assertFalse(noprofit_noloss(-100, -100))

    def test_non_integer_cost(self):
        with self.assertRaises(TypeError):
            noprofit_noloss(100.5, 100)

    def test_non_integer_sale(self):
        with self.assertRaises(TypeError):
            noprofit_noloss(100, 100.5)

    def test_non_integer_both(self):
        with self.assertRaises(TypeError):
            noprofit_noloss(100.5, 100.5)

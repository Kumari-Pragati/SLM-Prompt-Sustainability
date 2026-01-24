import unittest
from mbpp_637_code import noprofit_noloss

class TestNoprofitNoloss(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(noprofit_noloss(10, 10))

    def test_equal_cost(self):
        self.assertTrue(noprofit_noloss(10, 10))

    def test_greater_cost(self):
        self.assertFalse(noprofit_noloss(10, 15))

    def test_less_cost(self):
        self.assertFalse(noprofit_noloss(5, 10))

    def test_zero_cost(self):
        self.assertTrue(noprofit_noloss(0, 0))

    def test_negative_cost(self):
        with self.assertRaises(TypeError):
            noprofit_noloss(-10, 10)

    def test_negative_sale(self):
        with self.assertRaises(TypeError):
            noprofit_noloss(10, -10)

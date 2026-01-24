import unittest
from mbpp_637_code import noprofit_noloss

class TestNoprofitNoloss(unittest.TestCase):
    def test_equal_cost_and_sale(self):
        self.assertTrue(noprofit_noloss(10, 10))

    def test_greater_cost_than_sale(self):
        self.assertFalse(noprofit_noloss(10, 5))

    def test_less_cost_than_sale(self):
        self.assertFalse(noprofit_noloss(5, 10))

    def test_equal_cost_and_sale_with_negative_values(self):
        self.assertTrue(noprofit_noloss(-10, -10))

    def test_greater_cost_than_sale_with_negative_values(self):
        self.assertFalse(noprofit_noloss(-10, -5))

    def test_less_cost_than_sale_with_negative_values(self):
        self.assertFalse(noprofit_noloss(-5, -10))

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            noprofit_noloss('test', 10)

    def test_non_numeric_input_for_cost(self):
        with self.assertRaises(TypeError):
            noprofit_noloss(10, 'test')

    def test_non_numeric_input_for_sale(self):
        with self.assertRaises(TypeError):
            noprofit_noloss(10, 'test')

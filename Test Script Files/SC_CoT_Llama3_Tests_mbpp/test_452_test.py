import unittest
from mbpp_452_code import loss_amount

class TestLossAmount(unittest.TestCase):

    def test_positive_difference(self):
        self.assertEqual(loss_amount(10, 15), 5)

    def test_zero_difference(self):
        self.assertEqual(loss_amount(10, 10), None)

    def test_negative_difference(self):
        self.assertEqual(loss_amount(15, 10), None)

    def test_actual_cost_greater_than_sale_amount(self):
        self.assertEqual(loss_amount(20, 15), 5)

    def test_actual_cost_equal_to_sale_amount(self):
        self.assertEqual(loss_amount(10, 10), None)

    def test_actual_cost_less_than_sale_amount(self):
        self.assertEqual(loss_amount(5, 10), 5)

    def test_actual_cost_zero(self):
        self.assertEqual(loss_amount(0, 10), 10)

    def test_sale_amount_zero(self):
        self.assertEqual(loss_amount(10, 0), None)

    def test_actual_cost_and_sale_amount_zero(self):
        self.assertEqual(loss_amount(0, 0), None)

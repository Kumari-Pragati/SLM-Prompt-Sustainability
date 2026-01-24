import unittest
from mbpp_452_code import loss_amount

class TestLossAmount(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(loss_amount(100, 150), 50)

    def test_sale_greater_than_cost(self):
        self.assertEqual(loss_amount(50, 100), 50)

    def test_sale_equal_to_cost(self):
        self.assertIsNone(loss_amount(100, 100))

    def test_sale_less_than_cost(self):
        self.assertIsNone(loss_amount(150, 100))

    def test_sale_amount_negative(self):
        self.assertIsNone(loss_amount(100, -50))

    def test_actual_cost_negative(self):
        self.assertIsNone(loss_amount(-100, 150))

    def test_sale_amount_zero(self):
        self.assertIsNone(loss_amount(100, 0))

    def test_actual_cost_zero(self):
        self.assertIsNone(loss_amount(0, 150))

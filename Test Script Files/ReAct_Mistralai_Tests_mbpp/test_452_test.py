import unittest
from mbpp_452_code import loss_amount

class TestLossAmount(unittest.TestCase):

    def test_positive_sale_amount_greater_than_actual_cost(self):
        self.assertEqual(loss_amount(100, 150), 50)
        self.assertEqual(loss_amount(500, 400), 100)

    def test_positive_sale_amount_equal_to_actual_cost(self):
        self.assertIsNone(loss_amount(100, 100))

    def test_negative_sale_amount(self):
        self.assertIsNone(loss_amount(100, -50))

    def test_zero_sale_amount(self):
        self.assertIsNone(loss_amount(100, 0))

    def test_zero_actual_cost(self):
        self.assertEqual(loss_amount(0, 100), 100)

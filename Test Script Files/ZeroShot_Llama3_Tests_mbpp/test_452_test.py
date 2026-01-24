import unittest
from mbpp_452_code import loss_amount

class TestLossAmount(unittest.TestCase):

    def test_loss_amount_positive(self):
        self.assertEqual(loss_amount(100, 120), 20)

    def test_loss_amount_negative(self):
        self.assertIsNone(loss_amount(100, 100))

    def test_loss_amount_zero(self):
        self.assertIsNone(loss_amount(100, 100))

    def test_loss_amount_greater_than_actual_cost(self):
        self.assertEqual(loss_amount(100, 150), 50)

    def test_loss_amount_equal_to_actual_cost(self):
        self.assertIsNone(loss_amount(100, 100))

    def test_loss_amount_less_than_actual_cost(self):
        self.assertIsNone(loss_amount(100, 90))

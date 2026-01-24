import unittest
from mbpp_452_code import loss_amount

class TestLossAmount(unittest.TestCase):

    def test_positive_loss(self):
        self.assertEqual(loss_amount(100, 150), 50)

    def test_zero_loss(self):
        self.assertIsNone(loss_amount(100, 100))

    def test_negative_loss(self):
        with self.assertRaises(TypeError):
            loss_amount(-100, 100)

    def test_equal_loss(self):
        self.assertIsNone(loss_amount(100, 100))

    def test_greater_than_loss(self):
        self.assertEqual(loss_amount(100, 200), 100)

    def test_actual_cost_greater_than_sale_amount(self):
        self.assertEqual(loss_amount(200, 100), 100)

    def test_actual_cost_greater_than_sale_amount_with_zero(self):
        self.assertEqual(loss_amount(0, 0), 0)

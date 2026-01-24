import unittest
from mbpp_452_code import loss_amount

class TestLossAmount(unittest.TestCase):
    def test_positive_sale_greater_than_cost(self):
        self.assertEqual(loss_amount(100, 150), 50)

    def test_zero_sale_equal_to_cost(self):
        self.assertIsNone(loss_amount(100, 100))

    def test_negative_sale_less_than_cost(self):
        self.assertIsNone(loss_amount(100, 50))

    def test_negative_cost(self):
        self.assertIsNone(loss_amount(-100, 100))

    def test_zero_cost(self):
        self.assertIsNone(loss_amount(0, 100))

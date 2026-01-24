import unittest
from mbpp_452_code import loss_amount

class TestLossAmount(unittest.TestCase):

    def test_loss_amount_positive(self):
        self.assertEqual(loss_amount(100, 150), 50)

    def test_loss_amount_zero(self):
        self.assertIsNone(loss_amount(100, 100))

    def test_loss_amount_negative(self):
        self.assertIsNone(loss_amount(150, 100))

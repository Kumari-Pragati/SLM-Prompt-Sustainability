import unittest
from mbpp_452_code import loss_amount

class TestLossAmount(unittest.TestCase):

    def test_positive_loss(self):
        self.assertEqual(loss_amount(100, 150), 50)
        self.assertEqual(loss_amount(200, 300), 100)

    def test_zero_loss(self):
        self.assertIsNone(loss_amount(100, 100))
        self.assertIsNone(loss_amount(200, 200))

    def test_negative_loss(self):
        self.assertIsNone(loss_amount(100, 50))
        self.assertIsNone(loss_amount(200, 100))

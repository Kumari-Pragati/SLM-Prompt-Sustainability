import unittest
from mbpp_452_code import loss_amount

class TestLossAmount(unittest.TestCase):
    def test_positive_loss(self):
        self.assertEqual(loss_amount(100, 120), 20)

    def test_zero_loss(self):
        self.assertIsNone(loss_amount(100, 100))

    def test_negative_loss(self):
        self.assertIsNone(loss_amount(100, 50))

    def test_loss_greater_than_actual_cost(self):
        self.assertEqual(loss_amount(100, 150), 50)

    def test_loss_equal_to_actual_cost(self):
        self.assertIsNone(loss_amount(100, 100))

    def test_loss_less_than_actual_cost(self):
        self.assertIsNone(loss_amount(100, 90))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            loss_amount('a', 100)

    def test_invalid_input_type_2(self):
        with self.assertRaises(TypeError):
            loss_amount(100, 'b')

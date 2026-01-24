import unittest
from mbpp_452_code import loss_amount

class TestLossAmount(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(loss_amount(10, 15), 5)
        self.assertEqual(loss_amount(20, 25), 5)
        self.assertEqual(loss_amount(30, 35), 5)

    def test_equal_values(self):
        self.assertIsNone(loss_amount(10, 10))
        self.assertIsNone(loss_amount(20, 20))
        self.assertIsNone(loss_amount(30, 30))

    def test_negative_values(self):
        self.assertEqual(loss_amount(-10, -5), 5)
        self.assertEqual(loss_amount(-20, -15), 5)
        self.assertEqual(loss_amount(-30, -25), 5)

    def test_zero_values(self):
        self.assertIsNone(loss_amount(0, 0))
        self.assertEqual(loss_amount(0, 10), 10)
        self.assertEqual(loss_amount(10, 0), None)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            loss_amount("a", 10)
        with self.assertRaises(TypeError):
            loss_amount(10, "b")

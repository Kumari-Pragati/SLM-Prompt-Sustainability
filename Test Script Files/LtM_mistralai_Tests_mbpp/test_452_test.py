import unittest
from mbpp_452_code import loss_amount

class TestLossAmount(unittest.TestCase):

    def test_simple_positive_sale(self):
        self.assertEqual(loss_amount(100, 150), 50)

    def test_simple_negative_sale(self):
        self.assertEqual(loss_amount(150, 100), None)

    def test_zero_sale(self):
        self.assertEqual(loss_amount(100, 100), None)

    def test_negative_actual_cost(self):
        self.assertEqual(loss_amount(-100, 100), 200)

    def test_edge_case_zero_difference(self):
        self.assertEqual(loss_amount(100, 100), None)

    def test_large_positive_sale(self):
        self.assertEqual(loss_amount(1000000, 999999), 1)

    def test_large_negative_sale(self):
        self.assertEqual(loss_amount(999999, 1000000), None)

import unittest
from mbpp_452_code import loss_amount

class TestLossAmount(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(loss_amount(100, 120), 20)

    def test_edge_case_equal(self):
        self.assertIsNone(loss_amount(100, 100))

    def test_edge_case_actual_cost_zero(self):
        self.assertIsNone(loss_amount(0, 100))

    def test_edge_case_sale_amount_zero(self):
        self.assertIsNone(loss_amount(100, 0))

    def test_edge_case_actual_cost_negative(self):
        self.assertIsNone(loss_amount(-100, 100))

    def test_edge_case_sale_amount_negative(self):
        self.assertIsNone(loss_amount(100, -100))

    def test_edge_case_actual_cost_and_sale_amount_negative(self):
        self.assertIsNone(loss_amount(-100, -100))

    def test_edge_case_actual_cost_zero_and_sale_amount_zero(self):
        self.assertIsNone(loss_amount(0, 0))

    def test_edge_case_actual_cost_zero_and_sale_amount_negative(self):
        self.assertIsNone(loss_amount(0, -100))

    def test_edge_case_actual_cost_negative_and_sale_amount_zero(self):
        self.assertIsNone(loss_amount(-100, 0))

    def test_edge_case_actual_cost_negative_and_sale_amount_negative(self):
        self.assertIsNone(loss_amount(-100, -100))

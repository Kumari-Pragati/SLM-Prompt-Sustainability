import unittest
from mbpp_452_code import loss_amount

class TestLossAmount(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(loss_amount(100, 150), 50)
        self.assertEqual(loss_amount(50, 100), 0)
        self.assertEqual(loss_amount(0, 50), None)

    def test_edge_case(self):
        self.assertEqual(loss_amount(0, 0), None)
        self.assertEqual(loss_amount(1, 1), 0)

    def test_boundary_case(self):
        self.assertEqual(loss_amount(float('-inf'), 100), 100)
        self.assertEqual(loss_amount(100, float('-inf')), None)
        self.assertEqual(loss_amount(0, 0), None)

import unittest
from mbpp_452_code import loss_amount

class TestLossAmount(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(loss_amount(100, 150), 50)
        self.assertEqual(loss_amount(200, 250), 50)

    def test_edge_cases(self):
        self.assertEqual(loss_amount(0, 1), None)
        self.assertEqual(loss_amount(1, 0), None)
        self.assertEqual(loss_amount(100, 100), None)

    def test_boundary_cases(self):
        self.assertEqual(loss_amount(100, 100.01), 0.01)
        self.assertEqual(loss_amount(100.01, 100), -0.01)

    def test_negative_inputs(self):
        self.assertEqual(loss_amount(-100, 100), None)
        self.assertEqual(loss_amount(100, -100), None)

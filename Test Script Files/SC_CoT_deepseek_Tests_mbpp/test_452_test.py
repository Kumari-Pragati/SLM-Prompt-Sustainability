import unittest
from mbpp_452_code import loss_amount

class TestLossAmount(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(loss_amount(100, 150), 50)

    def test_boundary_case(self):
        self.assertEqual(loss_amount(100, 100), None)

    def test_edge_case(self):
        self.assertEqual(loss_amount(0, 100), 100)
        self.assertEqual(loss_amount(100, 0), None)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            loss_amount("100", 150)
        with self.assertRaises(TypeError):
            loss_amount(100, "150")
        with self.assertRaises(TypeError):
            loss_amount("100", "150")

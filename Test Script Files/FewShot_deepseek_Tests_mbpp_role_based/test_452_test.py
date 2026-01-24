import unittest
from mbpp_452_code import loss_amount

class TestLossAmount(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(loss_amount(100, 150), 50)

    def test_boundary_condition(self):
        self.assertEqual(loss_amount(0, 100), 100)
        self.assertIsNone(loss_amount(100, 100))

    def test_edge_case(self):
        self.assertEqual(loss_amount(100, 0), None)
        self.assertEqual(loss_amount(-100, 100), 200)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            loss_amount("100", 150)
        with self.assertRaises(TypeError):
            loss_amount(100, "150")

import unittest
from mbpp_962_code import sum_Even

class TestSumEven(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(sum_Even(2, 6), 20)
        self.assertEqual(sum_Even(4, 8), 32)
        self.assertEqual(sum_Even(6, 10), 40)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_Even(0, 2), 0)
        self.assertEqual(sum_Even(1, 3), 0)
        self.assertEqual(sum_Even(2, 0), 0)
        self.assertEqual(sum_Even(2147483647, 2147483648), 0)
        self.assertEqual(sum_Even(-1, 0), 0)
        self.assertEqual(sum_Even(-2, 1), 0)
        self.assertEqual(sum_Even(2147483647, -1), 0)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, sum_Even, "string", 5)
        self.assertRaises(TypeError, sum_Even, 5, "string")
        self.assertRaises(ValueError, sum_Even, -2, -3)
        self.assertRaises(ValueError, sum_Even, 0, -1)

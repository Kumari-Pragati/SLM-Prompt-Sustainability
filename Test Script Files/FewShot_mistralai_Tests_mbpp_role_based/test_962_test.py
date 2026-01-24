import unittest
from mbpp_962_code import sum_Even

class TestSumEven(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_Even(2, 4), 6)
        self.assertEqual(sum_Even(4, 8), 30)

    def test_zero(self):
        self.assertEqual(sum_Even(0, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_Even(-2, 0), 0)
        self.assertEqual(sum_Even(-2, 2), 0)
        self.assertEqual(sum_Even(-4, -2), 12)

    def test_edge_cases(self):
        self.assertEqual(sum_Even(1, 2), 1)
        self.assertEqual(sum_Even(2, 1), 1)
        self.assertEqual(sum_Even(0, 1), 0)
        self.assertEqual(sum_Even(1, 0), 0)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, sum_Even, 'a', 'b')
        self.assertRaises(TypeError, sum_Even, 1.5, 2)
        self.assertRaises(ValueError, sum_Even, -1, 0)

import unittest
from mbpp_962_code import sum_Even

class TestSumEven(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(sum_Even(2, 10), 20)

    def test_boundary_conditions(self):
        self.assertEqual(sum_Even(1, 1), 0)
        self.assertEqual(sum_Even(1, 2), 1)

    def test_edge_conditions(self):
        self.assertEqual(sum_Even(1, 1000000), 250000250000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sum_Even("2", 10)
        with self.assertRaises(TypeError):
            sum_Even(2, "10")
        with self.assertRaises(ValueError):
            sum_Even(2, 1)

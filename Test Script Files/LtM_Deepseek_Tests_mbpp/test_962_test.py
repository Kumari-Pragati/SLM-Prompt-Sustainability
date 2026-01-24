import unittest
from mbpp_962_code import sum_Even

class TestSumEven(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(sum_Even(2, 10), 30)
        self.assertEqual(sum_Even(1, 10), 25)

    def test_boundary_conditions(self):
        self.assertEqual(sum_Even(1, 1), 0)
        self.assertEqual(sum_Even(2, 2), 0)
        self.assertEqual(sum_Even(1, 2), 0)

    def test_edge_conditions(self):
        self.assertEqual(sum_Even(1, 100), 2550)
        self.assertEqual(sum_Even(1, 1000), 250500)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sum_Even("1", 10)
        with self.assertRaises(TypeError):
            sum_Even(1, "10")
        with self.assertRaises(TypeError):
            sum_Even("1", "10")

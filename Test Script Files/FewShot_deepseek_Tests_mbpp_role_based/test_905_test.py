import unittest
from mbpp_905_code import sum_of_square

class TestSumOfSquare(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(sum_of_square(3), 14)

    def test_boundary_conditions(self):
        self.assertEqual(sum_of_square(0), 1)
        self.assertEqual(sum_of_square(1), 2)

    def test_edge_conditions(self):
        self.assertEqual(sum_of_square(2), 6)
        self.assertEqual(sum_of_square(10), 30240)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            sum_of_square(-1)
        with self.assertRaises(ValueError):
            sum_of_square(1.5)

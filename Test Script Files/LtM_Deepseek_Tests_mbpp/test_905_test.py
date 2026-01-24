import unittest
from mbpp_905_code import sum_of_square

class TestSumOfSquare(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(sum_of_square(1), 1)
        self.assertEqual(sum_of_square(2), 5)
        self.assertEqual(sum_of_square(3), 14)

    def test_edge_conditions(self):
        self.assertEqual(sum_of_square(0), 1)
        self.assertEqual(sum_of_square(1), 1)

    def test_boundary_conditions(self):
        self.assertEqual(sum_of_square(10), 945)
        self.assertEqual(sum_of_square(20), 137340)

    def test_complex_cases(self):
        self.assertEqual(sum_of_square(15), 155117520)
        self.assertEqual(sum_of_square(25), 155117520)

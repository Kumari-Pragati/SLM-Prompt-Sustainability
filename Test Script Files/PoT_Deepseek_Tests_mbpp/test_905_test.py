import unittest
from mbpp_905_code import sum_of_square

class TestSumOfSquare(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(sum_of_square(1), 1)
        self.assertEqual(sum_of_square(2), 5)
        self.assertEqual(sum_of_square(3), 14)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_of_square(0), 1)
        self.assertEqual(sum_of_square(1), 1)

    def test_corner_cases(self):
        self.assertEqual(sum_of_square(10), 945)
        self.assertEqual(sum_of_square(20), 1373705)

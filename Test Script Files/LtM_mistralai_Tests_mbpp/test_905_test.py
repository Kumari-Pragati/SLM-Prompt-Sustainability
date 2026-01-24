import unittest
from mbpp_905_code import sum_of_square

class TestSumOfSquare(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(sum_of_square(1), 1)
        self.assertEqual(sum_of_square(2), 5)
        self.assertEqual(sum_of_square(3), 29)

    def test_edge_and_boundary(self):
        self.assertEqual(sum_of_square(0), 0)
        self.assertEqual(sum_of_square(4), 14)
        self.assertEqual(sum_of_square(5), 91)

    def test_complex(self):
        self.assertEqual(sum_of_square(6), 462)
        self.assertEqual(sum_of_square(7), 1679)
        self.assertEqual(sum_of_square(8), 6404)

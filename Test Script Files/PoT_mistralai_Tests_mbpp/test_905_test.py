import unittest
from mbpp_905_code import sum_of_square

class TestSumOfSquare(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_of_square(1), 1)
        self.assertEqual(sum_of_square(2), 5)
        self.assertEqual(sum_of_square(3), 27)
        self.assertEqual(sum_of_square(4), 125)

    def test_edge_case(self):
        self.assertEqual(sum_of_square(0), 0)
        self.assertEqual(sum_of_square(5), 243)

    def test_boundary_case(self):
        self.assertEqual(sum_of_square(100), 3045456097568676289)
        self.assertEqual(sum_of_square(1000), 10715086071862677561766063735593229)

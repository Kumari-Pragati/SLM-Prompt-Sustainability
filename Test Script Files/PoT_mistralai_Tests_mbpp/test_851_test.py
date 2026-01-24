import unittest
from mbpp_851_code import Sum_of_Inverse_Divisors

class TestSumOfInverseDivisors(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Sum_of_Inverse_Divisors(4, 2), 2.0)
        self.assertEqual(Sum_of_InverseDivisors(9, 3), 3.0)
        self.assertEqual(Sum_of_InverseDivisors(10, 4), 2.5)

    def test_edge_case(self):
        self.assertEqual(Sum_of_InverseDivisors(1, 1), 1.0)
        self.assertEqual(Sum_of_InverseDivisors(2, 1), 1.0)
        self.assertEqual(Sum_of_InverseDivisors(3, 1), 1.0)

    def test_boundary_case(self):
        self.assertEqual(Sum_of_InverseDivisors(0, 0), 0.0)
        self.assertEqual(Sum_of_InverseDivisors(1, 0), 0.0)
        self.assertEqual(Sum_of_InverseDivisors(2, 0), 0.0)

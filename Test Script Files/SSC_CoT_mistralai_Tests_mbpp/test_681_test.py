import unittest
from mbpp_681_code import smallest_Divisor

class TestSmallestDivisor(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(smallest_Divisor(6), 2)
        self.assertEqual(smallest_Divisor(10), 2)
        self.assertEqual(smallest_Divisor(18), 2)
        self.assertEqual(smallest_Divisor(24), 2)
        self.assertEqual(smallest_Divisor(26), 13)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(smallest_Divisor(0), 0)
        self.assertEqual(smallest_Divisor(1), 1)
        self.assertEqual(smallest_Divisor(3), 3)
        self.assertEqual(smallest_Divisor(5), 5)
        self.assertEqual(smallest_Divisor(2147483647), 2147483647)

    def test_special_cases(self):
        self.assertEqual(smallest_Divisor(4), 2)
        self.assertEqual(smallest_Divisor(12), 3)
        self.assertEqual(smallest_Divisor(20), 4)
        self.assertEqual(smallest_Divisor(22), 11)
        self.assertEqual(smallest_Divisor(30), 5)

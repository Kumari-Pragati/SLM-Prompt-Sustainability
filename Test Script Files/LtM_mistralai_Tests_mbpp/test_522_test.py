import unittest
from mbpp_522_code import lbs

class TestLbs(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(lbs([1, 5, 3, 4]), 5)
        self.assertEqual(lbs([10, 2, 3, 4]), 9)
        self.assertEqual(lbs([1, 2, 3, 4, 5]), 5)

    def test_edge_cases(self):
        self.assertEqual(lbs([1]), 1)
        self.assertEqual(lbs([1, 1]), 2)
        self.assertEqual(lbs([10, 9, 8, 7, 6]), 14)
        self.assertEqual(lbs([100, 99, 98, 97, 96]), 194)

    def test_boundary_conditions(self):
        self.assertEqual(lbs([]), 0)
        self.assertEqual(lbs([1000000]), 1)
        self.assertEqual(lbs([1000000, 1000000]), 2)

    def test_complex_cases(self):
        self.assertEqual(lbs([1, 10, 5, 2, 15, 3, 7]), 16)
        self.assertEqual(lbs([1000000, 999999, 999998, 999997, 999996]), 195)
        self.assertEqual(lbs([1000000, 999999, 999998, 999997, 999996, 1]), 195)

import unittest
from mbpp_504_code import sum_Of_Series

class TestSumOfSeries(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sum_Of_Series(1), 1)
        self.assertEqual(sum_Of_Series(2), 8)
        self.assertEqual(sum_Of_Series(3), 33)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_Of_Series(0), 0)
        self.assertEqual(sum_Of_Series(4), 104)
        self.assertEqual(sum_Of_Series(5), 325)

    def test_complex_input(self):
        self.assertEqual(sum_Of_Series(10), 3850)
        self.assertEqual(sum_Of_Series(20), 191468)

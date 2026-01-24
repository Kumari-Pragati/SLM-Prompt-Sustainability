import unittest
from mbpp_195_code import first

class TestFirstFunction(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(first([1, 3, 5, 6], 3, 4), 1)
        self.assertEqual(first([10, 20, 30, 40], 30, 4), 2)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(first([], 10, 1), -1)
        self.assertEqual(first([10], 10, 1), 0)
        self.assertEqual(first([1, 2, 3], 4, 3), -1)
        self.assertEqual(first([1, 2, 3], 1, 3), 0)
        self.assertEqual(first([1, 2, 3], 4, 0), -1)

    def test_complex_and_corner_cases(self):
        self.assertEqual(first([1, 3, 5, 6], 2, 4), 1)
        self.assertEqual(first([10, 20, 30, 40], 10, 4), 3)
        self.assertEqual(first([10, 9, 8, 7, 6], 10, 5), 4)
        self.assertEqual(first([10, 9, 8, 7, 6], 1, 5), 0)

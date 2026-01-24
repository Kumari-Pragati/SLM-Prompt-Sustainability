import unittest
from mbpp_550_code import find_Max

class TestFindMax(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 0, 4), 5)
        self.assertEqual(find_Max([5, 4, 3, 2, 1], 0, 4), 5)
        self.assertEqual(find_Max([1, 5, 3, 2, 4], 0, 4), 5)

    def test_edge_conditions(self):
        self.assertEqual(find_Max([1], 0, 0), 1)
        self.assertEqual(find_Max([], 0, -1), None)

    def test_boundary_conditions(self):
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 0, 0), 1)
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 4, 4), 5)
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 0, 4), 5)

    def test_complex_cases(self):
        self.assertEqual(find_Max([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8), 9)
        self.assertEqual(find_Max([9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 8), 9)
        self.assertEqual(find_Max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 9), 10)

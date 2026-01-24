import unittest
from mbpp_410_code import min_val

class TestMinVal(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(min_val([1, 2, 3, 4, 5]), 1)
        self.assertEqual(min_val([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(min_val([0, 0, 0, 0, 0]), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(min_val([1, float('inf'), 3]), 1)
        self.assertEqual(min_val([float('-inf'), -2, -3]), float('-inf'))
        self.assertEqual(min_val([-1, 0, 1]), -1)
        self.assertEqual(min_val([1, 2, 3, 4, 5, 5]), 1)
        self.assertEqual(min_val([5, 4, 3, 2, 1]), 1)

    def test_special_cases(self):
        self.assertEqual(min_val([1, 'two', 3]), 1)
        self.assertEqual(min_val([1, [], 3]), 1)
        self.assertEqual(min_val([1, None, 3]), 1)

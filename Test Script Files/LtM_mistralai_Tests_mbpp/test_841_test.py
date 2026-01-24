import unittest
from mbpp_841_code import get_inv_count

class TestGetInvCount(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(get_inv_count([1, 2, 3, 4], 4), 0)
        self.assertEqual(get_inv_count([4, 3, 2, 1], 4), 6)
        self.assertEqual(get_inv_count([1, 1, 1, 1], 4), 0)

    def test_edge_cases(self):
        self.assertEqual(get_inv_count([], 0), 0)
        self.assertEqual(get_inv_count([1], 1), 0)
        self.assertEqual(get_inv_count([1, 2], 2), 1)
        self.assertEqual(get_inv_count([2, 1], 2), 1)
        self.assertEqual(get_inv_count([1, 1, 2], 3), 1)
        self.assertEqual(get_inv_count([2, 1, 1], 3), 1)

    def test_boundary_conditions(self):
        self.assertEqual(get_inv_count([2147483647], 1), 0)
        self.assertEqual(get_inv_count([-2147483648], 1), 0)
        self.assertEqual(get_inv_count([-2147483648, -2147483647], 2), 1)
        self.assertEqual(get_inv_count([2147483647, 2147483648], 2), 1)

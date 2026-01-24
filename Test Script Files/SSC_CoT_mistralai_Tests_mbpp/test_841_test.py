import unittest
from mbpp_841_code import get_inv_count

class TestGetInvCount(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(get_inv_count([1, 2, 3, 4], 4), 0)
        self.assertEqual(get_inv_count([4, 3, 2, 1], 4), 6)
        self.assertEqual(get_inv_count([1, 1, 1, 1], 4), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(get_inv_count([1, 2, 3], 3), 0)
        self.assertEqual(get_inv_count([1, 2, 3, 4, 5], 5), 5)
        self.assertEqual(get_inv_count([], 0), 0)
        self.assertEqual(get_inv_count([1], 1), 0)

    def test_negative_numbers(self):
        self.assertEqual(get_inv_count([-1, -2, -3], 3), 6)
        self.assertEqual(get_inv_count([-1, -1, -1], 3), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_inv_count(1, 2.5)
        with self.assertRaises(TypeError):
            get_inv_count([1, 2], '3')

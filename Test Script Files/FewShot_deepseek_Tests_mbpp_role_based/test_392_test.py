import unittest
from mbpp_392_code import get_max_sum

class TestGetMaxSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(get_max_sum(6), 8)

    def test_boundary_conditions(self):
        self.assertEqual(get_max_sum(0), 0)
        self.assertEqual(get_max_sum(1), 1)
        self.assertEqual(get_max_sum(2), 2)

    def test_edge_conditions(self):
        self.assertEqual(get_max_sum(3), 3)
        self.assertEqual(get_max_sum(4), 4)
        self.assertEqual(get_max_sum(5), 5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_max_sum('6')
        with self.assertRaises(ValueError):
            get_max_sum(-1)

import unittest
from mbpp_392_code import get_max_sum

class TestGetMaxSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(get_max_sum(1), 0)
        self.assertEqual(get_max_sum(2), 1)
        self.assertEqual(get_max_sum(3), 2)
        self.assertEqual(get_max_sum(4), 3)
        self.assertEqual(get_max_sum(5), 4)
        self.assertEqual(get_max_sum(6), 5)
        self.assertEqual(get_max_sum(7), 6)
        self.assertEqual(get_max_sum(8), 7)
        self.assertEqual(get_max_sum(9), 8)
        self.assertEqual(get_max_sum(10), 9)

    def test_boundary_conditions(self):
        self.assertEqual(get_max_sum(0), 0)
        self.assertEqual(get_max_sum(11), 10)

    def test_edge_cases(self):
        self.assertEqual(get_max_sum(1), 0)
        self.assertEqual(get_max_sum(2), 1)
        self.assertEqual(get_max_sum(3), 2)
        self.assertEqual(get_max_sum(4), 3)
        self.assertEqual(get_max_sum(5), 4)
        self.assertEqual(get_max_sum(6), 5)
        self.assertEqual(get_max_sum(7), 6)
        self.assertEqual(get_max_sum(8), 7)
        self.assertEqual(get_max_sum(9), 8)
        self.assertEqual(get_max_sum(10), 9)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            get_max_sum('a')
        with self.assertRaises(TypeError):
            get_max_sum(None)
        with self.assertRaises(TypeError):
            get_max_sum([])
        with self.assertRaises(TypeError):
            get_max_sum({})

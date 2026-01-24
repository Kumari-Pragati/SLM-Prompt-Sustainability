import unittest
from mbpp_392_code import get_max_sum

class TestGetMaxSum(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(get_max_sum(5), 7)
        self.assertEqual(get_max_sum(10), 17)
        self.assertEqual(get_max_sum(15), 26)

    def test_edge_cases(self):
        self.assertEqual(get_max_sum(1), 0)
        self.assertEqual(get_max_sum(2), 1)
        self.assertEqual(get_max_sum(3), 1)

    def test_boundary_cases(self):
        self.assertEqual(get_max_sum(4), 2)
        self.assertEqual(get_max_sum(5), 7)
        self.assertEqual(get_max_sum(6), 6)

    def test_special_cases(self):
        self.assertEqual(get_max_sum(7), 9)
        self.assertEqual(get_max_sum(8), 8)
        self.assertEqual(get_max_sum(9), 9)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            get_max_sum('a')

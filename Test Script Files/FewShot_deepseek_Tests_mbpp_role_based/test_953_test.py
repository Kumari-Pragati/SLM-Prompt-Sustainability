import unittest
from mbpp_953_code import subset

class TestSubset(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(subset([1, 2, 2, 3, 3, 3], 6), 3)

    def test_edge_condition(self):
        self.assertEqual(subset([1], 1), 1)

    def test_boundary_condition(self):
        self.assertEqual(subset([], 0), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            subset("1, 2, 2, 3, 3, 3", 6)

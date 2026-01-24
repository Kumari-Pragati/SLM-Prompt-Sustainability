import unittest
from mbpp_66_code import pos_count

class TestPosCount(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(pos_count([1, 2, 3, 4, 5]), 5)
        self.assertEqual(pos_count([]), 0)
        self.assertEqual(pos_count([0]), 0)
        self.assertEqual(pos_count([0, -1, 2, 3, -5]), 3)
        self.assertEqual(pos_count([-1, -2, -3, -4, -5]), 0)

    def test_edge_cases(self):
        self.assertEqual(pos_count([float('inf')]), 1)
        self.assertEqual(pos_count([-float('inf')]), 0)
        self.assertEqual(pos_count([float('nan')]), 0)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, pos_count, 42)
        self.assertRaises(TypeError, pos_count, (1, 2, 3))

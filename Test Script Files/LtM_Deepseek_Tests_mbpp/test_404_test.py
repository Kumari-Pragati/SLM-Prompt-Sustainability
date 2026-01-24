import unittest
from mbpp_404_code import minimum

class TestMinimum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(minimum(1, 2), 1)
        self.assertEqual(minimum(3, 2), 2)

    def test_boundary_conditions(self):
        self.assertEqual(minimum(0, 0), 0)
        self.assertEqual(minimum(-1, 1), -1)
        self.assertEqual(minimum(float('-inf'), float('inf')), float('-inf'))

    def test_edge_cases(self):
        self.assertEqual(minimum(float('inf'), float('-inf')), float('-inf'))
        self.assertEqual(minimum(float('nan'), 1), float('nan'))
        self.assertEqual(minimum(1, float('nan')), 1)
        self.assertEqual(minimum(float('nan'), float('nan')), float('nan'))

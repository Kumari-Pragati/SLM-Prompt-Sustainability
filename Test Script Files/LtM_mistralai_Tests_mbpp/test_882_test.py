import unittest
from mbpp_882_code import parallelogram_perimeter

class TestParallelogramPerimeter(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(parallelogram_perimeter(2, 3), 12)
        self.assertEqual(parallelogram_perimeter(3, 4), 24)

    def test_edge_cases(self):
        self.assertEqual(parallelogram_perimeter(0, 1), 0)
        self.assertEqual(parallelogram_perimeter(1, 0), 0)
        self.assertEqual(parallelogram_perimeter(1, 1), 4)

    def test_boundary_conditions(self):
        self.assertEqual(parallelogram_perimeter(float('inf'), 1), 2*float('inf'))
        self.assertEqual(parallelogram_perimeter(1, float('inf')), 2*float('inf'))

    def test_negative_input(self):
        self.assertEqual(parallelogram_perimeter(-2, 3), -12)
        self.assertEqual(parallelogram_perimeter(2, -3), -12)

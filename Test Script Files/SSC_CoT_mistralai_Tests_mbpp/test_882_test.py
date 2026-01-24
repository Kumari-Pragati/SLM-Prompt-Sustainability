import unittest
from mbpp_882_code import parallelogram_perimeter

class TestParallelogramPerimeter(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(parallelogram_perimeter(4, 5), 20)
        self.assertEqual(parallelogram_perimeter(3, 6), 18)

    def test_edge_cases(self):
        self.assertEqual(parallelogram_perimeter(0, 5), 0)
        self.assertEqual(parallelogram_perimeter(5, 0), 0)

    def test_boundary_conditions(self):
        self.assertEqual(parallelogram_perimeter(1, 1), 4)
        self.assertEqual(parallelogram_perimeter(2.5, 2.5), 10)

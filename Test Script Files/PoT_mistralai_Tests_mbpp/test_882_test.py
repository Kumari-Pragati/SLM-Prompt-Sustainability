import unittest
from mbpp_882_code import parallelogram_perimeter

class TestParallelogramPerimeter(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(parallelogram_perimeter(3, 4), 24)

    def test_edge_case_zero(self):
        self.assertEqual(parallelogram_perimeter(0, 4), 0)
        self.assertEqual(parallelogram_perimeter(3, 0), 0)

    def test_edge_case_one(self):
        self.assertEqual(parallelogram_perimeter(1, 1), 4)

    def test_boundary_case_small(self):
        self.assertEqual(parallelogram_perimeter(1, 2), 6)

    def test_boundary_case_large(self):
        self.assertEqual(parallelogram_perimeter(100, 100), 20000)

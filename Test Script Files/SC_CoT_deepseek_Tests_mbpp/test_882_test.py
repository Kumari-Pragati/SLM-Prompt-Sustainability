import unittest
from mbpp_882_code import parallelogram_perimeter

class TestParallelogramPerimeter(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(parallelogram_perimeter(2, 3), 12)

    def test_boundary_case(self):
        self.assertAlmostEqual(parallelogram_perimeter(0, 0), 0)

    def test_edge_case(self):
        self.assertAlmostEqual(parallelogram_perimeter(1, 1), 4)

    def test_negative_values(self):
        self.assertAlmostEqual(parallelogram_perimeter(-2, -3), 12)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            parallelogram_perimeter("2", 3)

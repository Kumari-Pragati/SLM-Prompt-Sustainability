import unittest
from mbpp_882_code import parallelogram_perimeter

class TestParallelogramPerimeter(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(parallelogram_perimeter(5, 10), 100)

    def test_edge_case(self):
        self.assertAlmostEqual(parallelogram_perimeter(0, 10), 0)
        self.assertAlmostEqual(parallelogram_perimeter(5, 0), 0)

    def test_boundary_case(self):
        self.assertAlmostEqual(parallelogram_perimeter(1, 1), 2)
        self.assertAlmostEqual(parallelogram_perimeter(10000, 10000), 400000000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            parallelogram_perimeter("5", 10)
        with self.assertRaises(TypeError):
            parallelogram_perimeter(5, "10")
        with self.assertRaises(TypeError):
            parallelogram_perimeter("5", "10")

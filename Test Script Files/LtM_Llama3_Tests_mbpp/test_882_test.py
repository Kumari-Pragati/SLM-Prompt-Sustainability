import unittest
from mbpp_882_code import parallelogram_perimeter

class TestParallelogramPerimeter(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(parallelogram_perimeter(5, 10), 100)
        self.assertEqual(parallelogram_perimeter(10, 5), 100)
        self.assertEqual(parallelogram_perimeter(2, 3), 12)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(parallelogram_perimeter(0, 0), 0)
        self.assertEqual(parallelogram_perimeter(0, 10), 20)
        self.assertEqual(parallelogram_perimeter(10, 0), 20)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            parallelogram_perimeter("five", 10)
        with self.assertRaises(TypeError):
            parallelogram_perimeter(5, "ten")

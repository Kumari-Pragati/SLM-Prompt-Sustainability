import unittest
from mbpp_882_code import parallelogram_perimeter

class TestParallelogramPerimeter(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(parallelogram_perimeter(5, 10), 100)

    def test_boundary_conditions(self):
        self.assertEqual(parallelogram_perimeter(0, 0), 0)
        self.assertEqual(parallelogram_perimeter(1, 1), 2)
        self.assertEqual(parallelogram_perimeter(100, 100), 20000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            parallelogram_perimeter("5", 10)
        with self.assertRaises(TypeError):
            parallelogram_perimeter(5, "10")
        with self.assertRaises(TypeError):
            parallelogram_perimeter("5", "10")
        with self.assertRaises(ValueError):
            parallelogram_perimeter(-5, 10)
        with self.assertRaises(ValueError):
            parallelogram_perimeter(5, -10)

import unittest
from mbpp_52_code import parallelogram_area

class TestParallelogramArea(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(parallelogram_area(5, 10), 50)

    def test_boundary_conditions(self):
        self.assertEqual(parallelogram_area(0, 10), 0)
        self.assertEqual(parallelogram_area(5, 0), 0)
        self.assertEqual(parallelogram_area(0, 0), 0)

    def test_negative_values(self):
        self.assertEqual(parallelogram_area(-5, 10), -50)
        self.assertEqual(parallelogram_area(5, -10), -50)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            parallelogram_area("5", 10)
        with self.assertRaises(TypeError):
            parallelogram_area(5, "10")
        with self.assertRaises(TypeError):
            parallelogram_area("5", "10")

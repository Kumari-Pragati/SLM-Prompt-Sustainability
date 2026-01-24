import unittest
from mbpp_52_code import parallelogram_area

class TestParallelogramArea(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(parallelogram_area(5, 10), 50)
        self.assertEqual(parallelogramram_area(10, 5), 50)
        self.assertEqual(parallelogram_area(0, 0), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(parallelogram_area(-5, 10), 50)
        self.assertEqual(parallelogram_area(5, -10), 50)
        self.assertEqual(parallelogram_area(0, 10), 0)
        self.assertEqual(parallelogram_area(10, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            parallelogram_area('a', 10)
        with self.assertRaises(TypeError):
            parallelogram_area(5, 'b')

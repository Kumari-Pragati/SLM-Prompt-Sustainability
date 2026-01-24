import unittest
from mbpp_52_code import parallelogram_area

class TestParallelogramArea(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(parallelogram_area(5, 3), 15)

    def test_edge_cases(self):
        self.assertEqual(parallelogram_area(0, 3), 0)
        self.assertEqual(parallelogram_area(3, 0), 0)
        self.assertEqual(parallelogram_area(1, 1), 1)

    def test_negative_input(self):
        self.assertEqual(parallelogram_area(-5, 3), None)
        self.assertEqual(parallelogram_area(5, -3), None)

    def test_float_input(self):
        self.assertAlmostEqual(parallelogram_area(3.5, 2), 7.0)
        self.assertAlmostEqual(parallelogram_area(2, 3.5), 7.0)

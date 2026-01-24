import unittest
from mbpp_882_code import parallelogram_perimeter

class TestParallelogramPerimeter(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(parallelogram_perimeter(5, 10), 100)

    def test_edge_case_zero_base(self):
        self.assertEqual(parallelogram_perimeter(0, 10), 0)

    def test_edge_case_zero_height(self):
        self.assertEqual(parallelogram_perimeter(5, 0), 0)

    def test_edge_case_negative_base(self):
        self.assertEqual(parallelogram_perimeter(-5, 10), 0)

    def test_edge_case_negative_height(self):
        self.assertEqual(parallelogram_perimeter(5, -10), 0)

    def test_complex_case_large_numbers(self):
        self.assertAlmostEqual(parallelogram_perimeter(10000, 20000), 600000000)

import unittest
from mbpp_52_code import parallelogram_area

class TestParallelogramArea(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(parallelogram_area(5, 3), 15)

    def test_edge_case_zero_base(self):
        self.assertEqual(parallelogram_area(2, 0), 0)

    def test_edge_case_zero_height(self):
        self.assertEqual(parallelogram_area(3, 0), 0)

    def test_boundary_case_negative_base(self):
        self.assertEqual(parallelogram_area(-2, 3), 0)

    def test_boundary_case_negative_height(self):
        self.assertEqual(parallelogram_area(2, -3), 0)

import unittest
from mbpp_52_code import parallelogram_area

class TestParallelogramArea(unittest.TestCase):

    def test_simple_positive(self):
        self.assertEqual(parallelogram_area(3, 4), 12)

    def test_typical_positive(self):
        self.assertEqual(parallelogram_area(5, 7), 35)

    def test_edge_zero_base(self):
        self.assertEqual(parallelogram_area(0, 5), 0)

    def test_edge_zero_height(self):
        self.assertEqual(parallelogram_area(4, 0), 0)

    def test_edge_negative(self):
        self.assertEqual(parallelogram_area(-3, 4), 0)

    def test_edge_min_positive(self):
        self.assertEqual(parallelogram_area(1, 1), 1)

    def test_edge_max_positive(self):
        self.assertEqual(parallelogram_area(1000000, 1000000), 1000000000000)

import unittest
from mbpp_52_code import parallelogram_area

class TestParallelogramArea(unittest.TestCase):

    def test_parallelogram_area_positive(self):
        self.assertEqual(parallelogram_area(4, 5), 20)
        self.assertEqual(parallelogram_area(3, 6), 18)
        self.assertEqual(parallelogram_area(2, 8), 16)

    def test_parallelogram_area_zero(self):
        self.assertEqual(parallelogram_area(0, 5), 0)
        self.assertEqual(parallelogram_area(5, 0), 0)

    def test_parallelogram_area_negative(self):
        self.assertEqual(parallelogram_area(-3, 4), 0)
        self.assertEqual(parallelogram_area(4, -3), 0)

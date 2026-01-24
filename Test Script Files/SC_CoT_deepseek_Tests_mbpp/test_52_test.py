import unittest
from mbpp_52_code import parallelogram_area

class TestParallelogramArea(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(parallelogram_area(5, 10), 50)

    def test_zero_base(self):
        self.assertAlmostEqual(parallelogram_area(0, 10), 0)

    def test_zero_height(self):
        self.assertAlmostEqual(parallelogram_area(5, 0), 0)

    def test_negative_base(self):
        with self.assertRaises(Exception):
            parallelogram_area(-5, 10)

    def test_negative_height(self):
        with self.assertRaises(Exception):
            parallelogram_area(5, -10)

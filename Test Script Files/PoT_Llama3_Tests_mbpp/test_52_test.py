import unittest
from mbpp_52_code import parallelogram_area

class TestParallelogramArea(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(parallelogram_area(5, 3), 15)

    def test_zero_base(self):
        self.assertEqual(parallelogram_area(0, 3), 0)

    def test_zero_height(self):
        self.assertEqual(parallelogram_area(5, 0), 0)

    def test_negative_base(self):
        self.assertEqual(parallelogram_area(-5, 3), 15)

    def test_negative_height(self):
        self.assertEqual(parallelogram_area(5, -3), 15)

    def test_non_integer_base(self):
        self.assertEqual(parallelogram_area(5.5, 3), 16.5)

    def test_non_integer_height(self):
        self.assertEqual(parallelogram_area(5, 3.5), 17.5)

import unittest
from mbpp_52_code import parallelogram_area

class TestParallelogramArea(unittest.TestCase):

    def test_positive_values(self):
        self.assertEqual(parallelogram_area(5, 10), 50)

    def test_negative_values(self):
        self.assertEqual(parallelogram_area(-5, 10), -50)

    def test_zero_values(self):
        self.assertEqual(parallelogram_area(0, 0), 0)

    def test_non_numeric_values(self):
        with self.assertRaises(TypeError):
            parallelogram_area('a', 10)

    def test_non_numeric_values2(self):
        with self.assertRaises(TypeError):
            parallelogram_area(5, 'b')

    def test_non_numeric_values3(self):
        with self.assertRaises(TypeError):
            parallelogram_area('a', 'b')

import unittest
from mbpp_52_code import paralleloggram_area

class TestParallelogramArea(unittest.TestCase):
    def test_positive_b_and_h(self):
        self.assertEqual(parallelogram_area(5, 3), 15)

    def test_negative_b_and_h(self):
        self.assertEqual(parallelogram_area(-5, -3), 15)

    def test_zero_b_and_h(self):
        self.assertEqual(parallelogram_area(0, 0), 0)

    def test_zero_b_nonzero_h(self):
        self.assertEqual(parallelogram_area(0, 3), 0)

    def test_nonzero_b_zero_h(self):
        self.assertEqual(parallelogram_area(5, 0), 0)

    def test_non_integer_b_and_h(self):
        self.assertEqual(parallelogram_area(5.5, 3.5), 11.75)

    def test_non_numeric_b_and_h(self):
        with self.assertRaises(TypeError):
            parallelogram_area('five', 'three')

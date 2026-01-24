import unittest
from mbpp_52_code import parallelogram_area

class TestParallelogramArea(unittest.TestCase):
    def test_positive_b_and_h(self):
        self.assertEqual(parallelogram_area(3, 4), 12)

    def test_zero_b_and_h(self):
        self.assertEqual(parallelogram_area(0, 0), 0)

    def test_negative_b_and_h(self):
        self.assertEqual(parallelogram_area(-3, -4), 12)

    def test_negative_b_and_positive_h(self):
        self.assertEqual(parallelogram_area(-3, 4), -12)

    def test_positive_b_and_negative_h(self):
        self.assertEqual(parallelogram_area(3, -4), -12)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            parallelogram_area('3', '4')

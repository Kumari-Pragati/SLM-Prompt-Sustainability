import unittest
from mbpp_52_code import parallelogram_area

class TestParallelogramArea(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(parallelogram_area(5, 10), 50)
        self.assertEqual(parallelogram_area(15, 20), 300)

    def test_negative_numbers(self):
        self.assertEqual(parallelogram_area(-5, 10), -50)
        self.assertEqual(parallelogram_area(-15, -20), 300)

    def test_zero(self):
        self.assertEqual(parallelogram_area(0, 10), 0)
        self.assertEqual(parallelogram_area(15, 0), 0)
        self.assertEqual(parallelogram_area(0, 0), 0)

    def test_non_integer_values(self):
        self.assertEqual(parallelogram_area(2.5, 3.5), 8.75)
        self.assertEqual(parallelogram_area(5, 4), 20)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            parallelogram_area("5", 10)
        with self.assertRaises(TypeError):
            parallelogram_area(5, "10")
        with self.assertRaises(TypeError):
            parallelogram_area("5", "10")

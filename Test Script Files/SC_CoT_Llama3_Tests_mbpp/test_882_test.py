import unittest
from mbpp_882_code import parallelogram_perimeter

class TestParallelogramPerimeter(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(parallelogram_perimeter(5, 10), 100)

    def test_zero_base(self):
        self.assertEqual(parallelogram_perimeter(0, 10), 0)

    def test_zero_height(self):
        self.assertEqual(parallelogram_perimeter(5, 0), 0)

    def test_negative_base(self):
        self.assertEqual(parallelogram_perimeter(-5, 10), 0)

    def test_negative_height(self):
        self.assertEqual(parallelogram_perimeter(5, -10), 0)

    def test_non_numeric_base(self):
        with self.assertRaises(TypeError):
            parallelogram_perimeter('a', 10)

    def test_non_numeric_height(self):
        with self.assertRaises(TypeError):
            parallelogram_perimeter(5, 'b')

    def test_mixed_type_input(self):
        with self.assertRaises(TypeError):
            parallelogram_perimeter(5, 'b')

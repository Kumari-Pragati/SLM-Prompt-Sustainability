import unittest
from mbpp_882_code import parallelogram_perimeter

class TestParallelogramPerimeter(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(parallelogram_perimeter(5, 3), 30)
        self.assertEqual(parallelogram_perimeter(10, 4), 40)
        self.assertEqual(parallelogram_perimeter(7, 2), 28)

    def test_edge_cases(self):
        self.assertEqual(parallelogram_perimeter(0, 0), 0)
        self.assertEqual(parallelogram_perimeter(0, 5), 0)
        self.assertEqual(parallelogram_perimeter(5, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            parallelogram_perimeter('a', 3)
        with self.assertRaises(TypeError):
            parallelogram_perimeter(5, 'b')

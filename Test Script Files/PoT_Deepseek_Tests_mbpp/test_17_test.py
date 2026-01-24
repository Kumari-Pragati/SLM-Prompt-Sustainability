import unittest
from mbpp_17_code import square_perimeter

class TestSquarePerimeter(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(square_perimeter(5), 20)
        self.assertEqual(square_perimeter(10), 40)
        self.assertEqual(square_perimeter(0.5), 2)

    def test_edge_cases(self):
        self.assertEqual(square_perimeter(0), 0)
        self.assertEqual(square_perimeter(1), 4)

    def test_boundary_cases(self):
        self.assertEqual(square_perimeter(10000), 40000)
        self.assertEqual(square_perimeter(0.0001), 0.0004)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            square_perimeter('a')
        with self.assertRaises(TypeError):
            square_perimeter(None)
        with self.assertRaises(TypeError):
            square_perimeter([1, 2, 3])

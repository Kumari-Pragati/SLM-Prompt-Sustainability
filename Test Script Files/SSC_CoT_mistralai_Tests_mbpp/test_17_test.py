import unittest
from mbpp_17_code import square_perimeter

class TestSquarePerimeter(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(square_perimeter(3), 12)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(square_perimeter(0), 0)
        self.assertEqual(square_perimeter(1), 4)
        self.assertEqual(square_perimeter(2**32), 8*2**32)

    def test_negative_input(self):
        self.assertRaises(ValueError, square_perimeter, -1)

    def test_fractional_input(self):
        self.assertRaises(TypeError, square_perimeter, 3.14)

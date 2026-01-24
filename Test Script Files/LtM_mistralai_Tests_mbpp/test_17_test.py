import unittest
from mbpp_17_code import square_perimeter

class TestSquarePerimeter(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(square_perimeter(1), 4)
        self.assertEqual(square_perimeter(2), 8)
        self.assertEqual(square_perimeter(3), 12)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(square_perimeter(0), 0)
        self.assertEqual(square_perimeter(1000), 4000)
        self.assertRaises(TypeError, square_perimeter, 'not_a_number')

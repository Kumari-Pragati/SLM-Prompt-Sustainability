import unittest
from mbpp_17_code import square_perimeter

class TestSquarePerimeter(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(square_perimeter(5), 20)

    def test_boundary_case(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_edge_case(self):
        self.assertEqual(square_perimeter(1), 4)

    def test_special_case(self):
        self.assertEqual(square_perimeter(10), 40)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            square_perimeter('a')

import unittest
from mbpp_17_code import square_perimeter

class TestSquarePerimeter(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(square_perimeter(5), 20)

    def test_boundary_condition(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_edge_condition(self):
        self.assertEqual(square_perimeter(1), 4)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            square_perimeter('a')
